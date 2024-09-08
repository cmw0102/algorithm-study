# 11650_좌표-정렬하기

# 문제 분석
# 2차원 평면 위의 점 N개가 주어지고 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬하기
# 즉, x좌표를 기준으로 오름차순 정렬을 하되 x좌표의 값이 동일할 때는 y좌표를 기준으로 오름차순 정렬을 하면 된다.

# 해결 과정
# 첫 번째 - 성공
# 시간 복잡도: O(n * log n)
# 2차원 리스트 만들기

import sys
input = sys.stdin.readline
n = int(input())

n_list = []

for i in range(n):
    # 리스트 컴프리헨션을 이용하여 2차원 리스트 생성
    n_list.append([int(j) for j in input().split()])

n_list.sort()

for i in range(n):
    print(n_list[i][0], n_list[i][1])

# 두 번째 - 성공
# 시간 복잡도: O(n * log n)
# 직접 변수 x, y를 만들어서 리스트에 넣기로 결정했다.
# import sys
input = sys.stdin.readline
n = int(input())

n_list = []

for i in range(n):
    [x, y] = map(int, input().split())
    n_list.append([x, y])

n_list.sort()
for i in range(n):
    print(n_list[i][0], n_list[i][1])

# 결론
# 첫 번째 방법이 맨 처음 실패 했다가 두 번째 방법 성공 후 코드의 차이가 별로 나지 않아
# 확인 한 결과 정렬을 할 때 for문에 태워 하고 있었다.
# 이러면 시간 복잡도가 O(n * log n)가 아닌 O(n^2 * log n) 가 되어서 매우 오래걸리게 된다.
# 시간 복잡도를 항상 생각하면서 코드를 작성해야겠다.

# ++  추가 공부
# n_list.append([int(j) for j in input().split()])
# 여기서 대괄호를 지우고
# n_list.append(int(j) for j in input().split())
# 이렇게 표현 하면 제너레이터 표현식이 된다.
# 제너레이터 표현식이란?
# 값들을 한 번에 메모리에 모두 올려놓지 않고, 필요할 때마다 하나씩 생성하는 값을 반환하는 표현식(메모리 관리에 더 효율적!)

# 리스트 컴프리헨션과 제너레이터의 차이점
# 리스트 컴프리헨션 ([int(j) for j in input().split()]):
# 리스트를 즉시 생성하며, 모든 값을 메모리에 담아 한 번에 반환한다.
# 제너레이터 표현식 (int(j) for j in input().split()):
# 제너레이터 객체를 반환하며, 모든 값을 한 번에 생성하지 않고, 필요할 때마다 값을 생성한다. (lazy evaluation).
