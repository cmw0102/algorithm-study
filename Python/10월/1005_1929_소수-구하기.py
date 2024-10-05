# 1929_소수-구하기

# 문제 분석
# M 이상 N 이하 소수 모두 출력하기

# 해결 과정
# 소수 판별하는 함수를 정의하여 문제를 푼다.

import sys
import math
input = sys.stdin.readline
m, n = map(int, input().split())


def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(m, n+1):
    if is_prime_number(i):
        print(i)

# 결론
# 백준의 4143과 푸는 방식이 유사해서 금방 풀었다.
# 소수 판별은 추후 알고리즘에서 나오는 파트이기 때문에
# 더 열심히 공부해야겠다.
