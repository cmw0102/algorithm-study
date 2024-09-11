# 10814_나이순-정렬

# 문제 분석
# 정렬 기준 - 첫 번째: 나이순 / 두 번째: 먼저 가입한 순
# 입력 - 첫 번째: 입력할 사람 수 / 두 번째: 나이 이름 순으로 입력

# 해결 과정
# 첫 번째 - 실패
# 시간 복잡도: O(n log n)
# sort와 lambda함수를 이용하여 정렬하려고 한다.
# 막연하게 두 번째 정렬 기준인 가입 순 정렬은 따로 정렬기준을 정하지 않아도 vscode에서는 정상적으로 돌아가서
# 이렇게 해도 되는건가 하고 문제풀이를 시도하였지만 틀렸다.

import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for i in range(n):
    [age, name] = map(str, input().split())
    int(age)
    n_list.append([age, name])

n_list.sort(key=lambda x: x[0])


for i in range(n):
    print(n_list[i][0], n_list[i][1])

# 두 번째 - 성공
# 시간 복잡도: O(n log n)
# 두 번째 정렬 기준인 가입 순으로 정렬을 시도 하려면 입력 할 때 마다 인덱스 값이 필요한 것을 알았지만
# 어떻게 구현을 해야 할지 고민을 한 끝에
# n_list에 새로운 요소 하나를 추가하여 자연스럽게 몇번째 인덱스인지 확인 할 수 있고
# 그 요소를 통해 정렬하는 것을 sort와 lambda를 활용하여 구하기로 하였다.
# import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for i in range(n):
    age, name = input().split()
    n_list.append((int(age), name, i))

n_list.sort(key=lambda x: (x[0], x[2]))

for i in range(n):
    print(n_list[i][0], n_list[i][1])

# 결론
# 코드를 좀 더 간결하게 적어야 할 것 같다.
# map함수를 습관적으로 작성하는데 필요할 때 쓰고 불필요할 땐 안쓰는 습괍을 가져야겠다.
# map함수 ->> 한 번에 여러값을 받을 때 같은 타입으로 변환시 사용해야함
#         ->> 그렇지 않고 여러 타입으로 변환 해야 할 때는 map을 안쓴 상태로 입력을 받아야함.
