"""
Tests unitarios para los tres algoritmos de Fibonacci.
"""

import pytest
from fibonacci import fibonacci_recursive, fibonacci_iterative, fibonacci_generator

# Casos conocidos de la serie: índice → valor
KNOWN = {
    0: 0, 1: 1, 2: 1, 3: 2, 4: 3,
    5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55,
}


@pytest.mark.parametrize("n,expected", KNOWN.items())
def test_recursive(n, expected):
    assert fibonacci_recursive(n) == expected


@pytest.mark.parametrize("n,expected", KNOWN.items())
def test_iterative(n, expected):
    assert fibonacci_iterative(n) == expected


def test_generator_sequence():
    result = list(fibonacci_generator(11))
    assert result == list(KNOWN.values())


def test_negative_raises():
    with pytest.raises(ValueError):
        fibonacci_recursive(-1)
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)


def test_all_methods_agree():
    for n in range(20):
        rec = fibonacci_recursive(n)
        ite = fibonacci_iterative(n)
        assert rec == ite, f"Discrepancia en n={n}: recursiva={rec}, iterativa={ite}"
