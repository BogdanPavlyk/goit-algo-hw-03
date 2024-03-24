import turtle

def koch_snowflake(turtle, iterations, length):
    """
    Малює сніжинку Коха.

    :param turtle: Turtle object, який використовується для малювання.
    :param iterations: Рівень рекурсії.
    :param length: Довжина лінії.
    """
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, iterations-1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations-1, length)
        turtle.right(120)
        koch_snowflake(turtle, iterations-1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations-1, length)

def main():
    # Вікно для малювання
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Створення turtle для малювання
    koch_turtle = turtle.Turtle()
    koch_turtle.speed(0)  # Найвища швидкість

    # Встановлення початкової позиції
    koch_turtle.penup()
    koch_turtle.goto(-150, 90)
    koch_turtle.pendown()
    
    # Встановлення рівня рекурсії
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Малювання сніжинки Коха
    for i in range(3):
        koch_snowflake(koch_turtle, level, 300)
        koch_turtle.right(120)

    # Завершення
    window.mainloop()

if __name__ == "__main__":
    main()
