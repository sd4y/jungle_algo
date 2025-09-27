# 행렬을 곱하는데 필요한 곱셈 연산의 최솟값

import sys
input = sys.stdin.readline

N = int(input())
Arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')] * N for _ in range(N)]

def func(start, end):

    if dp[start][end] != float('inf'):
        return dp[start][end]  
    
    if start == end:
        return 0
    
    if start+1 == end:
        cost = Arr[start][0] * Arr[start][1] * Arr[end][1]
        dp[start][end] = cost
        return cost

    min_cost = float('inf')

    for i in range(start, end):
        cost = func(start, i) + func(i+1, end) + (Arr[start][0] * Arr[i][1] * Arr[end][1])
        min_cost = min(min_cost, cost)

    dp[start][end] = min_cost
    return min_cost

print(func(0, N-1))