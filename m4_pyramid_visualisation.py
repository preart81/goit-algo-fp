import heapq
import uuid
import copy

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

    def count_nodes(self):
        count = 1
        if self.left:
            count += self.left.count_nodes()
        if self.right:
            count += self.right.count_nodes()
        return count

    def __str__(self, level=0, prefix="Root: ") -> str:
        """
        Візуалізація дерева

        Параметри:
            level: початковий рівень дерева
            prefix: префікс, дефолт = 'Root: '

        Повертає:
            ret: багаторядкова текстова візуалізація дерева
        """

        ret = "\t" * level + prefix + str(self.val) + "\n"

        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")

        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")

        return ret


def add_edges(graph: nx.DiGraph, node: Node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            x_left = x - 1 / 2**layer
            pos[node.left.id] = (x_left, y - 1)
            add_edges(graph, node.left, pos, x=x_left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            x_right = x + 1 / 2**layer
            pos[node.right.id] = (x_right, y - 1)
            add_edges(graph, node.right, pos, x=x_right, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root: Node, title="Візуалізація дерева"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(graph=tree, node=tree_root, pos=pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]

    # Використовуйте значення вузла для міток
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    # plt.title(title, y=1.05, color="darkblue")
    plt.gcf().canvas.manager.set_window_title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def heap_to_tree(heap, level=0) -> Node:
    """Перетворення купи в дерево

    Парамтери:
        heap (list): купа
        level (int): початковий рівень вузла, default 0

    Повертає:
        (Node): дерево

    """
    if level >= len(heap):
        return None

    root = Node(heap[level])
    root.left = heap_to_tree(heap, level=(2 * level + 1))
    root.right = heap_to_tree(heap, level=(2 * level + 2))

    return root


def draw_heap(heap: heapq, title="Візуалізація купи") -> None:
    """Візуалізація купи"""

    root = heap_to_tree(heap)
    draw_tree(root, title=title)


def get_lighten_color(color_hex: str = "#1296F0", step: int = 2) -> str:
    """Отримання світлішого відтінку кольору

    Параметри:
        color_hex (str): шістнадцятковий код кольору
        step (int): крок зміни кольору
    Повертає
        (str): шістнадцятковий код світлішого відтінку кольору

    """
    # Перетворення шестнадцяткового кольору у RGB формат
    red = int(color_hex[1:3], 16)
    green = int(color_hex[3:5], 16)
    blue = int(color_hex[5:7], 16)

    # Збільшення значення кожного кольору на крок для світлішого відтінку
    red = min(255, red + step)
    green = min(255, green + step)
    blue = min(255, blue + step)

    # Формування нового кольору у вигляді шестнадцяткового коду
    new_color_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)
    return new_color_hex


if __name__ == "__main__":
    # Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення дерева
    # draw_tree(root)

    # Візуалізауція купи
    heap = [15, 10, 20, 8, 12, 16, 25]
    # print(f"list {heap = }")
    heapq.heapify(heap)
    print(f"{heap = }")

    draw_heap(heap, title="Візуалізація купи")
