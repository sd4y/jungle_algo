n = int(input())

arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n - 1

answer = 1000000000

answer_a = 0
answer_b = 0

temp_a = arr[start] + arr[end]

while start < end :

    if arr[0] > 0 :
        print(arr[0], arr[1])
        break

    if arr[n-1] < 0 :
        print(arr[n-2], arr[n-1])
        break

    current_sum = arr[start] + arr[end]

    if abs(current_sum) < answer:
        answer = abs(current_sum)
        answer_a = arr[start]
        answer_b = arr[end]

    if current_sum == 0:
        break
    elif current_sum < 0:
        start += 1
    else:
        end -= 1

print(answer_a, answer_b)
        