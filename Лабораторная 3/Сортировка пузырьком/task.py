from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """

    flag = True  # Ставим флаг для того что бы запустился наш цикл

    while flag:
        flag = False  # меняем флаг после запуска
        for val in range(len(container) - 1):
            if container[val] > container[val + 1]:
                container[val], container[val + 1] = container[val + 1], container[val]
                flag = True  # если были перестановки значений, то меняем флаг, что бы цикл запустился
    return container


if __name__ == "__main__":
    print(sort([1, 3, 2, 5, 48, 8, 7, 9]))

    #  реализовать алгоритм сортировки пузырьком

