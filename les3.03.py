# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    if (x + y) > (x + z) and (x + y) > (y + z):
        return x + y
    if (x + z) > (x + y) and (x + z) > (y + z):
        return x + z
    if (y + z) > (x + y) and (y + z) > (x + z):
        return y + z

try:
    n1 = int(input("x = "))
    n2 = int(input("y = "))
    n3 = int(input("z = "))
    print(f"сумма наибольших двух элементов:  {my_func(n1, n2, n3)}")
except ValueError as e:
    print(f"{e}")