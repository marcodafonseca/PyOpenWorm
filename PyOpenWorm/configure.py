
# a class for modules that need outside objects to parameterize their behavior (because what are generics?)
# Modules inherit from this class and use their self['expected_configured_property']
class BadConf(BaseException):
    pass
class _C:
    def __init__(self, v):
        self.v = v
    def get(self):
        return self.v

class Configure:
    def __init__(self, conf=False):

        # XXX: Maybe should require the subclass to declare its dependencies?
        if not conf:
            self._properties = {}
        elif isinstance(conf, type(self)):
            self._properties = conf._properties
        else:
            raise BadConf("Not a configuration object")

    def __setitem__(self, pname, value):
        if not hasattr(value, "get"):
            value = _C(value)
        self._properties[pname] = value

    def __getitem__(self, pname):
        return self._properties[pname].get()