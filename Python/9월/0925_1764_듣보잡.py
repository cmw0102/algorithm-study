# 1764_듣보잡

# 문제 분석
# n명단(듣도 못한 사람 명단), m명단(보도 못한 사람 명단)이 있을 때
# n명단(듣도 못한 사람 명단) 구하기

# 첫째 줄: n m 입력
# 둘째 줄 ~ : n개의 줄에 걸쳐 n명단(듣도 못한 사람 명단) 입력
# n + 2 줄 ~ : m명단(보도 못한 사람 명단) 순서대로 입력
#              (결국 n명단 다음에 m명단 오는 거임)

# 출력: 듣보잡의 수와 그명단을 "사전순"으로 출력
# 포인트: 즉 두 그룹에 속한 사람의 수와 이름을 사전순으로 출력해야함

# 해결 과정
# 첫 번째 - 성공

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nm_list = []
n_set = set()
m_set = set()

for i in range(n):
    n_set.add(input().rstrip())
for i in range(m):
    m_set.add(input().rstrip())

for i in n_set:
    if i in m_set:
        nm_list.append(i)

nm_list.sort()

print(len(nm_list))
for i in nm_list:
    print(i)

# 결론
# 오랜만에 한 번에 성공 하였다.
# 저번에 list로 저장된 요소를 찾는 것 보다 set으로 저장된 요소를 찾는게 더 빠르다는 것을 배웠기 때문에
# 이번에는 set을 이용하여 찾는 방식으로 해보았다.
# 그 다음 둘 다 포함되는 요소는 추후 출력할 때 사전순으로 정렬을 해야해서
# sort()를 용이하게 사용하기 위해 미리 list를 만들었다.

# 추가 풀이
# 나처럼 새로운 리스트를 생성하는 것이 아닌 &를 이용하여 한 번에 정렬과 출력까지 하는 방법이 있다.
# 하는 방법)
# n_set 과 m_set을 이용하여 저장하는 단계까진 같다
# 그러나 새로운 변수를 이용하여 정렬과 중복값을 뽑아내는 코드가 다르다.
# -> new_nm = sorted(list(n_set & m_set)) 이렇게 작성하면 정렬과 중복값을 한 번에 출력 가능하다.

# 저 한 번에 출력하는 코드를 작성하는게 가독성도 좋고 코드 작성 시간도 줄일 수 있어서 효율적인것 같다.
