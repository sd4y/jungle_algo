from collections import deque

N, M, V = map(int, input().split())

graph = [set() for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
    
sorted_graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    sorted_graph[i] = sorted(list(graph[i]))

def dfs(graph, start_node):

    visited = set()
    path = []

    def _dfs_recursive(node):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                _dfs_recursive(neighbor)

    _dfs_recursive(start_node)
    return path

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    
    visited.add(start_node)
    
    path = [] 

    while queue:
        node = queue.popleft()
        path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return path

result = dfs(sorted_graph, V)
print(*result)
result = bfs(sorted_graph, V)
print(*result)
