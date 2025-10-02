import sys

sys.setrecursionlimit(10**6)

M, N = map(int, input().split())

board = [list(map (int, input().split())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N and 0 <= ny < M) and board[ny][nx] < board[y][x]:
            dp[y][x] += dfs(nx,ny)

    return dp[y][x]

print(dfs(0,0))