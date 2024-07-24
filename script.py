print("Py is working")
import turtle
import random

# Создаем две черепахи
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Задаем начальные позиции для первых двух черепах
t1.penup()
t1.goto(-200, 0)
t1.pendown()

t2.penup()
t2.goto(200, 0)
t2.pendown()

# Функция для управления движением черепахи
def move_turtle(t):
    t.forward(random.randint(1, 50))
    t.left(random.randint(0, 360))

# Создаем ещё одну черепаху
t3 = turtle.Turtle()

# Задаем начальную позицию для третьей черепахи
t3.penup()
t3.goto(0, 200)
t3.pendown()

# Цикл для сражения точками и создания новой черепахи
for _ in range(1000):
    move_turtle(t1)
    move_turtle(t2)
    move_turtle(t3)

# Закрыть окно после завершения
turtle.done()
