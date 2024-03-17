import copy
import heapq
from m4_pyramid_visualisation import Node, get_lighten_color, draw_tree, heap_to_tree


def bfs_tree(
    root: Node, color: str = "#1296F0", title: str = "Візуалізація BFS"
) -> None:
    """Візуалізація обхода дерева в ширину (BFS).

    Кожен крок відображається іншим відтінком кольору.

    """

    root = copy.deepcopy(root)
    queue = [root]
    color_step = 220 // root.count_nodes()
    print("BFS: ", end="")
    while queue:
        node = queue.pop(0)
        node.color = color
        color = get_lighten_color(color, color_step)
        print(node.val, end=", ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()
    draw_tree(root, title=title)


def dfs_tree(
    root: Node, color: str = "#1296F0", title: str = "Візуалізація DFS"
) -> None:
    """Візуалізація обхода дерева в глибину (DFS).

    Кожен крок відображається іншим відтінком кольору.

    """

    root = copy.deepcopy(root)
    stack = [root]
    color_step = 220 // root.count_nodes()
    print("DFS: ", end="")
    while stack:
        node = stack.pop()
        node.color = color
        color = get_lighten_color(color, color_step)
        print(node.val, end=", ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print()
    draw_tree(root, title=title)


if __name__ == "__main__":
    heap = [15, 10, 20, 8, 12, 16, 25, 30, 35, 40, 45, 50, 55]
    heapq.heapify(heap)
    tree = heap_to_tree(heap)
    print()
    print(tree)

    bfs_tree(tree, title="Візуалізація обхода дерева в ширину (BFS)")
    dfs_tree(tree, title="Візуалізація обхода дерева в глибину (DFS)")
