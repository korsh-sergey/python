
# print(number=random.randint(0,100))
# print(r.randint(0,100))

# from random import randint
# print(randint(0,100))

# from random import *
# print(randint(0,100))
# import random as r
# spisok = [1,2,3,4,5]
# print(r.choice(spisok))
# r.shuffle(spisok)
# print(spisok)


# import turtle
# screen = turtle.Screen()
# t = turtle.Turtle()
# horisontal = 200
# vertical=100
# t.color("green","yellow")
# t.pensize(10)
# t.speed(5)
#
#
# t.begin_fill()
# t.forward(horisontal)
# t.right(90)
# t.fd(vertical)
# t.right(90)
# t.fd(horisontal)
# t.right(90)
# t.fd(vertical)
# t.right(90)
# t.end_fill()
#
# t.penup()
# t.goto(120,-30)
# t.pendown()
# t.forward(50)
# t.circle(50)
# t.color("blue")
# t.write("Movavi",font=("Arial Black",50,"normal"),align="center")

# screen.exitonclick()

# import random
# import time
# xacked = 0
# while xacked < 100:
#     xacked=xacked+random.randint(0,10)
#     if xacked >= 100:
#         print("Прогресс 100%")
#         time.sleep(1)
#     else:
#         print(f"{xacked}%")
#         time.sleep(1)
#
# import random
#
# list =["1","2","3"]
# quess = input("Ball 1,2,3")
# answer = random.choice(list)
# if quess == answer:
#     print("Ypppppppa")
# else:
#     print("Нет он был в",answer)

# import turtle
# import random
# screen = turtle.Screen()
# t=turtle.Turtle()
# side=(100)
# t.speed(0)
# t.pensize(6)
#
# colors = ["red","blue","pink","green","black"]
# i = int(input("сколько углов"))
# for j in range (0,i):
#     t.color(random.choice(colors))
#     t.fd(side)
#     t.rt(360/i)
#
#
# screen.exitonclick()

import time
import random
isgame = True
print("Время пострелять")
while isgame:
    patron =random.choice([1,2,3,4,5,6])
    our = random.choice([1,2,3,4,5,6])
    print("Заряжанм револьвер")
    time.sleep(3)
    print("Крутим барабан")
    time.sleep(1)
    print("Выстрел через")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    if patron == our:
        print("Смерть 💀💀")
    else:
        print("Не cмерть 😍")
        if (input("Играем ли дальше?") == "нет"):
            isgame = False
        else:
            pass

