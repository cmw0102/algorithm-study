# 2485_가로수

# 문제 분석
# 여러 수가 주어지고 여러수 사이의 규칙(간격)을 찾아 해당하는 최소의 수를 출력

# 해결 과정
# 첫 번째 - 시간 초과...
# 약간의 노다가성 가미
# step1: 입력 받은 수가 a b c d 이렇게 있으면 d - c, c -b, b - a 이렇게 해서 그 차가 가장 작은 수를 구한다.
# step2: step1에서 입력 받은 값 중 가장 작은 값부터 step1에서 구한 값을 가장 큰 값까지 몇개가 필요한지 구한다.(단, 중복값은 제외해야 하므로 if문을 통해 중복값 제거)
import math
import sys
input = sys.stdin.readline

n = int(input())
n_list = []  # 현재 알 수 있는 수
n_list2 = []  # n_list에서 차를 구한 수 정리
count = 0

for i in range(n):
    n_list.append(int(input()))

n_min = min(n_list)  # 입력 받은 수 중 가장 작은값(규칙의 첫 시작 값)

# step1
for i in range(1, n):
    n_list2.append(n_list[i] - n_list[i-1])

n_min2 = min(n_list2)  # 차의 최소값 (안되면 sort정렬 써서 바꾸기)

# step2
for i in range(max(n_list) // n_min2):
    n_min = n_min + n_min2
    if n_min not in n_list:
        count += 1

print(count)


# 두 번째 - 성공
# for i in range(max(n_list) // n_min2): 이부분에서 시간을 많이 잡아 먹는 것 같다.
# import sys
input = sys.stdin.readline

n = int(input())
n_list = []  # 현재 알 수 있는 수
n_list2 = []  # n_list에서 차를 구한 수 정리
count = 0

for i in range(n):
    n_list.append(int(input()))

n_list.sort()  # 정렬

# step1: 각 수들 사이의 차이를 구해서 리스트에 저장
for i in range(1, n):
    n_list2.append(n_list[i] - n_list[i - 1])

# step2: 차이들의 최대 공약수(GCD)를 구함
gcd_value = n_list2[0]
for i in range(1, len(n_list2)):
    gcd_value = math.gcd(gcd_value, n_list2[i])

# step3: 주어진 수들 사이에 몇 개의 수가 더 있어야 하는지 계산
min_value = n_list[0]
max_value = n_list[-1]  # 마지막 요소 불러오기
total_count = (max_value - min_value) // gcd_value + 1

# 추가해야 하는 수의 개수는 전체 개수에서 현재 있는 개수를 뺀 값
count = total_count - n

print(count)

# 결론
# 시간을 어떻게 줄여야할지 고민을 해야겠다.
# 또, 최소 차이값은 최대 공약수에 비해 나머지 값들 간의 차이가 일정하지 않는 문제가 발생할 수 있기 때문에 최대공약수로 구해야한다...

# ++추가 공부
# math.gcd(a, b) -> 두 수 a, b의 최대공약수를 계산
