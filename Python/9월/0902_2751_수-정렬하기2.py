# 2751_수-정렬하기2

# 문제 분석
# N개의 수가 주어졌을 때, 오름차순으로 정렬하는 프로그램 만들기
# 첫 째줄에는 몇개의 정수를 입력할 지 작성
# 둘 째줄부터 한 줄에 하나씩 정수 입력

# 해결 과정
# 첫 번째 - 삽입 정렬로 풀기 (시간 초과)

import sys
input = sys.stdin.readline
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

for i in range(1, n):  # 여기서 시간 초과가 난 것 같음
    for j in range(i, 0, -1):
        if n_list[j] < n_list[j-1]:
            n_list[j], n_list[j-1] = n_list[j-1], n_list[j]

for i in range(n):
    print(n_list[i])

# 두 번째 - 찾아본 결과 파이썬 내장 함수를 이용하는 방법이 있어서 내장 함수를 이용해 보기로 하였음.

# import sys
input = sys.stdin.readline
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()   # sort() 함수를 사용하면 오름차순으로 정렬됨
# 내림차순 정렬시 sort(reverse=False)를 사용하면 됨

for i in range(n):
    print(n_list[i])


# ++ 추가로 찾아본 결과
# 파이썬에는 리스트 컴프리헨션이라는 코드를 간편화 시킨 후 한 줄로 작성하는 코드가 있어서 공부하기 위해 작성

n_list = []
for _ in range(n):
    n_list.append(int(input()))

# 위 코드를 리스트 컴프리헨션으로 치환하면
n_list = [int(input()) for _ in range(n)]
# 이렇게 표현 가능
# 즉, for ~ in ~ 을 실행 하는 동안 for문 앞에 있는
# int(input()) 행동을 실행하라는 것이다.

# 결론
# 낮은 난이도의 문제의 경우 시간을 넉넉하게 주는 것 같은데
# 점점 난이도가 올라갈수록 코드를 실행시키는 시간이 줄어드는 것 같다
# 코드의 간결함, 시간 복잡도 최소화를 지향하면서 문제를 풀어야겠다.
