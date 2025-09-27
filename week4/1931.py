N = int(input())
Arr = []
for i in range(N):
    a, b = map(int, (input().split()))
    Arr.append([b, a])

Arr.sort()

target = Arr[0][0]
count = 1

for i in range(1, N):
    if target <= Arr[i][1]:
        count += 1
        target = Arr[i][0]

print(count)

