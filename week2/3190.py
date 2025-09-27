from collections import deque

N = int(input())    # 보드 크기
K = int(input())    # 사과 개수

Board = [[False] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    Board[r-1][c-1] = True

L = int(input()) # 방향 변환 횟수

moves = {} # 방향 변환 정보

for i in range(L):
    a, b = list(input().split())
    moves[int(a)] = b

snake = deque([(0,0)]) # 뱀의 위치
direction = 1          # 방향
time = 0

direcX = [-1, 0, 1, 0]
direcY = [0, 1, 0, -1]

while True:

    time += 1

    # 현재 뱀 머리 좌표
    head_x, head_y = snake[0]
    # 현재 방향으로 한 칸 이동한 다음 머리 좌표
    next_x, next_y = head_x + direcX[direction], head_y + direcY[direction]

    # 벽 체크
    if not (0 <= next_x < N and 0 <= next_y < N) :
        break

    # 내몸 체크
    if (next_x, next_y) in snake:
        break

    # 뱀 머리를 다음 칸으로 이동
    snake.appendleft((next_x, next_y))

    if Board[next_x][next_y] == True: # 이동한 칸에 사과가 있다면
        Board[next_x][next_y] = False # 몸길이 증가
    else :
        snake.pop() #꼬리 제거 

# 현재 시간이 방향 전환 시간과 일치하는지 확인
    if time in moves:
        if moves[time] == "L":   # 왼쪽
            direction = (direction - 1 + 4) % 4
        else:                    # 오른쪽      
            direction = (direction + 1) % 4

print(time)