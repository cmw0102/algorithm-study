# 14425_문자열-집합

# 문제 분석
# 입력한 M개의 문자열 중에 집합 S에 포함되어 있는 것이 총 몇 개인지 구하기
# (S는 N개의 문자열로 이루어져 있음)

# 해결 과정
# 첫 번째 - 성공
# 시간 복잡도: O(n+m)
# set을 이용해서 빠르게 검사할 수 있는 코드로 구현하고자 한다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = []
m_list = []
count = 0
for i in range(n):
    n_list.append(input())
for i in range(m):
    m_list.append(input())

n_set = set(n_list)

count = [count + 1 for item in m_list if item in n_set]

print(len(count))

# 결론
# 전에 풀었던 10815_숫자 카드와 비슷하게 set과 컴프리헨션을 이용하여 풀었다.
# 좀 더 다양한 문제를 풀면서 익숙해져야겠다.


# 다른 사람의 풀이 방법 분석
# 시간 복잡도: O(n)
# 출처: https://velog.io/@jswon/%EB%B0%B1%EC%A4%80-14425-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A7%91%ED%95%A9-python
# import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set()  # 집합 S 생성
for i in range(N):
    S.add(input())  # 집합 S에 앞서 입력한 N만큼 add를 이용하여 요소를 추가(나와 다른 점: list를 이용하지 않음)
ans = 0  # 몇 개가 같은지 체크하기 위한 변수 정의
for _ in range(M):
    t = input()  # 앞서 입력한 M만큼 입력하는데
    if t in S:  # 만약 입력한 문자열이 앞에서 정의한 집합 S에 있는 문자열 요소와 같을 경우
        ans += 1  # 앞에서 정의한 체크 변수에 + 1을 해준다.
print(ans)
# 분석)
# 컴프리헨션을 이용하여 검사하는 코드를 한 줄로 줄인 것은 잘한 것 같다.
# 하지만 set을 제대로 활용하지 못하고 list 생성 후 set으로 변환하여 문제를 뱅뱅 돌면서 푼 것 같다.
