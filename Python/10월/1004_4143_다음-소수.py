# 4143_다음-소수

# 문제 분석
# 임의의 정수 n보다 크거나 같은 소수 중 가장 작은 소수 찾기

# 해결 과정
# 첫 번째
# 입력 받은 수 부터 소수인지 차례대로 검사
# 먼저 소수 판별 함수를 정의 하여 이용하기로 했다.
# 그 후 for문과 while을 활용하여 소수 판별 시 소수면 출력 리스트에 추가 / 그렇지 않다면 +1하여 다시 계산토록 했다.

import sys
import math
input = sys.stdin.readline


def is_prime_number(x):  # 소수 판별 함수
    if x < 2:  # 2보다 작을 경우 소수가 아니다.
        return False
    for i in range(2, int(math.sqrt(x)) + 1):  # x의 제곱근 구하기
        if x % i == 0:
            return False
    return True


n = int(input())
n_list = []
n_list2 = []
for i in range(n):
    n_list.append(int(input()))

for i in n_list:
    if is_prime_number(i) != True:
        while not is_prime_number(i):
            i += 1
    n_list2.append(i)

for i in n_list2:
    print(i)

# 결론
# 소수 판별하는 함수를 만드는데 생각보다 시간이 오래걸렸다..
# 구글링은 신이야..
