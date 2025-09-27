N = int(input())

def move_snake(snake, direction, time):

    time += 1
    
    direct_x = [-1, 0, 1, 0]
    direct_y = [0, 1, 0, -1]

    snake_x, snake_y = snake
    next_x, next_y = direct_x[direction], direct_y[direction]

    if not (0 <= next_x < N and 0 <= next_y < N) :
        return -1
    
    
    
