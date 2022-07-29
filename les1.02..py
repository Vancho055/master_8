seconds = int(input('Введите число больше 3600'))


def zeroes(num):
    if num < 10: num = 0 + num
    return num


def return_hms(second, apply_zeroes):
    sec = second % 60
    min_ = second // 60 % 60
    hrs = second // 3600
    if apply_zeroes > 0:
        sec = zeroes(sec)
        min_ = zeroes(min_)
        if apply_zeroes > 1:
            hrs = zeroes(hrs)
    return "{}:{}:{}".format(hrs, min_, sec)


print(return_hms(seconds, 1))