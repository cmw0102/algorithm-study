# 1018_체스판-다시-칠하기
# 문제 분석
# 체스판은 검정, 흰색 으로 바닥이 이루어져있다.
# 따라서, 검정검정 또는 흰색흰색 이렇게 되면 안되기 때문에 닿아있는 사각형들은 서로 색이 달라야함

# 해결 과정
# 여러 생각들을 하였으나 구현을 하지 못하여 다른 사람의 코드를 참조하여 공부하고 해당 문제를 품

# 참조하여 생각한 해결 방법
# 첫 번째: 전체 보드판에서 체스판의 첫 시작 부분을 결정해야하는데 8*8이므로 전체 인덱스 범위를 초과하지 않게 해야함
#         예를 들면 전체 보드의 크기가 12*12이면 8*8의 시작지점을 정할 때 만약 시작 지점 좌표가 (5,5)면 전체 보드의 크기를
#         벗어나기 때문에 이러한 문제를 방지하기 위해 M과 N에서 각각 -7을 해주어야 원 위치 안에 들어감
# 두 번째: 색상이 중복되면 안되기 때문에 반대되는 것을 색칠하면 된다.

import sys
input = sys.stdin.readline
M, N = map(int, input().split())
board = []
result = []

for i in range(M):
    board.append(input())

for i in range(M-7):
    for j in range(N-7):
        color_black = 0  # 첫 시작 지점의 색이 검정색인 경우
        color_white = 0  # 첫 시작 지점의 색이 흰색인 경우
        for a in range(i, i + 8):  # 체스의 크기인
            for b in range(j, j + 8):  # 8*8 크기를 구현하기 위해 +8로 설정
                # 짝수 칸
                if (a + b) % 2 == 0:  # a + b를 2로 나눈 값이 홀수 인지 짝수 인지 구분하여 어떠한 색을 추가할지 조건문을 통해 해결
                    # if문과 else문을 통해
                    # 행과 열의 합을 기준으로 짝수칸, 홀수칸을 구분짓는다.
                    # 결론 부분의 내용처럼 짝수칸인지 홀수칸인지 상황에 따라 어떠한 경우의 수(첫 시작 지점의 색이 흰색인지 검정색인지)에 +1을 해야할지 정하는 코드이다.
                    if board[a][b] != 'B':  # 해당 좌표가 검정이 아닌 경우
                        color_black += 1
                    if board[a][b] != 'W':  # 해당 좌표가 흰색이 아닌 경우
                        color_white += 1
                # 홀수 칸
                else:
                    if board[a][b] != 'W':  # 해당 좌표가 흰색이 아닌 경우
                        color_black += 1
                    if board[a][b] != 'B':  # 해당 좌표가 검정이 아닌 경우
                        color_white += 1
        result.append(color_black)
        result.append(color_white)
print(min(result))

# 결론
# 결국 첫 시작 지점의 색이 검정색, 흰색 둘 중 하나이기 때문에 두가지 경우의 수 밖에 없다.
# 체스판의 경우 첫 시작지점의 색을 기준으로 짝수 칸은 같은색, 홀수 칸은 다른색으로 존재해야한다.
# 따라서 첫 시작지점의 색을 기준으로 짝수 칸, 홀수 칸의 색을 칠하는데
# 이때, color_black의 값이 +1 되었을 경우 color_white에게는 아무런 영향을 주지 않는다.
# 왜냐하면, color_black의 입장에서는 올바르지 않기 때문에 색을 알맞게 칠한 것이고 +1을 해준것 이지만
# color_white의 입자에서는 올바르기 때문에 아무런 변화가 없는 것이다!!
