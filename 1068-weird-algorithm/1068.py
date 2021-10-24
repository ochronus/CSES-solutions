# -*- coding: utf-8 -*-
import sys


def gen_next_value(value):
    if (value % 2) == 0:
        return value // 2
    else:
        return value * 3 + 1


def run_algo(n):
    values = []
    while n != 1:
        values.append(str(n))
        n = gen_next_value(n)
    values.append("1")
    print(" ".join(values))


n = int(input())
run_algo(n)
