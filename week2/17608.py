n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

high = arr[n-1]
count = 1

for i in range(n-2, -1, -1):
    if arr[i] > high:
        count += 1

print(count)

    
