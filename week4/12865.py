# N, K = map(int, input().split())

# Items = [tuple(map(int, input().split())) for _ in range(N)]

# dp = [0] * (K + 1)

# for weight, value in Items:
#     for i in range(K, weight - 1, -1):
#         if dp[i - weight] + value > dp[i]:
#             dp[i] = dp[i - weight] + value
    
# dp.sort()
# print(dp[-1])

#--------------------------------------------
    
# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# N, K = map(int, input().split())
# Items = [tuple(map(int, input().split())) for _ in range(N)]
# dp = [[-1] * (K + 1) for _ in range(N)]

# def knapsack_recursive(item_idx, k):
    
#     if item_idx == N:
#         return 0
    
#     if dp[item_idx][k] != -1:
#         return dp[item_idx][k]
    
#     weight, value = Items[item_idx]
    
#     value_if_not_packed = knapsack_recursive(item_idx + 1, k)

#     if k - weight >= 0:
#         value_if_packed = value + knapsack_recursive(item_idx + 1, k - weight)
#     else:
#         value_if_packed = -1 

#     dp[item_idx][k] = max(value_if_not_packed, value_if_packed)
    
#     return dp[item_idx][k]

# result = knapsack_recursive(0, K)
# print(result)

#--------------------------------------------------------

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    items.append(tuple(map(int, input().split())))

prev_dp = [0] * (K + 1)
current_dp = [0] * (K + 1)

for weight, value in items:
    for w in range(1, K + 1):
        if weight > w:
            current_dp[w] = prev_dp[w]
        else:
            current_dp[w] = max(prev_dp[w], value + prev_dp[w - weight])
    prev_dp = current_dp[:]
print(prev_dp[K])