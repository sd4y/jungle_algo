N = int(input())

is_False = True

for i in range(0, N, 3):
    Next = N - i
    result = i // 3
    if Next == 0:
        is_False = False
        print(result)
        break

    if Next % 5 == 0:
        is_False = False
        result += Next // 5
        print(result)
        break
        
if is_False == True:
    print(-1)