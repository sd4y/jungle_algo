X, Y = map(int, input().split())

N = int(input())

Xcut = [0]
Ycut = [0]

for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        Ycut.append(b)
    else:
        Xcut.append(b)

Xcut.append(X)
Ycut.append(Y)

Xcut.sort()
Ycut.sort()

xsize , ysize = 0, 0

for i in range(len(Xcut) -1):
    temp = Xcut[i+1] - Xcut[i]
    if xsize < temp:
        xsize = temp

for i in range(len(Ycut) - 1):
    temp = Ycut[i+1] - Ycut[i]
    if ysize < temp:
        ysize = temp
result = xsize * ysize
print(result)
# 0, Arr[a][i] .. , N 각 숫자의 차이