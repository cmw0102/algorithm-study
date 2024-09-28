# 11478_서로_다른_부분_문자열의_개수

# 문제 분석
# 문자열이 주어졌을 때, 서로 다른 부분 문자열의 개수를 구하기
# ex) ababc -> a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc
# 이렇게 분리 할 수 있는데 여기서 서로 다른 부분 문자열의 개수는 12개 이다.
# 12개: a, b, c, ab, ba, bc, aba, bab, abc, abab, babc, ababc

# 해결 과정
# set을 이용하여 저장
# 입력 받은 문자열의 길이를 이용하여 한글자 부터 문자열 최대 길이 까지 저장

import sys
input = sys.stdin.readline
S = input().rstrip()
S_set = set()

for i in range(len(S)):
    for j in range(i, len(S) + 1):
        if i == j:
            S_set.add(S[i])
        else:
            S_set.add(S[i:j])

print(len(S_set))

# 결론
# 순서대로 넣다보면
# ['a', 'ab', 'aba', 'abab', 'ababc', 'b', 'ba', 'bab', 'babc', 'a', 'ab', 'abc', 'b', 'bc', 'c']
# 이렇게 입력 값이 들어가는 의도한 바와 같이 모든 경우의 수가 들어가고
# 이를 set에 저장하면 중복값이 제거 된다.

# 다른 사람들의 풀이
# 출처: https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-11478%EB%B2%88-%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 코드

s = input()
total = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        total.add(s[i:j+1])  # i번째 문자부터 부분문자열 구하기

print(len(total))

# 풀이
# 나의 풀이과정과 비슷하지만 결정적인 것은 인덱싱을 할 때 한 번에 한다는 것이다.
# 아직 간결하게 작성하는게 어려운 것 같다.
# 인덱싱에 대한 이해도를 높여야겠다.
