from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)

queue = deque([1])
parent[1] = 1

while queue:
    current = queue.popleft()

    for next_node in graph[current]:
        if parent[next_node] == 0:
            parent[next_node] = current
            queue.append(next_node)

for i in range(2, n+1):
    print(parent[i])
