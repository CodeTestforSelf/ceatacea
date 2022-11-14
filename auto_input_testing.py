# VScode Extension - Competitive Programming Helper (cph)

# Basic setting & import Libraries
import sys
import re
import datetime

# input = sys.stdin.readline()

# 제출코드 :
import math

def bj_1026():
    N = int(input())
    A = sorted(map(int, input().split()),reverse=True)
    B = sorted(map(int, input().split()),reverse=False)
    result = 0
    for a,b in zip(A,B):
        prod = math.prod([a,b])
        result += prod
    return result

print(bj_1026())