N = int(input())

board = [[" "]*N for i in range(N)]

def func(N, _x, _y):

    if N == 1:
        board[_x][_y] = "*"
        return
    
    key = N//3
    
    for i in range(3):
        for j in range(3):
            if not(i == 1 and j == 1) :
                x = _x + i * key
                y = _y + j * key
                func(key, x, y)

func(N, 0, 0)

for i in board:
    print("".join(i))

