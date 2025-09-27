from collections import deque

def solve():
   
    # 1. 미로 정보 입력받기
    n, m = map(int, input().split())
    maze = [list(map(int, list(input()))) for _ in range(n)]

    # 2. 필요한 자료구조 생성
    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부를 기록할 2차원 리스트
    visited = [[False] * m for _ in range(n)]

    # 3. BFS 알고리즘 구현
    queue = deque([(0, 0, 1)])  # (x좌표, y좌표, 이동 거리)
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 목적지에 도달한 경우
        if x == n - 1 and y == m - 1:
            print(dist)
            break

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 공간을 벗어난 경우 무시
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            # 벽이거나 이미 방문한 경우 무시
            if maze[nx][ny] == 0 or visited[nx][ny]:
                continue
            
            # 해당 노드를 방문하고 큐에 삽입
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))

solve()