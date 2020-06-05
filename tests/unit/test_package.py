import pytest
import sys
print('[DEBUG] Python path = {}'.format(sys.path))
from pyqt_widgets import widgets


def test_helloworld():
    """
    """
    assert "Hello World"

    assert 1 == 1


if __name__ == '__main__':
    pytest.main([__file__])
