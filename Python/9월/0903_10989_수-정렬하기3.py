# 10989_수-정렬하기3

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# 메모리 아끼는 거 어렵다...
# 출처: https://yoonsang-it.tistory.com/49
