import sys

input = sys.stdin.readline

Arr = [0] * 10001

N = int(input())

for i in range(N):
    num = int(input())
    Arr[num] += 1

index = 0
while index < len(Arr):
    if Arr[index] > 0:
        for i in range(Arr[index]):
            print(index)
    index += 1