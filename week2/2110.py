N, C = map(int, input().split())

Arr = [int(input()) for _ in range(N)]

Arr.sort()

start = 1
end = Arr[len(Arr)-1] - Arr[0]

result = 0

while start <= end:
    mid = (start + end)//2

    pos = Arr[0]

    count = 1

    for i in range(1, N):
        if Arr[i] >= pos + mid:
            count += 1
            pos = Arr[i]

    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid -1    

print(result)

