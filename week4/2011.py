import sys

T = sys.stdin.readline().strip()

N = len(T)

dp = [0] * (N+1)


if T[0] == '0':
    print(0)
else:
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, N+1):
        current = int(T[i-1])

        if current > 0:
            dp[i] = (dp[i] + dp[i-1]) % 1000000
    
        two_num = int(T[i-2:i])

        if 10 <= two_num <= 26:
            dp[i] = (dp[i] + dp[i-2]) % 1000000

    print(dp[N])