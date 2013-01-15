from pytest import raises

from signature import Signature, SignatureError


def test_positional_parameters_vs_positional_arguments():

    s = Signature('year', 'month', 'day')

    s << [2013, 1, 15]
    assert s.year  == s[0] == 2013
    assert s.month == s[1] == 1
    assert s.day   == s[2] == 15
    assert list(s) == [2013, 1, 15]

    with raises(SignatureError):
        s << []

    with raises(SignatureError):
        s << [2013, 1, 15, 20, 44]


def test_keyword_parameters_vs_positional_arguments():

    s = Signature(('year', 1970), ('month', 1), ('day', 1))

    s << [2013, 1, 15]
    assert list(s) == [2013, 1, 15]

    s << [2013]
    assert list(s) == [2013, 1, 1]

    s << []
    assert list(s) == [1970, 1, 1]

    with raises(SignatureError):
        s << [2013, 1, 15, 20, 44]


def test_mixed_parameters_vs_positional_arguments():

    s = Signature('year', ('month', 1), ('day', 1))

    s << [2013, 1, 15]
    assert list(s) == [2013, 1, 15]

    s << [2013]
    assert list(s) == [2013, 1, 1]

    with raises(SignatureError):
        s << []

    with raises(SignatureError):
        s << [2013, 1, 15, 20, 44]





def test_mixed_parameters_vs_mixed_arguments():

    s = Signature('year', 'month', ('day', 1), ('hour', 0))

    if 0:
        s << Call(*args, **kwargs)
        s << Call(2013, month=1, day=15)
        assert list(s) == [2013, 1, 15, 0]

        s(*args, **kwargs)
        s(2013, month=1, day=15)
        assert list(s) == [2013, 1, 15, 0]

        args = s(*args, **kwargs)
        args = s(2013, month=1, day=15)
        assert list(args) == [2013, 1, 15, 0]
