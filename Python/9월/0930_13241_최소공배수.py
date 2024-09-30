# 13241_최소공배수

# 문제 분석
# 두 수에 대한 최소공배수 구하기

# 해결 과정
# 첫 번째
# 1934번 문제와 비슷하게 풀면 될 것 같다
# 유클리드 호제법과 최대공약수를 이용한 최소공배수 구하기

import sys
input = sys.stdin.readline
A, B = map(int, input().split())
AA, BB = A, B

while A % B != 0:
    A, B = B, A % B

print(AA * BB // B)

# 결론
# 1934번 문제에서 횟수와 for문을 없에면 정답이다.
# 다시 실전적으로 복습할 수 있어서 좋았다.
