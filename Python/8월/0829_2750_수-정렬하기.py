# 2750_수-정렬하기 - 문제단계: 정렬

# 문제 분석
# 오름차순 정렬 문제로
# 첫 번째 입력은 수의 개수
# 두 번째 입력은 수 입력

# 해결 과정
# 첫 번째
# 여러 정렬 방법이 있었지만 다른 정렬 방법보다 간단하게 구현이 가능한
# 선택 정렬로 풀기로 하였다
# 선택 정렬은 최솟값을 구하는 방식으로 풀면 된다.

# 선택 정렬 (최종 답안)
import sys
input = sys.stdin.readline
n = int(input())  # 입력할 수의 개수 입력
n_list = []

for i in range(n):
    n_list.append(int(input()))  # N번 만큼 수를 입력 받음

for i in range(n-1):
    min_index = i  # 현재 위치를 최소값의 인덱스로 가정
    for j in range(i+1, n):
        if n_list[min_index] > n_list[j]:  # 더 작은 값을 찾으면 min_index를 업데이트
            min_index = j
    # 최소값을 현재 위치로 이동
    n_list[i], n_list[min_index] = n_list[min_index], n_list[i]
    # 튜플 언패킹
    # n_list[i] = n_list[min_index]
    # n_list[min_index] = n_list[i]
for i in range(n):
    print(n_list[i])


# 선택 정렬 (처음에 본인이 작성한 코드)
# import sys
input = sys.stdin.readline
n = int(input())  # 입력할 수의 개수 입력
n_list = []

for i in range(n):
    n_list.append(int(input()))  # N번 만큼 수를 입력 받음

for i in range(n-1):
    temp = n_list[i]
    temp2 = i
    for j in range(i+1, n):
        if n_list[i] > n_list[j] and temp > n_list[j]:
            temp = n_list[j]
            temp2 = j
    n_list[temp2] = n_list[i]
    n_list[i] = temp

for i in range(n):
    print(n_list[i])
# 결론
# 선택 정렬을 찾아본 결과 본인이 작성한 코드에서 문제점은 temp와 temp2로 나누어서 값과 인덱스를 따로 설정했다는 것이다.
# 이로 인해 두 변수 모두 초기화를 한 번씩 해줘야 했다.
# 이를 해결한 방법은 최종 답안과 같이 인덱스 변수 하나만을 생성하여 값도 인덱스 변수로 구할 수 있게 작성하는 것이다.
# 결국 현재위치를 최솟값의 인덱스로 가정하는 방향은 같았지만 좀 더 간결하게 작성해야한다.
# ++ if문 안에 조건문도 복잡함(굳이다 싶은 코드 조합임)
# [처음 작성한 코드는 런타임 에러가 발생했음]
# 선택 정렬이라는 개념을 아는 것을 별개로 이를 코드로 구현한다는게 상당히 어렵고 복잡한 것 같다...
# 열심히 하자.

# ++ 삽입 정렬
# https://velog.io/@aosdbfc/Python-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-7.1.-%EB%B2%84%EB%B8%94%EC%84%A0%ED%83%9D%EC%82%BD%EC%9E%85-%EC%A0%95%EB%A0%AC
# 위 블로그를 참조하여 삽입정렬을 어떻게 구현하는지 개념을 공부한 후
# 참고하여 문제를 풀기위한 코드에 녹였다.
# 정렬에 대해서 이해를 많이 하고 체화시켜야겠다!!!
# import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for i in range(n):
    n_list.append(int(input()))

for i in range(1, n):
    for j in range(i, 0, -1):
        if n_list[j] < n_list[j-1]:  # 앞 뒤의 수 비교
            n_list[j], n_list[j-1] = n_list[j-1], n_list[j]
        else:
            break

for i in range(n):
    print(n_list[i])
