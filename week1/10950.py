T = int(input())

A = {}
B = {}

for i in range(T) : A[i],B[i] = map(int , input().split())

for i in range(T) : print(f"{A[i] + B[i]}")