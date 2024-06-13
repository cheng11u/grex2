import grewpy
import re

CLOSED_POS_TAGS = {
    "AUX",
    "ADP",
    "PRON",
    "DET",
    "SCONJ",
    "CCONJ",
    "PART"
}

# le terme "similar" n'est pas du tout adapté,
# mais c'est en gros les POS tags qu'on veut merger ensemble
# pour ajouter de nouvelles features
# càd que plutôt qu'avoir seulement "POS=NOUN",
# on veut aussi avoir "POS=NOUN|PROPN"
SIMILAR_POS_TAGS = [
    # use list to fix order, probably unecessary,
    # but just in case
    [
        "NOUN", "PROPN"
    ],
    [
        "NOUN", "PROPN", "PRON"
    ],
    [
        "AUX", "VERB"
    ],
    [
        "DET", "NUM"
    ]
]


def parents_from_successors(sucs):
    parents = dict()
    for head, children in sucs.items():
        for cid, rel in children:
            assert cid not in parents
            parents[cid] = head, rel
    return parents


def extract_features(draft, match, feature_predicate, include_metadata=False):
    sentence = draft[match["sent_id"]]
    parents = parents_from_successors(sentence.sucs)
    selected_node_ids = set(match["matching"]["nodes"].values())
    features = dict()

    # sentence level meta features
    if include_metadata:
        for k, v in sentence.meta.items():
            if k != "sent_id" and not k.startswith("text"):
                features["meta:" + k] = v

    for node_name, node_id in match["matching"]["nodes"].items():
        # Node features
        nodes_features = sentence.features[node_id]
        for k, v in nodes_features.items():
            if feature_predicate(node_name, "own", k):
                features["node:" + node_name + ":own:" + k] = v

        # relation with parent
        parent_id, rel = parents[node_id]
        if feature_predicate(node_name, "parent", "rel_shallow"):
            features["node:" + node_name + ":parent:rel_shallow"] = ":".join(rel[rel_key] for rel_key in ["1", "2"] if rel_key in rel)
        if feature_predicate(node_name, "parent", "rel_deep") and "deep" in rel:
            features["node:" + node_name + ":parent:rel_deep"] = rel["deep"]

        # position of parent
        if feature_predicate(node_name, "parent", "position"):
            features["node:" + node_name + ":parent:position"] = "before" if int(parent_id) < int(node_id) else "after"

        # head feature
        if parent_id not in selected_node_ids:
            parent_features = sentence.features[parent_id]
            for k, v in parent_features.items():
                if feature_predicate(node_name, "parent", k):
                    features["node:" + node_name + ":parent:" + k] = v

        # prev word
        prev_id = str(int(node_id) - 1)
        if prev_id in sentence.features and prev_id not in selected_node_ids:
            prev_features = sentence.features[prev_id]
            for k, v in prev_features.items():
                if feature_predicate(node_name, "prev", k):
                    features["node:" + node_name + ":prev:" + k] = v

        # next word
        next_id = str(int(node_id) + 1)
        if next_id in sentence.features and next_id not in selected_node_ids:
            next_features = sentence.features[next_id]
            for k, v in next_features.items():
                if feature_predicate(node_name, "next", k):
                    features["node:" + node_name + ":next:" + k] = v

        # children features
        for child_id, child_rel in sentence.sucs.get(node_id, list()):
            # only consider children that are not matched nodes
            if child_id in selected_node_ids:
                continue

            # child features
            child_features = sentence.features[child_id]
            for k, v in child_features.items():
                if feature_predicate(node_name, "child", k):
                    key = "node:" + node_name + ":child:" + k
                    if key not in features:
                        features[key] = {v}
                    else:
                        features[key].add(v)

            # relation with child
            _, rel = parents[child_id]
            if feature_predicate(node_name, "child", "rel_shallow"):
                k = "node:" + node_name + ":child:rel_shallow"
                v = ":".join(rel[rel_key] for rel_key in ["1", "2"] if rel_key in rel)
                if k not in features:
                    features[k] = {v}
                else:
                    features[k].add(v)
            if feature_predicate(node_name, "child", "rel_deep") and "deep" in rel:
                k = "node:" + node_name + ":child:rel_deep"
                v = rel["deep"]
                if k not in features:
                    features[k] = {v}
                else:
                    features[k].add(v)

    return features


def extract_data(treebank_path, scope, conclusion, conclusion_meta, feature_predicate):
    if conclusion is None and conclusion_meta is None:
        raise RuntimeError("No conclusion provided in configuration")

    corpus = grewpy.Corpus(treebank_path)
    draft = grewpy.CorpusDraft(treebank_path)

    req = grewpy.Request(scope)
    if conclusion is not None:
        matches = corpus.search(req, clustering_parameter=["{" + conclusion + "}"])
        matches = [(sent, c) for c, sents in matches.items() for sent in sents]
    else:
        matches = [(sent, "Yes") for sent in corpus.search(req)]

    if conclusion_meta is not None:
        conclusion_meta = {
            k: v if type(v) is list else [v]
            for k, v in conclusion_meta.items()
        }

        matches = [
            (sent, "No")
            if c == "No"
            else (
                (sent, "Yes")
                if all(
                    any(re.fullmatch(p, sent[k]) for p in v)
                    for k, v in conclusion_meta.items()
                )
                else (sent, "No")
            )
            for sent, c in matches
            if all(k in sent for k in conclusion_meta.keys())
        ]

    data = []
    for match, c in matches:
        assert c in ["Yes", "No"]

        data.append({
            "input": extract_features(draft, match, feature_predicate),
            "output": 1 if c == "Yes" else 0
        })

    return data