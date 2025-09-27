N = int(input())
Note = [int(input()) for _ in range(N)]

# dp = [0] * N 

# if Note[0] > 0:
#     dp[0] = Note[0]

# combo = 1

# for i in range(1, N):
#     dp[i] = dp[i-1] + (Note[i] * (combo + 1))
#     if dp[i] > dp[i-1]:
#         combo += 1
#     else:
#         combo = 1



# N = int(input())
# Note = [int(input()) for _ in range(N)]

# dp = [[0] * N for _ in range(N)] 

# if Note[0] > 0:
#     dp[0][0] = Note[0]

# combo = 1

# for i in range(1, N):
#     for j in range(1, N):
#         dp[i][j] = dp[i][j-1] + (Note[j] * (combo + 1))

#         if Note[i] < 0:
#             dp[i][j] = dp[i-1][j-1]
        

dp = [[[0] * (N+1)for _ in range(N+1)] for _ in range(3)]

def func(idx, combo, fail):
    if idx == N:
        return 0

    if dp[combo][fail][idx] != -float('inf'):
        return dp[combo][fail][idx]
    
    if fail == 2:
        dp[combo][fail][idx] = func(idx + 1, 1, 0)
        return dp[combo][fail][idx]

    dp[combo][fail][idx] = max(
        func(idx + 1, 0, fail + 1),
        func(idx +1, combo +1, 0) + Note[idx] * (combo + 1)
    )

    return dp[combo][fail][idx]