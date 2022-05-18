# # Unit testing refers to taking a component of a program and testing it in isolation. Generally this means testing an individual class or function.
def recursive_fibonacci(n):
    return n if n <= 1 else recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


assert to_fahrenheit(30) == 86

from temperature import to_fahrenheit
import unittest, pytest


class TestTemperature(unittest.TestCase):
    def test_to_farenheit(self):
        self.assertEqual(to_fahrenheit(30), 86)


def test_non_numeric_input():
    with pytest.raises(TypeError):
        recursive_fibonacci("foo")


@pytest.mark.parametrize("number,expected", [(0, 0), (1, 1), (2, 1), (3, 2)])
def test_initial_numbers(number, expected):
    assert recursive_fibonacci(number) == expected


def test_approximate_pi():
    assert 22 / 7 == pytest.approx(math.pi, abs=1e-2)
