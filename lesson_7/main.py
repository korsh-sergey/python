# Виды ошибок

# ZeroDivisionError: division by zero
# x = 15/0

# TypeError
# x = 15 + "а"

# IndexError: list index out of range
# lst = [10, 5, 3]
# print(lst[3])

#SyntaxError
# if 5 > 0

# ValueError
# x = int("А")

# Коды завершения
# 0 - всё хорошо
# 1 - ошибка
# -1 - прерывание


# assert
# def summa(number: list[int]):
#     return sum(number)
#
# assert summa([1,3]) == 4  # ошибки не будет
# assert summa([1,3]) == 5  # ошибка

try:
    x = 5/0
except ZeroDivisionError:
    print("На ноль делить низя")

# try - попытаться
# except - ожидать ошибки

