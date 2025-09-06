T = int(input())

for j in range(T) : 
    data = input().split()
    R = int(data[0])
    S = str(data[1])
    
    for i in S:
        print(i * R, end="")
    print()