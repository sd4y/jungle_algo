N = int(input())
arr_N = list(map(int, input().split()))
M = int(input())
arr_M = list(map(int, input().split()))

arr_N.sort()

for i in range(M):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end)//2
        if arr_N[mid] == arr_M[i]:
            print(1)
            break
        elif arr_N[mid] < arr_M[i]:
            start = mid+1
        else:
            end = mid-1

    if arr_N[mid] != arr_M[i]:
        print(0)