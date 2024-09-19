# 7785_회사에-있는-사람

# 문제 분석
# 출퇴근 로그를 통해 현재 회사에 있는지 여부를 구하는 문제이다.
# enter인 경우 출근, leave인 경우 퇴근

# 해결 과정
# 첫 번째 - 실패(런타임 에러)
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

for name in sorted(n_set, reverse=True):
    print(name)


# 두 번쨰 - 성공...
# 이번엔 리스트를 사용하지 않고 풀어보려고 했다.
# name, company 두 변수로 각각 이름과 출퇴근 여부를 입력받았고
# 이를 이용하여 company 변수가 enter일 때는 n_set에 name를 추가하였고
# company 변수가 leave일 때는 n_set에서 name을 제거하였다.(discode 이용)
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
# 첫 번째 방법으로 맨 처음 틀렸을 때는 그냥 틀렸다고 나왔다. (이 원인은 단순하다... 최종 출력 때 역순을 안함)
# 문제는 최종 출력문을 수정해도 런타임에러가 발생하는 것이었다.
# 원인은 remove에 있었다.
# remove는 집합에 있는 요소를 삭제하지만 만약 집합에 없는 요소를 삭제하게 되면 KeyError*(존재하지 않는 키나 요소를 참조하려고 할 때 발생하는 오류)가 발생한다.
# 따라서 이러한 상황이 생기지 않게 discard를 사용하여 에러가 발생하지 않게 하면된다.
# discard: 집합에 존재하지 않는 요소를 제거해도 에러를 발생시키지 않고 넘어간다.
# 함수를 잘 사용하자..
