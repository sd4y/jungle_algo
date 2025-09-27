N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def serch(start, end, arr, target): 

    if start > end:
        return 0
    
    mid = (start+end)//2
    
    if arr[mid] == target:
        return 1
    elif arr[mid] > target:
        return serch(start, mid-1, arr, target)
    else :
        return serch(mid+1, end, arr, target)
    

for i in range(M):
    result = serch(0,N-1, A, B[i])
    if result == 1 :
        print(1)
    else:
        print(0)