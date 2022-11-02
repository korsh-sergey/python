# import aditional
# import random
# print(aditional.logo)
# score=0
# is_game = True
# data=aditional.data
#
# while is_game == True:
#     a = random.choice(data)
#     b = random.choice(data)
#     while a == b:
#         b=random.choice(data)
#     print("Твой счёт - ",score)
#     print("-"*10)
#     print(f"А:{a['name']}.{a['description']}.{a['country']}")
#     print(aditional.vs)
#     print(f"В:{b['name']}.{b['description']}.{b['country']}")
#     select = input ("У кого больше подписоты?(A,B)").upper().strip()
#     if select == "МЕНЯЙ":
#         continue
#     if select == "A" or select == "B":
#         if a['follower_count'] > b['follower_count'] and select =="A":
#             score = score + 1
#             print("Правильно")
#         elif a['follower_count'] < b['follower_count'] and select =="B":
#             score = score + 1
#             print("Правильно")
#         else:
#             print("Одна ошибка и ты ошибся ")
#             is_game = False
#     else:
#         print("Я обиделся 😭😭😭😭😭")
#         break