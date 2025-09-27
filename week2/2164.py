N = 6

arr = []

for i in range(1, N+1):
    arr.append(i)

idx = 0

while idx < N:
    if not idx % 2 == 0 :
        arr.append(arr[idx])
        N += 1
    idx += 1

print(arr[-1])