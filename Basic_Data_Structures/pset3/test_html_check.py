import pytest
from html_check import html_check

@ pytest.mark.parametrize('doc_path, output',
                            [
                                ('html_1.html', True),
                                ('html_2.html', False),
                                ('html_3.html', False)
                            ])
def test_html_check(doc_path, output):
    assert html_check(doc_path) == output