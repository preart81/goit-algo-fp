"""
Програму використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
"""

# Словник з вартістю та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Жадібний алгоритм
def greedy_algorithm(items: dict, budget: int) -> tuple:
    """
    Вибір страв з найбільшою сумарною калорійністю в межах бюджету.

    Параметри:
        items: словник з вартістю та калорійністю страв
        budget: бюджет
    Повертає кортеж:
        max_items: список страв з найбільшою сумарною калорійністю
        total_calories: сумарна калорійність
        total_cost: сумарна вартість

    """
    # страви відсортовані за співвідношенням вартість/калорійність
    items_sorted = sorted(
        items, key=lambda x: items[x]["cost"] / items[x]["calories"], reverse=True
    )
    max_items = []
    total_cost = 0
    total_calories = 0
    for item in items_sorted:
        if total_cost + items[item]["cost"] <= budget:
            total_cost += items[item]["cost"]
            total_calories += items[item]["calories"]
            max_items.append(item)
    return max_items, total_calories, total_cost


# Алгоритм динамічного програмування
def dynamic_programming(items: dict, budget: int) -> tuple:
    """
    Вибір страв з найбільшою сумарною калорійністю в межах бюджету.

    Параметри:
        items: словник з вартістю та калорійністю страв
        budget: бюджет
    Повертає кортеж:
        selected_items: список обраних страв
        total_calories: сумарна калорійність
        total_cost: сумарна вартість

    """
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            item_cost = items[list(items.keys())[i - 1]]["cost"]
            item_calories = items[list(items.keys())[i - 1]]["calories"]
            if item_cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_cost] + item_calories)
            else:
                dp[i][j] = dp[i - 1][j]

    # список обраних страв
    selected_items = []
    i = n
    j = budget
    total_cost = 0
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(
                # (
                list(items.keys())[i - 1],
                # items[list(items.keys())[i - 1]]["calories"],
                # )
            )
            total_cost += items[list(items.keys())[i - 1]]["cost"]
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return selected_items, dp[n][budget], total_cost


if __name__ == "__main__":
    BUDGET = 90
    print(f"Вибір страв з найбільшою сумарною калорійністю для бюджету: {BUDGET}₴:")
    print("Жадібний алгоритм:")
    greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget=BUDGET)
    print(
        f"-страви: {greedy_items}\n"
        f"-сумарна калорійність: {greedy_calories}\n"
        f"-сумарна вартість: {greedy_cost}₴"
    )
    print()

    print("Динамічний алгоритм:")
    dynamic_items, dynamic_calories, dynamic_cost = dynamic_programming(
        items, budget=BUDGET
    )
    print(
        f"-страви: {dynamic_items}\n"
        f"-сумарна калорійність: {dynamic_calories}\n"
        f"-сумарна вартість: {dynamic_cost}₴"
    )
    print()
