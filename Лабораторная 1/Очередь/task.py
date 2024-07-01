"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        C лево начало, с право конец очереди
        """
        self._list = list()  # инициализировать список

    def enqueue(self, elem: Any) -> None:  # O(1)
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._list.append(elem)  # реализовать метод enqueue

    def dequeue(self) -> Any:  # O(N)
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self._list) == 0:
            raise IndexError("Очередь пуста")

        return self._list.pop(0)  # реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: Индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        low = 0
        # high = len(self._list) - 1

        if not isinstance(ind, int):
            raise TypeError("Указан не целочисленный тип данных")

        if not 0 <= ind < len(self._list):
            raise IndexError(f"Указанный индекс: {ind} вне границ очереди")

        return self._list[ind]
        #  реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self._list.clear()  # реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._list)  # реализовать метод __len__
