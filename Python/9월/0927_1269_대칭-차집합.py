# 1269_대칭-차집합

# 문제 분석
# &을 써서 중복 되는 것을 구한 후 대칭 차집합의 특성을 이용하여 풀기
# A + B - 2(A∩B) 를 하면 AUB - A∩B값을 알 수 있음

# 해결 과정
# 첫 번째
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

ab_list = list(a_set & b_set)

print(len(a_set) + len(b_set) - 2 * len(ab_list))

# 결론
# 벤 다이어그램을 생각하면서 문제를 쉽게 푼 것 같다.

# 다른 사람의 풀이
# 출처: https://alpyrithm.tistory.com/165
# 여기서는 나처럼 중복된 요소를 구해서 계산하는 방식이 아닌
# 기존에 구한 a_set, b_set을 이용하여
# len(a_set - b_set) + len(b_set - a_set)
# 위와 같은 수식으로 구하였다.

# 나도 좀 더 쉽고 간결하게 풀어야겠다..
