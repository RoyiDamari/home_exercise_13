# Exercise 1
import math
# a


def power(num: int, p: int) -> int:
    return pow(num, p);


# b


def sqrt(num: int) -> float:
    return math.sqrt(num);


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



def factorial(num: int) -> int | ValueError:
    if num < 0:
        raise ValueError("factorial not defined for negative values");

    result: int = 1;
    for i in range(2, num + 1):
        result *= i;


    return result;

if __name__ == "__main__":
    print(power(2, 3));
    print(is_prime(7));;
    print(sqrt(9));
    print(factorial(5));
