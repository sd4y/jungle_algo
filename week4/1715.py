import sys
import heapq

input = sys.stdin.readline

N = int(input())
Cards = []
for _ in range(N):
    heapq.heappush(Cards, int(input()))

TotalCount = 0
while len(Cards) > 1:
    deckA = heapq.heappop(Cards)
    deckB = heapq.heappop(Cards)

    currentCount = deckA + deckB
    TotalCount += currentCount
    heapq.heappush(Cards, currentCount)

print(TotalCount)