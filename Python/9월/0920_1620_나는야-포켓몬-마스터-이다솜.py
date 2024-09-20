# 1620_나는야-포켓몬-마스터-이다솜

# 문제 분석
# 사전형태의 문제를 푸는 것으로 이해하면 된다.
# 미리 원하는 개수의 단어를 입력하고 그 후 풀어야 하는 개수를 입력한 후
# 숫자 입력(여기선 인덱스가 됨) -> 그 순서(숫자)에 해당하는 단어 출력
# 단어 출력 -> 단어에 해당하는 순서(숫자) 출력

# 해결 과정
# 첫 번째 - 실패(시간 초과)
# 시간 복잡도: O(n + m * n)
# 시간 복잡도가 크게 나온 이유: n_list.index(k) 부분에서 추가로 O(n)이 소요되기 때문..
# 문자열 k가 리스트의 몇 번째에 위치하는지를 찾는 작업은 리스트 전체를 순회해야 하기 때문이다.
# 리스트를 생성한 후, 숫자인지 판별하는 isdigit()와 인덱스 번호를 사용하기 위해
# index()를 이용하여 문제를 풀었다.
# 하지만 시간이 초과 되어 문제를 성공하지는 못했다.

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = []
m_list = []
for i in range(n):
    n_list.append(input().strip())

for i in range(m):
    k = input().strip()
    if k.isdigit() == True:  # k가 숫자일 때
        m_list.append(n_list[int(k)-1])
    elif k.isdigit() == False:  # k가 숫자가 아닌 문자열 일 때
        m_list.append(n_list.index(k) + 1)

for po in m_list:
    print(po)


# 두 번째 - 시간 복잡도: O(n + m)
# 도저히 풀 방법이 생각이 안나서 gpt의 도움을 받았다.
# 기존 코드에서 딕셔너리를 생성하여 딕셔너리의 특징을 이용하여 사전을 만들 수 있다.
# import sys
input = sys.stdin.readline
n, m = map(int, input().split())

n_list = []  # 순서 있는 리스트
n_set = set()  # 검색을 위한 set
n_dict = {}  # 이름과 인덱스를 매칭할 딕셔너리

for i in range(n):
    name = input().strip()
    n_list.append(name)  # 리스트에 추가
    n_set.add(name)  # set에 추가
    n_dict[name] = i + 1  # 딕셔너리에 이름과 인덱스(1부터 시작)를 저장

m_list = []  # 결과를 저장할 리스트

for i in range(m):
    k = input().strip()
    if k.isdigit():  # k가 숫자인 경우
        m_list.append(n_list[int(k)-1])  # 리스트에서 인덱스로 검색
    elif k in n_set:  # k가 숫자가 아닌 문자열인 경우
        m_list.append(n_dict[k])  # 딕셔너리에서 해당 이름의 인덱스 가져오기

for po in m_list:
    print(po)


# 결론
# 결국 내 스스로 문제를 풀지 못했다.
# 실버4에 해당하는 문제여서 혼자 할 수 있을 거라 생각했는데
# 아직까지 기존에 배웠던 함수나 개념을 제대로 응용하지 못한 부분과
# 간단한 문제를 너무 어렵게 풀어내려고 하는 것을 고쳐야겠다는 생각이 들었다.
# KEY POINT: 입력받은 값을 dict에 key : value로 번호 : 이름, 이름 : 번호로 한 번씩 저장한 후 그대로 찾아서 출력하는 것을 찾아내야한다.


# 다른 사람의 코드 - 시간 복잡도: O(n + m)
# 출처: https://gudwns1243.tistory.com/63
# 코드
# import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
# 코드 분석
# 이 코드도 딕셔너리를 이용하여 구현하고 있다.
# 먼저 딕셔너리를 생성한 후, 첫 번째 for문에서 인덱스와 문자열로 이루어진 사전을 생성하고있다.
# 두 번째 for문에서 입력받은 요소를 if-else문을 이용하여 출력할 값을 구하는데
# if에서는 isdigit를 이용하여 quest값이 숫자면 그 숫자(순서)에 해당하는 dict값을 출력하고,
# 숫자가 아니라면 dict[quest]를 통해 인덱스(순서, 숫자)를 출력한다.
