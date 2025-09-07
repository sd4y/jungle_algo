import sys

N = int(sys.stdin.readline().rstrip())
result = 0

col = [False] * N
diag1 = [False] * (2*N-1)
diag2 = [False] * (2*N-1)

def dfs(row):
    global result
    if row == N:
        result += 1
        return
    for c in range(N):
        if not col[c] and not diag1[row+c] and not diag2[row-c+(N-1)]:
            col[c] = diag1[row+c] = diag2[row-c+(N-1)] = True
            dfs(row+1)
            col[c] = diag1[row+c] = diag2[row-c+(N-1)] = False

dfs(0)
print(result)