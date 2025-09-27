
graph = {
    'A' :['B','C'],
    'B' :['D','E'],
    'C' :['F'],
    'D' :['G'],
    'E' :['G'],
    'G' :['H'],
    'H' :['F'],
}

def dfs(graph, start):
    visited = []
    back_edges = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(graph.get(node, []), reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
                else:
                    edge = tuple(sorted((node, neighbor)))
                    back_edges.add(edge)
    return visited, sorted(list(back_edges))


visited_path, non_tree_edges = dfs(graph, 'A')
print("방문 순서:", visited_path)
print("비트리 간선:", non_tree_edges)