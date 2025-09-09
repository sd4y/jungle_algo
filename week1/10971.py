N = int(input())

W = []
for i in range(N):
    W.append(list(map(int, input().split())))

min_cost = 0

visited = [False] * N 

def func(start, current, cost, count):
    
    global min_cost

    if count == N:
        end_cost = cost + W[current][start]
        if W[current][start] != 0 :
            if end_cost < min_cost or min_cost == 0:  
                min_cost = end_cost        
        return

    for next_city in range(N):
        if visited[next_city] == False and W[current][next_city] != 0:
            visited[next_city] = True
            func(start, next_city, cost + W[current][next_city], count +1)
            visited[next_city] = False

for i in range(N):
    visited[i] = True
    func(i,i,0,1)
    visited[i] = False

print(min_cost)