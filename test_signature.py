from pytest import raises

from signature import Signature


def test_positional_parameters_vs_positional_arguments():

    signature = Signature('year', 'month', 'day')

    args = signature(2013, 1, 15)
    assert args.year  == args[0] == 2013
    assert args.month == args[1] == 1
    assert args.day   == args[2] == 15
    assert args == (2013, 1, 15)

    with raises(TypeError):
        signature()
    with raises(TypeError):
        signature(2013, 1, 15, 20, 44)


def test_keyword_parameters_vs_positional_arguments():

    signature = Signature(('year', 1970), ('month', 1), ('day', 1))

    assert signature(2013, 1, 15) == (2013, 1, 15)
    assert signature(2013) == (2013, 1, 1)
    assert signature() == (1970, 1, 1)

    with raises(TypeError):
        signature(2013, 1, 15, 20, 44)


def test_mixed_parameters_vs_positional_arguments():

    signature = Signature('year', ('month', 1), ('day', 1))

    assert signature(2013, 1, 15) == (2013, 1, 15)
    assert signature(2013) == (2013, 1, 1)

    with raises(TypeError):
        signature()
    with raises(TypeError):
        signature(2013, 1, 15, 20, 44)


def test_mixed_parameters_vs_mixed_arguments():

    signature = Signature('year', 'month', ('day', 1), ('hour', 0))

    assert signature(     2013,       1,     15) == (2013, 1, 15, 0)
    assert signature(     2013,       1, day=15) == (2013, 1, 15, 0)
    assert signature(     2013, month=1, day=15) == (2013, 1, 15, 0)
    assert signature(year=2013, month=1, day=15) == (2013, 1, 15, 0)
    with raises(TypeError):
        signature(year=2013, month=1, day=15, nonexistent=True)
