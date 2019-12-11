#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:28:53 2019

@author: jeanwang
"""
f
import math
import statistics

score = [int(i) for i in input().split(',')]

print('Mean: '+ str(statistics.mean(score)))
print('Median: ' + str(statistics.median(score)))
print('Standard Deviation: ' + str(statistics.stdev(score)))


def calculate(a, b):
    if a == 1:
        result = math.log2(b)
        return result
    if a == 2:
        result = math.log(b)
        return result
    if a == 3:
        result = b ** 2.0
        return result

type_of_input =int(input())
enter_number = int(input())

print(calculate(type_of_input, enter_number))


def fa_s(n):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        result_1 = fa_s(n - 2) + fa_s(n -1)
    return result_1

a = int(input('Enter a number to calculate:'))
print(fa_s(a))
