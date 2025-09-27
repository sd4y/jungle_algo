from collections import deque

def bfs(graph, start_node):
    """너비 우선 탐색 (BFS) 함수"""
    # 1. 방문 기록을 위한 set과 탐색을 위한 큐(deque) 생성
    visited = set()
    queue = deque([start_node])
    
    # 2. 시작 노드를 방문 처리
    visited.add(start_node)
    
    path = [] # 탐색 경로를 저장할 리스트

    # 3. 큐가 빌 때까지 반복
    while queue:
        # 큐에서 노드를 하나 꺼냄 (가장 먼저 들어온 노드)
        node = queue.popleft()
        path.append(node)

        # 현재 노드와 연결된 모든 이웃 노드를 확인
        for neighbor in graph[node]:
            # 아직 방문하지 않은 이웃이라면
            if neighbor not in visited:
                # 방문 처리하고 큐에 추가
                visited.add(neighbor)
                queue.append(neighbor)
                
    return path