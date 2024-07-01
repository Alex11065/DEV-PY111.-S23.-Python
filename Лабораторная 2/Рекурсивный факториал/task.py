def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    # реализовать рекурсивный алгоритм нахождения факториала

    if n < 0:
        raise ValueError("Факториал считается от не отрицательных целых чисел")
    if isinstance(n, (float, str, set, dict)):
        raise TypeError("Факториал считается от не отрицательных целых чисел")

    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


if __name__ == "__main__":
   pass


    # print(factorial_recursive(5))
    # print(factorial_recursive(2.4))
    # print(factorial_recursive(-10))
