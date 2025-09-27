N, M = map(int, input().split())

from collections import deque

arr = deque(range(1, N+1))

result = []

while arr:
    for _ in range(M - 1):
        arr.append(arr.popleft())
    result.append(arr.popleft())

print("<" + ", ".join(map(str, result)) + ">")