arr = []

for i in range(9):
    arr.append(input())
    sum_all += arr[i]

sum_target = sum_all - 100

is_end = False

for i in range(9):
    for j in range(i+1, 9):
        if arr[i] + arr[j] == sum_target:
            targetA, targetB = arr[i], arr[j]
            arr.remove(targetA)
            arr.remove(targetB)
            arr.sort()
            for k in arr:
                print(k)
            is_end = True
            break    
    if is_end == True:
        break    