T = int(input())

Arr = []

for i in range(T):
    Arr.append(int(input()))

Data = [True] * 10001
Data[0] = Data[1] = [False]

for i in range(2, 10001):
    if Data[i] == True :
        for j in range(i*2, 10001, i):
            Data[j] = False

for i in range(T) :
    a = b = Arr[i] // 2
    
    while True:
        if Data[a] == True and Data[b] == True:
            print(a, b)
            break
        else:
            a -= 1
            b += 1