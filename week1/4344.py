C = int(input())

for i in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    score = []
    for j in range(len(data) - 1):
        score.append(data[j+1])

    avg = sum(score) / N
    count = 0
    for k in score :
        if k > avg : count += 1

        rate = (count / N) * 100
    print(f"{rate:.3f}%")