# 1735_분수-합

# 문제 분석
# 분자 분모를 두 번 입력하여 기약분수(더 이상 약분되지 않는 분수)를 구하여 출력하기

# 해결 과정
# 첫 번째
# step1: 분모는 분모끼리 곱하고 분자는 분자와 분모를 곱한 값을 더한다.
# step2: 구한 분자와 분모의 최대공약수를 유클리드 호제법을 이용하여 구한다.
# step3: 구한 최대공약수 값을 다시 전에 구했던 분자와 분모값에 나누기 연산자를 통해 나누어 구한다.

import sys
input = sys.stdin.readline

# step1 (분자, 분모 순)
A, B = map(int, input().split())
C, D = map(int, input().split())

AC = A * D + B * C  # 분자
ACU = AC  # 분자 원본
BD = B * D  # 분모
BDU = BD  # 분모 원본

# step2 (유클리드 호제법 사용)
while BD % AC != 0:
    BD, AC = AC, BD % AC  # 이제 AC가 최대 공약수가 됨

# step3 (ACU, BDU를 AC로 몫나누기(정수형으로 출력) 하여 출력하면 됨)
print(ACU // AC, BDU // AC)

# 결론
# 유클리드 호제법으로 쉽게 풀었다.
# 전에 풀었던 최소공배수문제의 응용 격으로 느껴졌다.
