# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script, hours, money_per_hour, bonus = argv


def calс_salary(hours_, money_per_hour_, bonus_):
    try:
        result = (int(hours_) * float(money_per_hour_)) + float(bonus_)
    except ValueError:
        return
    return result


print(f"{calс_salary(hours, money_per_hour, bonus)}")