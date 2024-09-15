# 18870_좌표-압축

# 문제 분석
# 문제에서 말하는 좌표 압축은 예를 들어
# 4 8 6 3 2 와 같은 5개의 좌표가 있을 때
# 4의 좌표 압축 값이 4 보다 작은 3, 2를 포함하여 2개 즉, 2인 것을 말한다.
# 결국 각 좌표의 값을 비교하여 자기 보다 작은 서로 다른 값(중복 안됨)의 개수를 말하는 것이다.

# 해결 과정
# 첫 번째
# 처음에는 요소를 추가해서 인덱스 값을 알아내어 푸는 방식을 생각하였는데
# sort 정렬을 하면 나중에 출력 할 때 올바르게 출력을 못해서 어떻게 할 지 고민이 많았는데
# sorted을 이용하면 원본은 그대로인 상태에서 원하는 정렬과 값을 구할수 있겠다는 생각이 들었다.
# 근데 sorted사용법을 전에 정리하긴 했으나 사용해본적은 없어서 사용법을 구글링 하던 도중
# 딕셔너리를 sorted을 이용하여 정렬해도 키값과 벨류값은 서로 고정되어 변하지 않는 다는 점을
# 알게 되었고 이를 통해 처음에 고민했던 부분이 딕셔너리의 특징을 통해 해결 되는 것을 알게되었다.
# 딕셔너리를 다시 한 번 공부하면서 문제에 어떻게 적용해야 할 지 고민을 하였다.
#
# 과정!!
# 1. n_list에 값을 넣은 후 set(중복 제거)과 sorted를 이용하여 정렬한 값을 n_list2에 넣을 것이다.
# 2. n_list2를 이용하여 압축된 좌표의 개수를 구한다.
#    딕셔너리를 이용하면 n_list2의 요소값이 key값이 되고 각 요소의 좌표값이 value값이 된다.
# 4. 그런 다음 n_list의 요소(key값)에 해당하는 value값(압축된 좌표 값)을 그대로 출력하는 코드를 구현하고자 한다.

import sys
input = sys.stdin.readline
n = int(input())

# 1
n_list = list(map(int, input().split()))  # 입력받은 값 바로 리스트로 저장
n_list2 = sorted(list(set(n_list)))  # set이용해서 중복 제거
# 2
n_dict = dict()  # 딕셔너리 생성
for i in range(len(n_list2)):  # set과 sorted를 이용하여 중복 제거 및 정렬된 n_list2의 인덱스를
    n_dict[n_list2[i]] = i  # 이용하여 서로다른 좌표 압축 값 입력
# 3
for i in n_list:  # n_list를 for문을 통해 차례대로 뽑아내어
    print(n_dict[i], end=" ")  # 미리 만들어둔 n_dict 딕셔너리에 요소를 넣은면 서로다른 좌표 압축값이 출력 됨
# 출처 - sorted 정렬 공부한 블로그
# https://blockdmask.tistory.com/466

# 결론
# 문제를 풀면서 개념을 다시 공부하고 정리하다보니 시간이 많이 걸린 것 같다.
# 딕셔너리를 좀 더 잘 활용하여 문제를 풀어야겠다.


# 다른사람의 코드 (출처: https://gudwns1243.tistory.com/52)
# 이 사람의 코드는 내가 작성한 코드와 흐름은 비슷하나 딕셔너리를 구성하는 부분에서 달랐다.
# 딕셔너리 생성을 효율적으로 작성하는 방법을 생각해야겠다.
# import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i]: i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end=' ')
