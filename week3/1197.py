import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_sets(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve_mst(v, edges):
    parent = [i for i in range(v + 1)]
    total_cost = 0
    edge_count = 0
    for cost, a, b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_sets(parent, a, b)
            total_cost += cost
            edge_count += 1
            if edge_count == v - 1:
                break
    return total_cost

V, E = map(int, input().split())

edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = solve_mst(V, edges)

print(result)