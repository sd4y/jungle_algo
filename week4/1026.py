S = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)
result = 0
for i in range(S):
    result += A[i] * B[S-1-i]

print(result)