import pytest
from templates.testing_frameworks.pytest.main.main import basic_add
from templates.testing_frameworks.pytest.main.main import is_true
from templates.testing_frameworks.pytest.main.main import divide_by_zero


# Must start with test_*
def test_value():
    assert basic_add(1, 2) == 3
    assert basic_add(-1, 2) == 1


def test_is_true():
    assert is_true(True)
    assert not is_true(False)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_by_zero()

