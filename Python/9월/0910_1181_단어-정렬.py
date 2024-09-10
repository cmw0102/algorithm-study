# 1181_단어-정렬

# 문제 분석
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면
# 첫 번째 기준 - 길이가 짧은 것부터
# 두 번째 기준 - 길이가 같으면 사전 순으로(알파벳 단어 숫 같음)
# 위의 기준으로 정렬하기
# 중복된 단어는 하나만 남기고 제거 하기

# 해결 과정
# 첫 번째 - 성공
# 시간 복잡도: O(n * m + n * log(n))
# 람다 함수를 써서 두 개의 정렬 기준을 처리하고 0번 인덱스를 제외한
# 1번 인덱스 부터 전의 인덱스와 다를시 출력하고 같으면 넘어가는 방식으로 코드를 구현할 예정

# 코드
import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for _ in range(n):
    n_list.append(input().strip())  # strip -> 개행문자 제거

n_list.sort(key=lambda x: (len(x), x))

print(n_list[0], end="")
for i in range(1, n):
    if n_list[i-1] != n_list[i]:
        print(n_list[i], end="")

# 결론
# 람다 함수를 이용하여 쉽게 정렬하는데 성공 했다.
# 람다 함수를 이용한 방법도 좋지만 다른 방버도 생각을 해봐야겠다.

# ++ 추가 공부
# 내가 사용한 중복 제거 방법은 단순한 방식으로
# 리스트의 첫 번째 값을 출력한 후, for문을 돌려 중복을 확인 한 후 중복이 아닌 값만 차례대로 출력 하게 만들었다.
# 하지만 다른 사람들의 코드를 찾아본 결과 set() 함수(중복 제거 함수)를 이용하여 중복을 제거한 것을 알 수 있다.
# 이는 파이썬 문법을 아직 제대로 잘 다루지 못하는 나한테서 나온 문제점이기 때문에 갈고 닦아서 코드를 더 유연하게 작성할 수 있도록 노력해야겠다.
# set함수 사용법 -> n_list = list(set(n_list))

# 더 깔끔한 코드 (gpt 코드)
# 시간 복잡도: O(n * m + n * log(n))
# import sys
input = sys.stdin.readline
n = int(input())
n_list = []

for _ in range(n):
    n_list.append(input().strip())  # 입력 후 strip()으로 개행 문자 제거

n_list = list(set(n_list))  # 중복 제거
n_list.sort(key=lambda x: (len(x), x))  # 길이와 알파벳 순으로 정렬

for i in range(len(n_list)):  # n 대신 len(n_list)
    print(n_list[i])

# 의문
# 코드는 간결해져도 시간 복잡도는 동일 하다면... 어떻게 해야 할까
# 공부해봅시다..
