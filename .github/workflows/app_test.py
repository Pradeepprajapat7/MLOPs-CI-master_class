import pytest
from app import square, cube, fifth_power


def test_square():
    assert square(2) == 4
    assert square(3) == 9


def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27


def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243


def test_invalid_input():
    with pytest.raises(TypeError):
        square("abc")