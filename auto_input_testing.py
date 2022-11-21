# VScode Extension - Competitive Programming Helper (cph)

# Basic setting & import Libraries
import sys
import re
import datetime

# input = sys.stdin.readline()

# 제출코드 :

def bj_2839():
    sugar = int(input())
    bags = [5, 3]
    result = 0
    for b in bags:
        print(f'start -- b : {b} / result : {result} / sugar : {sugar}')
        result += sugar // b
        print(f'result += sugar // b --> b : {b} / result : {result} / sugar : {sugar}')
        sugar %= b
        print(f'sugar %= b --> b : {b} / result : {result} / sugar : {sugar}')

    return -1 if sugar != 0 else result

print(bj_2839())