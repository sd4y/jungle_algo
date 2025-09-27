n, target = map(int, input().split())

tree = list(map(int, input().split()))

tree.sort()

result = 0

low = 0

high = tree[-1] // 2
while low <= high:
    total = 0
    mid = (low+high)//2

    for i in range(n-1, -1, -1):
        if tree[i] <= high:
            break
        
        total += (tree[i] - high)
    
    if total >= target:
        result = mid
        low = mid+1
    else:
        high = mid - 1

print(result)