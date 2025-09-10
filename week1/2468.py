N = int(input())

area = []

for i in range(N):
    area.append(list(map(int, input().split())))

result = 1

def func(x, y, h, visited, area, n): #경계선 찾는 함수 (안전 영역의 범위 알기 위한)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = True     #방문 표시

    for i in range(4):       #상,하,좌,우 각 한칸씩 확인해보기
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n and not visited[nx][ny] and area[nx][ny] > h: #보드 내부인지 체크
            func(nx,ny,h,visited,area,n)                                                           #방문한적 있는지 체크
                                                                                                   #물에 잠기지 않았는지 체크

for h in range(1, 101):      #물 높이 1부터 100까지 Loop
    visited = [[False]*N]*N  #물 높이 별로 보드 초기화 (돌면서 물에 잠기지 않은 영역 찾으면 활성화 하기 위해) + 물 높이가 달라지면 잠기는 영역이 바뀌기 때문에
    zones = 0                #물 높이 별로 안전구역이 총 몇개인지 저장할 임시 변수 (최종 값이랑 비교해서 더 크면 result에 넣기) 

    for x in range(N):
        for y in range(N):
            if not visited[x][y] and area[x][y] > h: # 내가 방문한 적 없고 물 높이보다 높은 영역이라면 Do
                zones += 1                           # 안전구역 발견했으니까 일단 1개 증가 이후에 해당 구역의 경계 찾아 어디까지가 한 덩어리 인지 확인하는 작업필요
                func(x, y, h, visited, area, N)      # 구역의 경계 찾기
            
    if result < zones : result = zones
print(result)