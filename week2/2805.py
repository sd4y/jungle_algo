import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

#재귀 ver
def func(arr, start, end, goal):
    if start > end : return
    global answer
    mid = (start+end)//2
    total_wood = 0
    for i in range(len(arr)-1, -1, -1):
        temp = arr[i] - mid 
        if temp <= 0 : break
        total_wood += temp

    if total_wood >= goal:
        answer = mid
        func(arr, mid+1, end, goal)
    else:
        func(arr, start, mid-1, goal)

#while ver
def func2(arr, target, size):
    low = 0
    high = arr[size - 1]
    result = 0
    
    while low <= high:
        mid = (low + high)//2
        total = 0
        for i in range(size-1, -1, -1):
            temp = arr[i] - mid
            if temp <= 0 : break
            total += temp
            
        if total >= target:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


arr.sort()
answer = 0
func(arr, 0, arr[N-1], M)
print(answer)