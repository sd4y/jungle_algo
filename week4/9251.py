str_A = input()
str_B = input()

ASize = len(str_A)
BSize = len(str_B)

dp = [[0] * (BSize + 1) for _ in range(ASize + 1)]

# for i in range(1, ASize+ 1):
#     for j in range(1, BSize + 1):
#         if str_A[i-1] == str_B[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp[ASize][BSize])

def func(i, j):
    if i < 0 or j < 0 :
        return 0

    if dp[i][j] != -float('inf'):
        return dp[i][j]
    
    if str_A[i] == str_B[j]:
        dp[i][j] = func(i-1, j-1) + 1
        return dp[i][j]

    dp[i][j] = max(
        func(i-1, j),
        func(i, j-1)
    )

    return dp[i][j]
