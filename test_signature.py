from pytest import raises

from signature import Signature, SignatureError


def test_positional_parameters_vs_positional_arguments():

    signature = Signature('year', 'month', 'day')

    args = signature(*[2013, 1, 15])
    assert args.year  == args[0] == 2013
    assert args.month == args[1] == 1
    assert args.day   == args[2] == 15
    assert list(args) == [2013, 1, 15]

    with raises(SignatureError):
        signature(*[])
    with raises(SignatureError):
        signature(*[2013, 1, 15, 20, 44])


def test_keyword_parameters_vs_positional_arguments():

    signature = Signature(('year', 1970), ('month', 1), ('day', 1))

    assert list(signature(2013, 1, 15)) == [2013, 1, 15]
    assert list(signature(2013)) == [2013, 1, 1]
    assert list(signature()) == [1970, 1, 1]

    with raises(SignatureError):
        signature(2013, 1, 15, 20, 44)


def test_mixed_parameters_vs_positional_arguments():

    signature = Signature('year', ('month', 1), ('day', 1))

    assert list(signature(2013, 1, 15)) == [2013, 1, 15]
    assert list(signature(2013)) == [2013, 1, 1]

    with raises(SignatureError):
        signature()
    with raises(SignatureError):
        signature(2013, 1, 15, 20, 44)


def test_mixed_parameters_vs_mixed_arguments():

    signature = Signature('year', 'month', ('day', 1), ('hour', 0))

    if 0:
        args = signature(*args, **kwargs)
        args = signature(2013, month=1, day=15)
        assert list(args) == [2013, 1, 15, 0]
