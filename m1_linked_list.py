class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            end = " -> " if current.next else "\n"
            print(current.data, end=end)
            current = current.next

    def reverse(self):
        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next  # Зберегти посилання на наступний вузол
            current_node.next = (
                prev_node  # Змінити напрямок посилання на попередній вузол
            )
            prev_node = current_node  # Переміститися вперед, p стає на поточний вузол
            current_node = next_node  # Переміститися вперед, c стає на наступний вузол

        self.head = (
            prev_node  # Змінити голову списку на останній вузол (який тепер є першим)
        )

    def insertion_sort(self, asc=True):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None  # Ініціалізуємо початок відсортованого списку

        current = self.head

        while current:
            next_node = (
                current.next
            )  # Зберігаємо наступний вузол перед видаленням поточного
            sorted_list = self.sorted_insert(
                sorted_list, current, asc
            )  # Вставляємо поточний вузол у відсортований список
            current = next_node  # Переходимо до наступного вузла

        self.head = sorted_list  # Оновлюємо початок списку

    def sorted_insert(self, sorted_list, new_node, asc=True):
        if (
            sorted_list is None
            or (asc and sorted_list.data >= new_node.data)
            or (not asc and sorted_list.data <= new_node.data)
        ):
            new_node.next = sorted_list
            return new_node

        current = sorted_list
        while current.next and (
            (asc and current.next.data < new_node.data)
            or (not asc and current.next.data > new_node.data)
        ):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_list

    def merge_sorted_lists(self, other_list):
        merged_list = LinkedList()  # Створюємо новий список для об'єднання

        current_self = self.head
        current_other = other_list.head

        while current_self and current_other:
            if current_self.data <= current_other.data:
                merged_list.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged_list.insert_at_end(current_other.data)
                current_other = current_other.next

        # Додавання залишкових елементів з першого списку
        while current_self:
            merged_list.insert_at_end(current_self.data)
            current_self = current_self.next

        # Додавання залишкових елементів з другого списку
        while current_other:
            merged_list.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged_list


if __name__ == "__main__":

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(35)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    # Перевернути зв'язний список
    print("\nРеверсування зв'язного списку:")
    print("оригінал: ", end="")
    llist.print_list()

    print("реверс:   ", end="")
    llist.reverse()
    llist.print_list()

    # Сортування зв'язного списку
    print("\nСортування зв'язного списку:")
    print("оригінал:  ", end="")
    llist.print_list()
    llist.insertion_sort(asc=True)
    print("зростання: ", end="")
    llist.print_list()
    llist.insertion_sort(asc=False)
    print("спадання:  ", end="")
    llist.print_list()

    # Об'єднання двох зв'язних списків
    llist_1 = LinkedList()
    llist_1.insert_at_end(1)
    llist_1.insert_at_end(3)
    llist_1.insert_at_end(5)
    llist_1.insert_at_end(7)

    llist_2 = LinkedList()
    llist_2.insert_at_end(2)
    llist_2.insert_at_end(4)
    llist_2.insert_at_end(6)

    print("\nОб'єднання двох зв'язних списків:")
    print("Список_1: ", end="")
    llist_1.print_list()
    print("Список_2: ", end="")
    llist_2.print_list()
    print("Об'єднаний список: ", end="")
    merged_list = llist_1.merge_sorted_lists(llist_2)
    merged_list.print_list()
