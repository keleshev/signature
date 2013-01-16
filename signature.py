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
        if len(args) < len([p for p in self._params if p.default is Nothing]):
            raise TypeError()  # TODO test
        # Pad `args` to make it's length same as `self._params`
        args = args + (Nothing,) * (len(self._params) - len(args))
        values = {}
        for param, arg in zip(self._params, args):
            if arg is Nothing:
                if param.default is Nothing:
                    assert not 'reachable'
                else:
                    values[param.name] = param.default
            else:
                values[param.name] = arg
        Arguments = namedtuple('Argument', [p.name for p in self._params])
        return Arguments(**values)
