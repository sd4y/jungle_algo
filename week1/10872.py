N = int(input())

def func(N):
    if N == 0 : return 1
    return func(N-1) * N

print(func(N))