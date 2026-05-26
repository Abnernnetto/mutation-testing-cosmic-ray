import pytest
from src.calculator import add, subtract, is_positive


# Particionamento de equivalência + valores positivos, negativos, zero e floats
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, 3, 1),
        (-2, -3, -5),
        (10, 0, 10),
        (1.5, 2.5, 4.0),
        (-1.5, 2.5, 1.0),
    ],
)
def test_add_cases(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 0, 0),
        (3, 5, -2),
        (-5, -3, -2),
        (10, 0, 10),
        (1.5, 0.5, 1.0),
        (-1.5, -0.5, -1.0),
    ],
)
def test_subtract_cases(a, b, expected):
    assert subtract(a, b) == expected


# Valores de fronteira em torno de zero
@pytest.mark.parametrize(
    "number,expected",
    [
        (10, True),
        (1, True),
        (0.0001, True),
        (0, False),
        (-0.0001, False),
        (-1, False),
        (-10, False),
    ],
)
def test_is_positive_cases(number, expected):
    assert is_positive(number) is expected


# Testes relacionais: ajudam a pegar mutações que ainda passam em casos isolados
@pytest.mark.parametrize(
    "a,b",
    [
        (1, 2),
        (10, -3),
        (-5, 7),
        (0, 9),
    ],
)
def test_add_inverse_relation(a, b):
    assert subtract(add(a, b), b) == a


@pytest.mark.parametrize(
    "a,b",
    [
        (5, 3),
        (10, -4),
        (-8, -2),
        (0, 6),
    ],
)
def test_subtract_inverse_relation(a, b):
    assert add(subtract(a, b), b) == a


# Propriedade importante do add: comutatividade
@pytest.mark.parametrize(
    "a,b",
    [
        (1, 2),
        (-5, 7),
        (0, 9),
        (3.5, 2.5),
    ],
)
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)