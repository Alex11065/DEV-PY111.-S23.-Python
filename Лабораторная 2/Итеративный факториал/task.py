def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    result = 1
    if n < 0:
        raise ValueError("Факториал не может быть отрицательным числом")
    elif n == 0 or n == 1:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print(factorial_iterative(5))

    import math
    number = 5
    factorial_value = math.factorial(number)
    print(factorial_value)
# реализовать итеративный алгоритм нахождения факториала
