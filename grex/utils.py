import re
import collections


ALLOWED_FEATURE_POSITIONS = ["own", "parent", "child", "prev", "next"]

class Dict:
    def __init__(self, values):
        values = set(values)
        self._id_to_str = list()
        self._str_to_id = dict()

        for v in values:
            self._str_to_id[v] = len(self._id_to_str)
            self._id_to_str.append(v)

    def str_to_id(self, v):
        return self._str_to_id[v]

    def id_to_str(self, v):
        return self._id_to_str[v]

    def __len__(self):
        return len(self._id_to_str)


class StringMatcher:
    def __init__(self, method, regexps):
        assert method in ["include", "exclude"]
        self.include = (method == "include")

        if type(regexps) != list:
            regexps = [regexps]
        assert all(type(p) == str for p in regexps)
        self.regexps = regexps

    def __call__(self, string):
        m = any(re.fullmatch(p, string) for p in self.regexps)
        return m if self.include else not m


class LemmaFilter:
    def __init__(self, top_k=0, allowed_upos=list()):
        self.top_k = top_k
        self.allowed_upos = allowed_upos
        self.counter = None
        self.is_initialized = False
        self.allowed_lemmas = None

    def check_initialization(self):
        if not self.is_initialized:
            raise RuntimeError("Unitialized")

    def transform_upos(self, upos):
        if len(self.allowed_upos) == 0:
            return "**UNDEF**"
        else:
            return upos

    def transform_lemma(self, lemma):
        return lemma.lower()

    def reset_counter(self):
        self.counter = collections.Counter()
        self.is_initialized = False

    def freeze_counter(self):
        assert self.counter is not None
        self.is_initialized = True
        if self.top_k <= 0:
            self.allowed_lemmas = None
        else:
            allowed_lemmas = collections.defaultdict(lambda: set())
            for (lemma, upos), c in self.counter.most_common(self.top_k):
                allowed_lemmas[upos].add(lemma)
            self.allowed_lemmas = dict(allowed_lemmas)

    def update_counter(self, lemma, upos):
        assert self.counter is not None
        upos = self.transform_upos(upos)
        lemma = self.transform_lemma(lemma)

        if len(self.allowed_upos) == 0 or upos in self.allowed_upos:
            self.counter[(lemma, upos)] += 1

    def __call__(self, lemma, upos):
        self.check_initialization()

        if self.top_k < 0:
            return True
        if self.top_k == 0:
            return False

        upos = self.transform_upos(upos)
        lemma = self.transform_lemma(lemma)
        return lemma in self.allowed_lemmas.get(upos, set())


class FeaturePredicate:
    def __init__(self):
        self.matchers = dict()
        self.lemma_filters = dict()

    @staticmethod
    def from_config(config, templates=dict()):
        obj = FeaturePredicate()

        for node, tpl in config.items():
            if type(tpl) == str:
                obj.matchers[node] = templates.matchers[tpl]
                obj.lemma_filters[node] = templates.lemma_filters[tpl]
            else:
                assert node not in obj.matchers
                obj.matchers[node] = dict()
                obj.lemma_filters[node] = dict()
                for k, v in tpl.items():
                    assert k in ALLOWED_FEATURE_POSITIONS
                    assert all(k2 in ["method", "regexp", "lemma_top_k", "lemma_upos_filter"] for k2 in v.keys())
                    obj.matchers[node][k] = StringMatcher(v["method"], v["regexp"])
                    obj.lemma_filters[node][k] = LemmaFilter(v.get("lemma_top_k", -1), v.get("lemma_upos_filter", list()))

        return obj

    def __call__(self, name, where, feature):
        assert where in ALLOWED_FEATURE_POSITIONS
        if name not in self.matchers:
            raise KeyError("Feature matching has not been implemented for node '%s'" % name)
        if where not in self.matchers[name]:
            return False
        else:
            return self.matchers[name][where](feature)

    def reset_lemmas_counter(self):
        for k, v in self.lemma_filters.items():
            for k2, v2 in v.items():
                v2.reset_counter()

    def freeze_lemmas_counter(self):
        for k, v in self.lemma_filters.items():
            for k2, v2 in v.items():
                v2.freeze_counter()

    def update_lemmas_counter(self, node_name, rel_name, lemma, upos):
        self.lemma_filters[node_name][rel_name].update_counter(lemma, upos)

    def check_lemma(self, node_name, rel_name, lemma, upos):
        return self.lemma_filters[node_name][rel_name](lemma, upos)
