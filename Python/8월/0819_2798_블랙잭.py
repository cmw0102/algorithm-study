# 2798_블랙잭
N, M = map(int, input().split())
card = list(map(int, input().split()))
for i in range(N):
    for j in range(i+1, N):
        for k in range(i+2, N):
            sum = card[i] + card[j] + card[k]
            if sum <= M:
                result = max(result, sum)
print(result)
