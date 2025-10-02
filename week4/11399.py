N = int(input())

Arr = list(map(int, input().split()))

Arr.sort()

result = 0

for i in range(N-1, -1, -1):
    result += Arr[N-i] * (i+1)

print(result)