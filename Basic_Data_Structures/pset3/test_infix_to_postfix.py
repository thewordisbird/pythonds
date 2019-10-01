import pytest

from infix_to_postfix import infix_to_postfix 

@pytest.mark.parametrize('infix, postfix', 
                        [
                            ('A + B', 'A B +'),
                            ('A + B * C', 'A B C * +'),
                            ('( A + B ) * C', 'A B + C *'),
                            ('( A + B ) * C - ( D - E ) * ( F + G )', 'A B + C * D E - F G + * -')
                        ])
def test_infix_to_postfix(infix, postfix):
    assert infix_to_postfix(infix) == postfix

