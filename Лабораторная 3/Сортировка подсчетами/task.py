from collections import defaultdict
from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if len(container) == 0 or len(container) == 1:
        return container  # Сколько я мучался с этой проверкой [],[1], а оказалось все так просто

    max_arr = max(container)  # максимальное значение
    count = [0] * (max_arr + 1)  # список заполненный нулями
    sort_list = []  # результирующий список

    for i in container:
        count[i] += 1  # подсчет элементов

    for ind, val in enumerate(count):
        sort_list.extend([ind] * val)  # умножаем индекс на значение и добавляем в результирующий список

    return sort_list

    #  реализовать алгоритм сортировки подсчетами


if __name__ == "__main__":
    print(sort([2, 1, 4, 5, 4, 2, 1]))
    print(sort([]))
    print(sort([1]))
    # arr = []
    # print(sort(arr))
    # def sort2(arr2: Sequence[int]) -> Sequence[int]:
    # max_value = max(container)
    # min_value = min(container)
    # count = [0] * (max_value - min_value + 1)
    # sort_count = []
    #
    # if container == 0 or container == 1:
    #     return sort_count
    #
    # # print(f'count {count}')  # count [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #
    # for element in container:
    #     count[element - min_value] += 1
    #
    # # print(f'count {count}')  # count [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
    #
    # for ind, val in enumerate(count):
    #     sort_count.extend([ind + min_value] * val)
    #
    # return sort_count

    # print(sort2([1, 2, 3, 9, 2]))

