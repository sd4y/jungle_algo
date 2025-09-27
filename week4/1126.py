

# 1. 두 탑의 높이가 같아야 한다.

# (1)을 만족하는 경우 가장 높은 탑의 높이를 구해라

N = int(input())
Arr = [int(input()) for _ in range(N)]

dp = [[[-1] * 50 for _ in range(250000)]for _ in range(250000)]

def func(idx, Atop, Btop):

    #1 예외 처리1
    if idx == N:
        if Atop == Btop:
            return Atop
        else:
            return -1

    #2 예외 처리2
    if dp[idx][Atop][Btop] != -1:
        return dp[idx][Atop][Btop]

    #3 점화식
    dp[idx][Atop][Btop] = max(
        func(idx + 1, Atop + Arr[idx], Btop),
        func(idx + 1, Atop, Btop + Arr[idx]),
        func(idx + 1, Atop, Btop)
    )

    return dp[idx][Atop][Btop]