# VScode Extension - Competitive Programming Helper (cph)

# Basic setting & import Libraries
import sys
import re
import datetime

input = sys.stdin.readline()
# 그리디
def ch11_01():
    N = int(input) # (1 <= N <= 100,000) -> O(N) 가능
    X = sorted(map(int, input.split()))
    count, group = 0, 0
    for n in X:
        # count += 1 # 모험가 수
        if n <= N:
            group += 1 # 그룹 수
            count = 0 # 그룹 결성 되었으므로 초기화
    return group


print(ch11_01())