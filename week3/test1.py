from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
  
    queue = deque([(start_node, [start_node])]) 
    visited = {start_node}

    while queue:
        current_node, path = queue.popleft()

        if current_node == end_node:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

cities_graph = {
    '서울': ['천안', '원주'],
    '천안': ['서울', '대전', '광주'],
    '원주': ['서울', '강릉', '대구'],
    '대전': ['천안', '대구'],
    '광주': ['천안', '부산'],
    '대구': ['원주', '대전', '부산'],
    '강릉': ['원주'],
    '부산': ['광주', '대구']
}

# --- 코드 실행 ---
if __name__ == "__main__":
    start_city = '서울'
    end_city = '부산'

    shortest_path = bfs_shortest_path(cities_graph, start_city, end_city)

    if shortest_path:
        print(f"'{start_city}'에서 '{end_city}'까지의 최단 경로 (최소 경유):")
        # ' -> '.join(리스트)는 리스트의 요소들을 화살표로 연결해줌
        print(" -> ".join(shortest_path))
        print(f"총 경유 도시 수: {len(shortest_path) - 1}개")
    else:
        print(f"'{start_city}'에서 '{end_city}'까지 가는 경로를 찾을 수 없습니다.")