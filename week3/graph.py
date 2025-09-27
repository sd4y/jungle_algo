from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(set)

    def add_edge(self, u, v):
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)

    def __str__(self):
        output = ""
        for key, value in self.adj_list.items():
            output += f"Node {key}: {list(value)}\n"
        return output

    def bfs(self, start_node):
        if start_node not in self.adj_list:
            print("Error: 시작 노드가 그래프에 없습니다.")
            return []

        # 1. 방문 기록을 위한 set과 탐색을 위한 큐(deque) 생성
        visited = set()
        queue = deque([start_node])
        
        # 2. 시작 노드를 방문 처리
        visited.add(start_node)
        
        path = [] # 탐색 경로

        # 3. 큐가 빌 때까지 반복
        while queue:
            node = queue.popleft()
            path.append(node)

            for neighbor in self.adj_list[node]:
                # 4. 아직 방문하지 않은 이웃이라면 방문 처리하고 큐에 추가
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return path

    def dfs(self, start_node):
        if start_node not in self.adj_list:
            print("Error: 시작 노드가 그래프에 없습니다.")
            return []
            
        visited = set() # 방문 기록
        path = []       # 탐색 경로

        # 재귀 함수 정의
        def _dfs_recursive(node):
            # 1. 현재 노드를 방문 처리
            visited.add(node)
            path.append(node)

            # 2. 현재 노드의 이웃들을 탐색
            for neighbor in self.adj_list[node]:
                # 3. 아직 방문하지 않은 이웃이라면 재귀 호출
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        # 시작 노드부터 재귀 탐색 시작
        _dfs_recursive(start_node)
        return path
    
    