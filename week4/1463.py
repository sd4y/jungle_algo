import sys

T = int(sys.stdin.readline())

N = [int(sys.stdin.readline())for _ in range(T)]

dp = [0, 0] * (T + 1)

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, T+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for j in range(T):
    print(dp[N[j]][0], dp[N[j]][1])