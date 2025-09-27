import sys
sys.setrecursionlimit(10000)  
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(vertex):
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

components = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        components += 1

print(components)
