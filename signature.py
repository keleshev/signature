class SignatureError(Exception):
    pass


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

    @property
    def is_required(self):
        return self.default is Nothing


class Signature(object):

    def __init__(self, *params):
        self._params = map(Param, params)
        # TODO test, implement that keyword params follow positional params

    def __iter__(self):
        return (self.__dict__[p.name] for p in self._params)

    def __getitem__(self, key):
        return list(iter(self))[key]

    def __lshift__(self, other):
        self.__dict__ = {'_params': self._params}  # reset __dict__
        if len(other) > len(self._params):
            raise SignatureError()  # TODO better error reporting
        if len(other) < len([p for p in self._params if p.is_required]):
            raise SignatureError()  # TODO test
        # Pad `other` to make it's length same as `self._params`
        other = other + [Nothing] * (len(self._params) - len(other))
        for param, arg in zip(self._params, other):
            if arg is Nothing:
                if param.default is Nothing:
                    assert not 'reachable'
                else:
                    self.__dict__[param.name] = param.default
            else:
                self.__dict__[param.name] = arg




