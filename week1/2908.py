A, B = input().split()

Acount = len(A)
Bcount = len(B)

Arev = []
Brev = []

for i in range(Acount - 1, -1, -1):
    Arev.append(A[i])

for i in range(Bcount - 1, -1, -1):
    Brev.append(B[i])

resultA = int(''.join(Arev))
resultB = int(''.join(Brev))

if resultA > resultB : print(resultA)
elif resultA < resultB : print(resultB)
else : print(0)