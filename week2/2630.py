N = int(input())


Arr = []

for i in range(N):
    temp = list(map(int, input().split()))
    Arr.append(temp)

white = 0
blue = 0

def func(x, y , size):
        
        global white, blue

        current_color = Arr[x][y]

        for i in range(x, x+size):
              for j in range(y, y+size):
                    if Arr[i][j] != current_color:
                        half_size = size//2
                        func(x,y,half_size)
                        func(x,y+half_size,half_size)
                        func(x+half_size,y,half_size)
                        func(x+half_size,y+half_size,half_size)
                        return
        if current_color == 0:
              white += 1
        else : 
              blue += 1

func(0,0,N)

print(white)
print(blue)