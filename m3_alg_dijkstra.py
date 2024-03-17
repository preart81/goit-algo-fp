"""
Алгоритм Дейкстри 

Алгоритм Дейкстри — це алгоритм пошуку найкоротшого шляху у графі з невід'ємними
вагами ребер від однієї вершини до всіх інших."""

import heapq
import matplotlib.pyplot as plt
import networkx as nx


def dijkstra(graph, start_vertex, end_vertex=None) -> dict:
    """Алгоритм Дейкстри

    Параметри:
        graph: dict - граф;
        start_vertex - початкова вершина;
        end_vertex - кінцева вершина.
    Повертає dict:
        distances:dict|int - відстані від початкової до всіх вершин, або відстань до заданої end_vertex.;
        path:list - оптимальний шлях якщо задана end_vertex або None.

    """
    # Ініціалізація відстаней і списку попередніх вершин
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start_vertex] = 0
    previous_vertices = {vertex: None for vertex in graph}

    # Пріоритетна черга для зберігання вершин і відстаней
    priority_queue = [(0, start_vertex)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо в списку вже є коротший шлях - ігноруємо цю вершину
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань і попередню вершину
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    # Якщо вказана кінцева вершина, будуємо оптимальний шлях
    if end_vertex:
        path = []
        current_vertex = end_vertex
        while previous_vertices[current_vertex] is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.insert(0, start_vertex)
        return {"distance": distances[end_vertex], "path": path}
    else:
        # return {"distance": distances, "path": previous_vertices}
        return {"distance": distances, "path": None}


def to_digraph(graph: dict) -> nx.DiGraph:
    """Перетворення графа в направлений nx.DiGraph

    Параметри:
        graph: dict - граф в вигляді словника з вагою ребер.;
        напр.: {'A': {'B': 5, 'C': 10}, 'B': {'A': 5, 'D': 3}, 'C': {'A': 10, 'D': 2}, 'D': {'B': 3, 'E': 4}, 'E': {'D': 4}}.

    """
    di_graph = nx.DiGraph()

    # Додавання ребер та ваг
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            di_graph.add_edge(node, neighbor, weight=weight)
    return di_graph


def graph_show(G: nx.DiGraph) -> None:
    """Візуалізація графа

    Візуалізація графа з вагами ребер. Використовуємо бібліотеку networkx.
    Довжини ребер пропорційні їх вазі.
    """
    plt.figure(figsize=(8, 6))

    # Позиціонування вузлів і зврахуванням відстані (ваги ребер)
    pos = nx.kamada_kawai_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1500,
        node_color="skyblue",
        font_size=12,
        font_weight="bold",
    )
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color="red", font_size=10
    )
    title = "Візуалізація графа"
    plt.gcf().canvas.manager.set_window_title(title)
    # plt.axis("off")  # Вимкнення відображення координатної осі
    plt.show()


if __name__ == "__main__":
    # Приклад графа у вигляді словника
    graph = {
        "A": {"B": 5, "C": 10},
        "B": {"A": 5, "D": 3},
        "C": {"A": 10, "D": 2},
        # "D": {"B": 3, "C": 2, "E": 4},
        "D": {"B": 3, "E": 4},
        "E": {"D": 4},
    }

    print("Граф:")
    print(f"{graph}")

    # Задаємо початкову вершину
    start_node = "A"
    # та прелік вершин, до яких визначаємо маршрути
    end_nodes = filter(lambda x: x != start_node, graph.keys())

    print()
    print(f"Найкоротші шляхи від початкової вершини {start_node} до всіх вершин:")
    for end_node in end_nodes:
        print(
            f"{start_node} -> {end_node}: {dijkstra(graph, start_node, end_node)['distance']:3}, маршрут: {dijkstra(graph, start_node, end_node)['path']}"
        )

    print()

    # Ініціалізація направленого графа
    G = to_digraph(graph)

    # Візуалізація графа
    graph_show(G)
