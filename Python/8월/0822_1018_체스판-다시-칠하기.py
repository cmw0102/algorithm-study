# 1018_체스판-다시-칠하기
# 문제 분석
# 체스판은 검정, 흰색 으로 바닥이 이루어져있다.
# 따라서, 검정검정 또는 흰색흰색 이렇게 되면 안되기 때문에 닿아있는 사각형들은 서로 색이 달라야함

# 해결 과정
# 여러 생각들을 하였으나 구현을 하지 못하여 다른 사람의 코드를 참조하여 공부하고 해당 문제를 품

# 참조하여 생각한 해결 방법
# 첫 번째: 전체 보드판에서 체스판의 첫 시작 부분을 결정해야하는데 8*8이므로 전체 인덱스 범위를 초과하지 않게 해야함
#         예를 들면 전체 보드의 크기가 12*12이면 8*8의 시작지점을 정할 때 만약 시작 지점 좌표가 (5,5)면 전체 보드의 크기를
#         벗어나기 때문에 이러한 문제를 방지하기 위해 M과 N에서 각각 -7을 해주어야 함.
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
        color_black = 0  # 검정색이 아닐때 증가(검정색을 칠하기 위해)
        color_white = 0  # 흰색이 아닐때 증가(흰색을 칠하기 위해)
        for a in range(i, i + 8):  # 체스의 크기인
            for b in range(j, j + 8):  # 8*8 크기를 구현하기 위해 +8로 설정
                if (a + b) % 2 == 0:  # a + b를 2로 나눈 값이 홀수 인지 짝수 인지 구분하여 어떠한 색을 추가할지 조건문을 통해 해결
                    if board[a][b] != 'B':  # 첫 시작 지점이 검정이 아닐 경우
                        color_black += 1  # 검정색을 칠해줌
                    if board[a][b] != 'W':  # 첫 시작 지점이 흰색이 아닐 경우
                        color_white += 1  # 흰색을 칠해줌
                else:
                    if board[a][b] != 'W':  # 첫 시작 지점이 흰색이 아닐 경우
                        color_black += 1  # 검정색을 칠해줌
                    if board[a][b] != 'B':  # 첫 시작 지점이 검정이 아닐 경우
                        color_white += 1  # 흰색을 칠해줌
        result.append(color_black)
        result.append(color_white)
print(min(result))
