A = int(input())
B = int(input())

b_1 = B%10
b_10 = (B%100 - b_1)//10
b_100 = B//100

print(A*b_1)
print(A*b_10)
print(A*b_100)
print(A*B)