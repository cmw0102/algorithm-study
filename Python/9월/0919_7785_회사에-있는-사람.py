# 7785_회사에-있는-사람

# 문제 분석
# 출퇴근 로그를 통해 현재 회사에 있는지 여부를 구하는 문제이다.
# enter인 경우 출근, leave인 경우 퇴근

# 해결 과정
# 첫 번째 - 실패
# 입력받은 이름을 변수에 담아 set구성
# leave가 있는 이름은 저 set에서 제거
# 맨처름 만든 set에 있는 이름 출력

import sys
input = sys.stdin.readline
n = int(input())
n_list = []
n_set = set()

for i in range(n):
    name, company = input().split()
    n_set.add(name)
    n_list.append([name, company])

for i in range(n):
    if n_list[i][1] == "leave":
        n_set.remove(n_list[i][0])

for name in n_set:
    print(name)


# 두 번쨰 - 성공...
# import sys
input = sys.stdin.readline

n = int(input())
n_set = set()

for i in range(n):
    name, company = input().split()
    if company == "enter":
        n_set.add(name)
    elif company == "leave":
        n_set.discard(name)

for name in sorted(n_set, reverse=True):
    print(name)

# 결론
# 함수를 잘 사용하자..
