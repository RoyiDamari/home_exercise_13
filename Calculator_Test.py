import ProgramHomeExercise13 as calc
import pytest


# d


def test_power_four():
    # Arrange
    x: int = 2;
    y: int = 4;
    expected: int = 16;

    # Act
    actual: int = calc.power(x, y);

    # Assert
    assert actual == expected;


# e


def test_power_three():
    # Arrange
    x: int = 2;
    y: int = 3;
    expected: int = 8;

    # Act
    actual: int = calc.power(x, y);

    # Assert
    assert actual == expected;


# f


def test_power_zero():
    # Arrange
    x: int = 9;
    y: int = 0;
    expected: int = 1;

    # Act
    actual: int = calc.power(x, y);

    # Assert
    assert actual == expected;


# g


def test_sqrt():
    # Arrange
    x: int = 25;
    expected: int = 5;

    # Act
    actual: float = calc.sqrt(x);

    # Assert
    assert actual == expected;


# h


def test_sqrt_error():
    # Arrange
    x: int = -5;

    with pytest.raises(ValueError) as ex:
        calc.sqrt(x);

  

# i


def test_is_prime_one():
    # Arrange
    x: int = 1;
    expected: bool = False;

    # Act
    actual: bool = calc.is_prime(x);

    # Assert
    assert actual == expected;


# j


def test_is_prime_two():
    # Arrange
    x: int = 2;
    expected: bool = True;

    # Act
    actual: bool = calc.is_prime(x);

    # Assert
    assert actual == expected;


# k


def test_is_prime_sixteen():
    # Arrange
    x: int = 16;
    expected: bool = False;

    # Act
    actual: bool = calc.is_prime(x);

    # Assert
    assert actual == expected;


# l


def test_is_prime_minus_three():
    # Arrange
    x: int = -3;
    expected: bool = False;

    # Act
    actual: bool = calc.is_prime(x);

    # Assert
    assert actual == expected;


# m


def test_is_prime_zero():
    # Arrange
    x: int = 0;
    expected: bool = False;

    # Act
    actual: bool = calc.is_prime(x);

    # Assert
    assert actual == expected;


# n


def test_factorial_four():
    # Arrange
    x: int = 4;
    expected: int = 24;

    # Act
    actual: int = calc.factorial(x);

    # Assert
    assert actual == expected;


# o


def test_factorial_zero():
    # Arrange
    x: int = 0;
    expected: int = 1;

    # Act
    actual: int = calc.factorial(x);

    # Assert
    assert actual == expected;


# p


def test_factorial_one():
    # Arrange
    x: int = 1;
    expected: int = 1;

    # Act
    actual: int = calc.factorial(x);

    # Assert
    assert actual == expected;


# q


def test_factorial_five():
    # Arrange
    x: int = 5;
    expected: int = 120;

    # Act
    actual: int = calc.factorial(x);

    # Assert
    assert actual == expected;


# r


def test_factorial_minus_three():
    # Arrange
    x: int = -3;

    with pytest.raises(ValueError) as ex:
        calc.factorial(x);

    # Assert
    assert str(ex.value) == "factorial not defined for negative values";
