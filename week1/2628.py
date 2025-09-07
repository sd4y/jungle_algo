x_size,y_size = map(int, input().split())
count = int(input())

cut_x = [0,x_size]
cut_y = [0,y_size]

for i in range(count):
    direct, pos = map(int, input().split())
    if direct == 0:
        cut_y.append(pos)
    else:
        cut_x.append(pos)

cut_x.sort()
cut_y.sort()

max_x = 0
for i in range(len(cut_x) - 1):
    diff = cut_x[i+1] - cut_x[i]
    if diff > max_x:
        max_x = diff

max_y = 0
for i in range(len(cut_y) -1):
    diff = cut_y[i+1] - cut_y[i]
    if diff > max_y:
        max_y = diff 


print(max_x*max_y)
        