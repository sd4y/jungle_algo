import sys
from collections import deque

input = sys.stdin.readline

def solve():
    
    # 1. 입력 처리
    n, m, k, x = map(int, input().split())
    
    # 인접 리스트로 그래프 생성 (단방향)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 2. 거리 배열 초기화
    # -1은 아직 방문하지 않았음을 의미
    distance = [-1] * (n + 1)
    
    # 3. BFS 시작
    queue = deque([x])
    distance[x] = 0 # 시작 도시의 거리는 0

    # 4. 탐색 진행
    while queue:
        now = queue.popleft()
        
        # 현재 도시에서 이동할 수 있는 모든 도시 확인
        for next_node in graph[now]:
            # 아직 방문하지 않은 도시라면
            if distance[next_node] == -1:
                # 최단 거리 갱신
                distance[next_node] = distance[now] + 1
                queue.append(next_node)

    # 5. 결과 확인
    answer = []
    for i in range(1, n + 1):
        if distance[i] == k:
            answer.append(i)
            
    # 6. 출력
    if not answer:
        print(-1)
    else:
        # 오름차순으로 정렬할 필요 없이, 번호 순서대로 확인했으므로 바로 출력
        for city in answer:
            print(city)

solve()