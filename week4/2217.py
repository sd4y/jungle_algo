# N = int(input())

# rope = [int(input()) for _ in range(N)]

# rope.sort()

# result = [0]*N

# for i in range(N):
#     result[i] = rope[i] * (N-i)

# result.sort()

# print(result[-1])

N = int(input())

data = [0] * 10001

for _ in range(N):
    data[int(input())] += 1

max_weight = 0
rope_count = 0

for strength in range(10000, 0, -1):
    if data[strength] > 0:
        rope_count += data[strength]
        max_weight = max(max_weight, strength * rope_count)

print(max_weight)