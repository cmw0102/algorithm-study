# 25305_커트라인

# 문제 분석
# 응시자 수 n 상을 받는 사람의 수 k 차례로 입력
# 둘째 줄에 각 학생의 점수를 공백을 기준으로 입력

# 해결 과정
# 첫 번째 - 삽입 정렬로 풀기
# 삽입 정렬을 통해 오름차순 정렬을 한 후, 전체 인원 n명에서 수상자 인원 k명을 뺀 수가
# 커트라인 인덱스와 동일 하다는 점을 파악하고 코드를 구현하고자 하였다.

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
n_list = (list(map(int, input().split())))

for i in range(1, n):
    for j in range(i, 0, -1):
        if n_list[j] < n_list[j-1]:
            n_list[j], n_list[j-1] = n_list[j-1], n_list[j]
        else:
            break

print(n_list[n-k])

# 결론
# 처음에는 n_list = [], append, split을 이용하여 리스트에 입력하여 하였으나
# 리스트 안에 리스트가 생기는 문제가 발생하였고
# 구글링을 하여 n_list = (list(map(int, input().split())))와 같이 입력된 값을 리스트로 변환하고
# 다시 리스트 변수로 값을 대입하는 것을 찾았다.
# 아직 파이썬에 대해 많이 부족한 것 같다.
# 더 열심히 문법을 공부하여 코딩테스트를 준비해야 할 것 같다.
