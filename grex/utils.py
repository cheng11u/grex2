import re


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


class FeaturePredicate:
    def __init__(self):
        self.matchers = dict()

    @staticmethod
    def from_config(config, templates=dict()):
        obj = FeaturePredicate()

        for node, tpl in config.items():
            if type(tpl) == str:
                obj.matchers[node] = templates.matchers[tpl]
            else:
                assert node not in obj.matchers
                obj.matchers[node] = dict()
                for k, v in tpl.items():
                    assert k in ALLOWED_FEATURE_POSITIONS
                    obj.matchers[node][k] = StringMatcher(v["method"], v["regexp"])

        return obj

    def __call__(self, name, where, feature):
        assert where in ALLOWED_FEATURE_POSITIONS
        if name not in self.matchers:
            raise KeyError("Feature matching has not been implemented for node '%s'" % name)
        if where not in self.matchers[name]:
            return False
        else:
            return self.matchers[name][where](feature)