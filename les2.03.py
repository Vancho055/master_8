#  Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#  Напишите решения через list и dict.

n =int(input('Введите число месяца'))
if n <= 12 and n >= 1:
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]
    month_num = n
    if month_num in range(1, 13):
        for i, el in enumerate(month_list):
            if month_num in el[1:4]:
                print(f'Введенный номер месяца относится к сезону {el[0]}')
                break
else:
    print('Введен некорректный номер месяца!')
