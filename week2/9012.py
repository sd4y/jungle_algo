n = int(input())

for i in range(n):
    arr = list(input())
    count = 0
    is_break = False
    for j in range(len(arr)):
        if arr[j] == '(':
            count += 1
        else : count -= 1

        if count < 0 :
            print("NO")
            is_break = True
            break
    if count == 0:
        print("YES")
    elif is_break == False :
        print("NO")

