# 19532_수학은-비대면강의입니다
a, b, c, d, e, f = map(int, input().split())  # 계수 입력 받기

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x) + (b * y) == c and (d * x) + (e * y) == f:  # 조건이 성립해야함
            print(x, y)
            break
