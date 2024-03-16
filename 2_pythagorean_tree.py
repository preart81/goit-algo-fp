"""
Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення
фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево
Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії."""

import turtle


def pifagor_tree(t: turtle.Turtle, branch_len: int, level: int):
    """
    Функція рекурсії для створення дерева Піфагора

    :param t: turtle.Turtle
    :param branch_len: int
    :param level: int
    :return: None
    """

    def level_config(t: turtle.Turtle, level: int):
        """
        Налаштування гілок в залежнотсі від рівня:
        імітує стовбур, гілки і листя
        level = 0 - зелена;
        level = 1 - коричнева;
        """
        if level > 1:
            t.color("brown")
            t.width(level)
        else:
            t.color("green")
            t.width(8)

    if level > 0:
        # коефіцієнт зменшення дочірніх гілок
        k = 0.75
        # налаштування гілок для level
        level_config(t, level)

        t.forward(branch_len)
        t.right(45)
        pifagor_tree(t, branch_len * k, level - 1)
        t.left(90)
        pifagor_tree(t, branch_len * k, level - 1)
        t.right(45)

        # налаштування гілок для level
        level_config(t, level)

        t.backward(branch_len)


def draw_pifagor_tree(branch_len: int = 75):
    t = turtle.Turtle()
    window = turtle.Screen()
    window.title("Дерево Піфагора")
    window.setup(500, 400)
    window.bgcolor("white")

    level = window.textinput("Налаштування", "Введіть рівень рекурсії:")
    try:
        level = int(level)
    except:
        level = 6

    turtle_form = ["arrow", "turtle", "circle", "square", "triangle", "classic"][2]
    t.shape(turtle_form)
    t.shapesize(0.3)
    # t.hideturtle()
    t.color("#002184")
    t.width(2)

    t.speed(0)
    t.up()
    t.left(90)
    t.backward(100)
    t.down()

    pifagor_tree(t, branch_len, level)
    window.exitonclick()


if __name__ == "__main__":
    draw_pifagor_tree()
