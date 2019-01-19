#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


def should_stop(big_number, n):
    for i in range(n):
        if big_number[i] == 9:
            continue
        else:
            return False
    return True


def print_number(big_number):
    start_print = False
    for i in range(len(big_number)):
        if start_print:
            print(big_number[i], end='')
        else:
            if big_number[i] != 0:
                start_print = True
                print(big_number[i], end='')

    print()


def solve(n):
    if n <=0:
        return
    big_number = [0] * n
    while not should_stop(big_number, n):
        for i in range(-1, -n - 1, -1):
            temp = big_number[i]
            temp += 1
            big_number[i] = temp % 10
            carry = temp // 10
            if not carry:
                break
        print_number(big_number)


if __name__ == '__main__':
    solve(0)
    solve(-1)
