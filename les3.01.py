# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func (a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "b is'n be a zero"
    except ValueError:
        return "enter only number"
print(my_func(int(input("Enter a = ")), int(input("Enter b = "))))