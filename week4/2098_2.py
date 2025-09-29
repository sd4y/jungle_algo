N = int(input())

W = [list(map(int, (input().split()))) for _ in range(N)]

dp = [[-1] * N for _ in range(N)] 

visited_list = [False] * N

INF = float('inf')

result = []


def visited_all(visited_list):
    for i in range(N):
        if visited_list[i] == True:
            count += 1
        return count == N

def TSP(current, visited):
    if visited_all(visited_list):
        if W[current][0]:
            return W[current][0]
        else:
            return INF
        
    if dp[current][visited] != -1:
        return dp[current][visited]
    
    min_cost = INF
    for next_city in range(N):
        if not visited[next_city] and W[current][next_city] != 0:
            visited_list[next_city] = True
            cost = W[current][next_city] + TSP(next_city, visited)
            min_cost = min(min_cost, cost)
    
    dp[current][visited] = min_cost
    return min_cost

for i in range(N):
    result.append(TSP(i, N))

print(min(result))