import pytest
from fractions import Fraction, gcd, int_chk


def test_pytest():
    assert 1 == 1

def test_gcd():
    assert gcd(4, 8) == 4

def test_show_fraction():
    f = Fraction(1, 2)
    assert f.show() == "1/2"

@pytest.mark.parametrize('num_1, den_1, num_2, den_2', 
                        [(1, 2, 1, 2),
                        (-1,3, -1,3),
                        (1,-3, -1, 3)
                        ])
def test_eq_fractions(num_1, den_1, num_2, den_2):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    assert f1 == f2

@pytest.mark.parametrize('num_1, den_1, num_2, den_2', 
                        [(1, 2, 3, 4),
                        (-1,3, -4,3),
                        (3,-3, -6, 3)
                        ])
def test_ne_fractions(num_1, den_1, num_2, den_2):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    assert f1 != f2

def test_gt_fractions():
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)

    assert f2 > f1

def test_ge_functions():
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)
    f3 = Fraction(4, 6)

    assert f2 >= f1
    assert f2 >= f3

def test_lt_fractions():
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)

    assert f1 < f2

def test_ge_functions():
    f1 = Fraction(1,2)
    f2 = Fraction(2,3)
    f3 = Fraction(4, 6)

    assert f1 <= f2
    assert f2 <= f3

@pytest.mark.parametrize('num_1, den_1, num_2, den_2, fcheck', 
                        [(1, 2, 3, 4, Fraction(5,4)),
                        (-1, 2, 3, 4, Fraction(1,4)),
                        (1, 2, -3, 4,Fraction(-1,4)),
                        (1, -2, 3, 4, Fraction(1,4)),
                        (1, 2, 3, -4,Fraction(-1,4)),
                        ])
def test_add_fractions(num_1, den_1, num_2, den_2, fcheck):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    fsum = f1 + f2    
    assert fsum == fcheck

@pytest.mark.parametrize('num_1, den_1, num_2, den_2, fcheck', 
                        [(1, 2, 3, 4, Fraction(-1,4)),
                        (-1, 2, 3, 4, Fraction(-5,4)),
                        (1, 2, -3, 4,Fraction(5,4)),
                        (1, -2, 3, 4, Fraction(-5,4)),
                        (1, 2, 3, -4,Fraction(5,4)),
                        ])
def test_sub_fractions(num_1, den_1, num_2, den_2, fcheck):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    fdiff = f1-f2    
    assert fdiff == fcheck

@pytest.mark.parametrize('num_1, den_1, num_2, den_2, fcheck', 
                        [(1, 2, 3, 4, Fraction(3,8)),
                        (-1, 2, 3, 4, Fraction(-3,8)),
                        (1, 2, -3, 4,Fraction(-3,8)),
                        (1, -2, 3, 4, Fraction(-3,8)),
                        (-1, 2, 3, -4,Fraction(3,8)),
                        ])
def test_mul_fractions(num_1, den_1, num_2, den_2, fcheck):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    fprod = f2 * f1
    assert fprod == fcheck

@pytest.mark.parametrize('num_1, den_1, num_2, den_2, fcheck', 
                        [(1, 2, 3, 4, Fraction(4, 6)),
                        (-1, 2, 3, 4, Fraction(-4, 6)),
                        (1, 2, -3, 4,Fraction(-4, 6)),
                        (1, -2, 3, 4, Fraction(-4, 6)),
                        (-1, 2, 3, -4,Fraction(4, 6)),
                        ])
def test_truediv_fractions(num_1, den_1, num_2, den_2, fcheck):
    f1 = Fraction(num_1, den_1)
    f2 = Fraction(num_2, den_2)

    fquotient = f1 / f2
    assert fquotient == fcheck


def test_getNum():
    f1 = Fraction(2, 3)

    assert f1.getNum() == 2

def test_getDen():
    f1 = Fraction(2, 3)

    assert f1.getDen() == 3

@pytest.mark.parametrize('ints', [-5, 0, 3, 10])
def test_int_check(ints):
    assert int_chk(ints) == True

@pytest.mark.parametrize('non_ints', ['Justin', 1.2,  2+3j])
def test_int_check_raise_error(non_ints):
    with pytest.raises(TypeError):
        int_chk(non_ints)

@pytest.mark.parametrize('num, den', [('Justin', 1),  
                                        (1.2, 1),  
                                        (2+3j, 1),
                                        (1, 'justin'),
                                        (1, 1.2),
                                        (1, 2+3j)])
def test_add_fraction_wrong_data_type(num, den):
    with pytest.raises(TypeError):
        Fraction(num, den)


def test_add_fraction_to_int():

        i = 4
        f = Fraction(3, 5)

        sum = i + f
        assert sum == Fraction(23, 5)
