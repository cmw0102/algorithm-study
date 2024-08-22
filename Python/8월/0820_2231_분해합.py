# 2231_분해합
M = int(input())  # 분해합 입력 받기
min_constructor = float('inf')  # 최소값의 생성자를 최대 크기의 숫자로 초기화

for i in range(1, M):
    nameoji = M - i  # nameoji: 분해합 - 생성자
    jali = 0
    j = i

    for k in range(len(str(i))):  # 자리수를 구하기 위함
        jali += j % 10
        j //= 10
    if nameoji == jali:  # 분해합 - 생성자 == 자리수의 합이 같고
        if i < min_constructor:  # i(생성자)의 값이 최소가 될 때
            min_constructor = i  # i의 값은 최소 생성자가 됨
if min_constructor == float('inf'):
    print(0)
else:
    print(min_constructor)
