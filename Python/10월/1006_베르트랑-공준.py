# 4948_베르트랑-공준

# 문제 분석
# 임의의 수 n이 주어졌을 때 n과 2n 사이에는 소수가 적어도 하나는 존재한다.
# 이러한 명제를 통해 자연수 n이 주어졌을 때 n과 2n 사이의 소수를 구하기

# 해결 과정
# 첫 번째 - 실패 (제한 조건을 보지 못했음)
# 소수 판별 함수를 만들어 값을 구한다.

import sys
import math
input = sys.stdin.readline


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n_list = list(map(int, input().split()))
count = 0
for i in n_list:
    for j in range(i + 1, (i * 2) + 1):
        if is_prime_number(j):
            count += 1

print(count)


# 두 번째 - 제한 추가
# 제한된 숫자 내에 있는 소수를 찾고 따로 저장한 다음
# 입력된 숫자를 통한 범위값 안에 도출해낸 소수가 있다면 카운트 하는 방식으로 진행한다.
# import sys
# import math
input = sys.stdin.readline


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


limt_list = list(range(2, 123456 * 2 + 1))
sosu_list = []
for i in limt_list:
    if is_prime_number(i):
        sosu_list.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in sosu_list:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())

# 결론
# 응용하는게 생각보다 어려웠다.
# 특히 제한 조건을 거는게 쉬우면서도 어려웠다.
