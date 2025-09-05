N = int(input())

result = []

for i in range(N):
    result.append(list(map(str, input())))

for i in range(N):
    point = 1
    MyPoint = 0
    for j in range(len(result[i])):
        if result[i][j] == 'O' : 
            MyPoint += point
            point += 1
        else:
            point = 1
    print(MyPoint)
