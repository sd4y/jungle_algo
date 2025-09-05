A = int(input())
B = int(input())
C = int(input())

result = A*B*C

index = [0] * 10

while result > 0:
    value = result%10
    index[value] += 1
    result //= 10

for i in range(10):
    print(index[i])