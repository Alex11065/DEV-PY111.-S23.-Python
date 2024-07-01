"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    #  реализовать итеративный линейный поиск
    if len(arr) == 0:
        raise ValueError("Массив пустой")
    min_value = arr[0]  # выбираем значение под индексом 0 для сравнения
    min_index = 0  # ставил None и не проходило тест если на 0 индексе стояло сразу минимальное значение, а с 0 все сработало
    for index, value in enumerate(arr):
        if arr[index] < min_value:
            min_value = value
            min_index = index
    return min_index


if __name__ == "__main__":
    pass
# Другой вариант
#     def min_(lst):
#         if len(lst) == 0:
#             raise ValueError
#
#         min_v = lst[0]
#         min_ind = 0
#         for i in range(len(lst)):
#             if lst[i] < min_v:
#                 min_v = lst[i]
#                 min_ind = i
#         return f"Минимальное значение {min_v} -- индекс {min_ind}"
#
# print(min_([2, 3, 4, 5, 6, 1]))
# print(min_([0, 2, 3, 4, 5, 6, 1]))
