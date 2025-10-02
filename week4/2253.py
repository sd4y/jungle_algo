import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

small_stones = set()

for _ in range(M):
    small_stones.add(int(input()))
    
max_speed = int((2 * N) ** 0.5) + 2

dp = [[-1] * max_speed for _ in range(N + 1)]

INF = float('inf')

if 2 not in small_stones:
    dp[2][1] = 1

def func(stone, jump_power):
    
    if stone > N:
        return INF
    
    if stone == N:
        return 0
    
    if dp[stone][jump_power] != -1:
        return dp[stone][jump_power]
    
    min_jumps = INF

    for jump_offset in [-1, 0, 1]:
        next_power = jump_power + jump_offset
    
        if next_power > 0:
            next_stone = stone + next_power

            if next_stone not in small_stones:
                result = func(next_stone, next_power)

                if result != INF:
                    min_jumps = min(min_jumps, result + 1)

    dp[stone][jump_power] = min_jumps
    return min_jumps

if N == 1:
    print(0)
else:
    answer = func(1, 0)

    if answer == INF:
        print(-1)
    else:
        print(answer)

