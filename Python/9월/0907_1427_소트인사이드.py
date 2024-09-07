# 1427_소트인사이드

# 문제 분석
# 내림차순으로 정렬하기
# 첫째 줄에 임의의 수들을 나열하면
# 내림차순으로 정렬 후 출력함.

# 해결 과정
# 첫번째
# sort(reverse=True)함수 이용

import sys
input = sys.stdin.readline
n = int(input())

n_list = []
for i in str(n):
    n_list.append(int(i))

n_list.sort(reverse=True)

for i in n_list:
    print(i, end='')


# 결론
# 블로그를 참고한 결과 위의 코드가 나옴
# sort(reverse=True)를 사용하고자 하는 부분에서는 나와 블로그와 동일 했으나
# 좀 더 유연하게 생각을 해야겠다...
# https://jiwon-coding.tistory.com/9 -> 블로그 주소

# chatgpt에 물어본 결과
# 수 N을 입력받는다.
N = input()

# 자릿수를 내림차순으로 정렬한 후, 문자열로 이어붙여 출력한다.
print(''.join(sorted(N, reverse=True)))
# 이렇게 두 줄로 끝낼 수 있다는 것에 있어 파이썬을 더 공부해야겠다는 생각이 들었다.

# ++ 추가 공부
# sort(): 원본 리스트를 직접 정렬할 때, 메모리 효율이 중요한 경우에 많이 사용
# sorted(): 원본 데이터를 유지하거나, 리스트 외의 이터러블을 정렬할 때 사용
