#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = num * -1
    last_num = num % 10

    print('{}'.format(last_num), end='')
    return last_num
