# 10816_숫자-카드2

# 문제 분석
# 상근이가 숫자 카드 N개를 가지고 있을 때 정수 M개가 주어진다면 이 정수가 적혀있는 숫자 카드를
# 상근이가 몇개를 가지고 있는지 구하기


# 해결 과정서
# 첫 번째 - 실패: 시간 초과
# 리스트와 딕셔너리를 이용한 고전적인 방법으로 각각 저장(초기값(개수) -> 0)
import sys
from collections import Counter  # 두 번째 코드 때 활용
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_dict = {}
m_list = list(map(int, input().split()))

for i in m_list:
    m_dict[i] = 0
for i in n_list:
    for j in m_list:
        if i == j:
            m_dict[j] += 1

for i in m_list:
    print(m_dict[i], end=" ")

# 두 번째
# 도저히 모르겠어서 gpt한테 물어보았다...

# import sys
# from collections import Counter
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# n_list의 빈도를 미리 카운트
n_count = Counter(n_list)

# m_list의 각 값에 대해 결과 출력
for i in m_list:
    print(n_count.get(i, 0), end=" ")

# 세번째
# collections 사용안하는 다른 방법
# import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())  # n_list의 크기
n_list = list(map(int, input().split()))  # n_list의 값들
m = int(input())  # m_list의 크기
m_list = list(map(int, input().split()))  # m_list의 값들

# n_list의 값들을 카운팅할 딕셔너리 생성
m_dict = {}

for i in n_list:
    if i in m_dict:
        m_dict[i] += 1  # 이미 있으면 값 증가
    else:
        m_dict[i] = 1  # 없으면 값 1로 초기화

# m_list에 대해 빈도수를 출력
for i in m_list:
    if i in m_dict:
        print(m_dict[i], end=" ")  # n_list에서 등장한 횟수 출력
    else:
        print(0, end=" ")  # m_list에 있지만 n_list에 없는 값이면 0 출력

# 결론
# 새로운 문제를 접할 때마다 어렵다...
