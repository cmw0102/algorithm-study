T = int(input())

for i in range(T):
    score = [0 for i in range(101)]
    num = int(input())
    n = list(map(int, input().split()))
    for j in range(len(n)):
        score[n[j]] = score[n[j]] + 1
        max_score = max(score)
        for k in range(100, 0, -1):
            if max_score == score[k]:
                max_index = k
                break
    print("#{} {}".format(i + 1, max_index))
