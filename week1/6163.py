N = []
M = []

for i in range(9):
    N.append(int(input()))

M = N.copy()

N.sort()

print(N[8])

for i in range(9):
    if N[8] == M[i] : 
        print(i + 1)
        break




    
