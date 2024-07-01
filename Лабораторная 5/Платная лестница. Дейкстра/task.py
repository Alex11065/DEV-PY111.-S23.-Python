from typing import Union

import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    #  c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    return nx.dijkstra_path_length(graph, 0, len(graph.nodes) - 1)


def create_stairway_graph(costs):
    graph = nx.DiGraph()
    n = len(costs)

    # Добавляем ребра для переходов на следующую ступень и через одну
    for i in range(n):
        if i + 1 < n:
            graph.add_edge(i, i + 1, weight=costs[i + 1])
        if i + 2 < n:
            graph.add_edge(i, i + 2, weight=costs[i + 2])

    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = create_stairway_graph(
        stairway)  # записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
