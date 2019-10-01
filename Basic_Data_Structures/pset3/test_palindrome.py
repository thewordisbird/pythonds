import pytest
from palindrome import palindrome

@pytest.mark.parametrize('string, output',
                        [
                            ('No lemon, no melon', True),
                            ('Red rum, sir, is murder.', True),
                            ('Racecar', True),
                            ('Justin', False),
                            ('Not a palindrome', False)
                        ])
def test_palindrome(string, output):
    assert palindrome(string) == output                        