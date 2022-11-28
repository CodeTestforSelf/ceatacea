# VScode Extension - Competitive Programming Helper (cph)

# Basic setting & import Libraries
import sys
import re
import datetime

# input = sys.stdin.readline()

# 제출코드 :
def fun4_3 () :
	# input -> a1 일 때, col = a, row 1
	# ord(str) -> 유니코드 정수를 반환
	# a : 97 ~ h : 104 -> 8 * 8 안에서 해야 하므로 97에서 빼고 +1 해서 1~8 만들어야 함
	position = input()
	col = int(ord(position[0])) - int(ord('a')) + 1
	row = int(position[1]) # str -> int
	# 경우의 수로서 가능성들
	moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
	count = 0 # 경우의 수 카운팅
	for m in moves:
		cols = col + int(m[0])
		rows = row + int(m[1])
		if (1 <= cols <= 8) and (1 <= rows <= 8):
		# 범위 벗어나지 않을 때만
			count += 1

	return count


print(fun4_3())
