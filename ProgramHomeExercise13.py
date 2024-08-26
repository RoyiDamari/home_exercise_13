# Exercise 1
import math
# a


def power(num: int, p: int) -> int:
    return pow(num, p);


print(power(2, 3));


# b


def sqrt(num: int) -> float:
    return math.sqrt(num);


print(sqrt(9));


# c


def is_prime(num: int) -> bool:
    if num <= 1:  # 1, 0, and negative numbers are not prime
        return False;
    if num == 2:  # 2 is the only even prime number
        return True;
    if num % 2 == 0:  # Other even numbers are not prime
        return False;

    # Check for factors from 3 up to the square root of n
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False;

    return True;


print(is_prime(7));


def factorial(num: int) -> int | ValueError:
    if num < 0:
        raise ValueError("factorial not defined for negative values");

    result: int = 1;
    for i in range(2, num + 1):
        result *= i;

    return result;


print(factorial(5));
