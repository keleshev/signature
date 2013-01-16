from collections import namedtuple


Nothing = object()
class Param(object):

    def __init__(self, name_or_tuple):
        # TODO better error reporting
        if type(name_or_tuple) is tuple:
            self.name, self.default = name_or_tuple
        else:
            assert type(name_or_tuple) is str
            self.name = name_or_tuple
            self.default = Nothing

    def __repr__(self):
        if self.default is Nothing:
            return 'Param(%r)' % self.name
        return 'Param(%r, %r)' % (self.name, self.default)


class Signature(object):

    def __init__(self, *params):
        self._params = map(Param, params)
        # TODO test, implement that keyword params follow positional params

    def __call__(self, *args, **kwargs):
        if len(args) > len(self._params):
            raise TypeError()  # TODO better error reporting
        if not set(kwargs) <= set([p.name for p in self._params]):
            raise TypeError()
        # See PEP 3102
        slots = {}
        for param, arg in zip(self._params, args):
            slots[param.name] = arg
        for keyword, argument in kwargs.items():
            if keyword in slots:
                raise TypeError()
            for param in [p for p in self._params if p.name not in slots]:
                if param.name == keyword:
                    slots[param.name] = kwargs[keyword]
        for param in [p for p in self._params if p.name not in slots]:
            if param.default is not Nothing:
                slots[param.name] = param.default
            else:
                raise TypeError()
        Arguments = namedtuple('Argument', [p.name for p in self._params])
        return Arguments(**slots)
