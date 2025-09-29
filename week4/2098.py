N = int(input())

W = [list(map(int, (input().split()))) for _ in range(N)]

dp = [[-1] * (1<<N) for _ in range(N)] 

INF = float('inf') 

def TSP(current, visited_mask):
    
    if visited_mask == (1 << N) - 1: 
        if W[current][0] != 0: 
            return W[current][0]
        else:
            return INF 

    if dp[current][visited_mask] != -1:
        return dp[current][visited_mask]

    min_cost = INF
    for next_city in range(N):
        if not (visited_mask & (1 << next_city)) and W[current][next_city] != 0:
            cost = W[current][next_city] + TSP(next_city, visited_mask | (1 << next_city))
            min_cost = min(min_cost, cost)

    dp[current][visited_mask] = min_cost
    return min_cost

print(TSP(0, 1)) 