N, X = map(int, input().split())

Li = list(map(int, input().split()))

for i in range(len(Li)):
    if Li[i] < X : print(Li[i], end=" ")