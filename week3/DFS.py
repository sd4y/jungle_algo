def dfs(graph, start_node):
    """깊이 우선 탐색 (DFS) 함수 - 재귀 방식"""
    # 1. 방문 기록을 위한 set과 탐색 경로를 저장할 리스트 생성
    visited = set()
    path = []

    # 2. 실제 재귀 로직을 수행할 내부 함수 호출
    def _dfs_recursive(node):
        # 현재 노드를 방문 처리
        visited.add(node)
        path.append(node)

        # 현재 노드와 연결된 모든 이웃 노드를 확인
        for neighbor in graph[node]:
            # 아직 방문하지 않은 이웃이라면 재귀 호출
            if neighbor not in visited:
                _dfs_recursive(neighbor)

    _dfs_recursive(start_node)
    return path
