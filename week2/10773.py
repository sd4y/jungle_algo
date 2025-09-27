K = int(input())

arr = []

result = 0
count = 0

for i in range(K):
    arr.append(int(input()))


for i in range(K-1, -1, -1):
    if arr[i] == 0:
        count += 1
    elif not count == 0 :
        count -= 1
    else :
        result += arr[i]

print(result)
