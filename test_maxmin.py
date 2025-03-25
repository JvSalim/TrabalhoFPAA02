import pytest
from main import max_min_select

def test_elemento_unico():
    assert max_min_select([42], 0, 0) == (42, 42)

def test_dois_elementos():
    assert max_min_select([15, 3], 0, 1) == (3, 15)

def test_elementos_negativos():
    arr = [-5, -1, -10]
    assert max_min_select(arr, 0, 2) == (-10, -1)

def test_array_grande():
    arr = list(range(1000))
    assert max_min_select(arr, 0, 999) == (0, 999)
