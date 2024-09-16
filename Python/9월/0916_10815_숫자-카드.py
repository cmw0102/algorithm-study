# 10815_숫자-카드

# 문제 분석
# 임의의 정수 M개가 있을 때 상근이가 가지고 있는 정수와 비교하여 상근이가 가지고 있을때는 1, 없을 때는 0을 입력

# 해결 과정
# 첫 번째 -> 시간 초과로 실패
# 리스트 생성 후 딕셔너리 따로 만들어서 풀고자 했다.
import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
m_dict = dict()

for i in range(len(m_list)):
    m_dict[m_list[i]] = 0
    for j in range(len(n_list)):
        if m_list[i] == n_list[j]:
            m_dict[m_list[i]] = 1

for i in m_list:
    print(m_dict[i], end=" ")


# 두 번째 - 집합과 딕셔너리 컴프리헨션 이용
# import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_set = set(n_list)
m_dict = {item: 1 if item in n_set else 0 for item in m_list}

for i in m_list:
    print(m_dict[i], end=" ")

# 결론
# 맨 처음 이중 for문을 이용하였을 때 시간초과로 인해 푸는데 실패를 했었다.
# 그래서 어떻게 풀어야 할 지 고민하고 찾아본 결과 set을 이용하여 비교시 검색 속도를 높일 수 있다는 점에서 set을 이용하였다.
# (set 이용시 검색 시간 복잡도는 O(1)이지만 list를 이용해서 검색하면 시간 복잡도가 O(n)이다.) -> 해시테이블 사용
# (이는 list가 배열과 유사하게 요소가 순차적으로 저장되며 특정 요소를 검사하기 위해 요소를 하나하나 확인하기 때문이다.)
# ++ 컴프리헨션 사용법 익히기
# 아직 컴프리헨션을 완벽하게 익히지 못해서 더 익숙해지게 많이 사용해야겠다.
