"""Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і
побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.

"""

import random
import matplotlib.pyplot as plt

# к-сть кидків кубиків
n = 1000_000
# n = 100

#  словник для зберігання результатів
results = {i: 0 for i in range(2, 13)}

# побудова таблиці сум та імовірностей за допомогою методу Монте-Карло
for _ in range(n):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    results[dice1 + dice2] += 1

# обрахунок ймовірностей
probability = {sum_val: count / n for sum_val, count in results.items()}


# --- аналітичний розрахунок ймовірностей ---

# Створення словника для зберігання кількості способів отримання кожної суми
outcomes = {i: 0 for i in range(2, 13)}

# Обчислення кількості способів для кожної суми
for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        total = dice1 + dice2
        outcomes[total] += 1

total_outcomes = sum(outcomes.values())

# --- аналітичний розрахунок ймовірностей ---


# виводимо таблицю ймовірнстей
print("Сума | Монте-Карло | Аналітичний | Розбіжність")
print("----------------------------------------------")
for sum_val, count in results.items():
    print(
        f"{sum_val:2d}   | {count/n:>10.2%}  | {outcomes[sum_val]/total_outcomes:>10.2%} | {count/n - outcomes[sum_val]/total_outcomes:>10.2%}"
    )
print()

# візуалізація результатів
plt.bar(probability.keys(), probability.values())
plt.xlabel("Сума значень кубиків")
plt.ylabel("Ймовірність")
plt.title("Ймовірності сум при киданні 2х кубиків")
plt.show()
