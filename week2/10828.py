arr = []


def push(n):
    return arr.append(n)

def pop():
    end = len(arr)
    remove_idx = -1
    if end <= 1 : return print(-1)
    else:
        arr[end-1] = -1
        newList = []
        for i in range(end-1):
            newList[i] = arr[i]

        arr.clear()

        for i in newList:
            arr.append(i)

        end -= 1
        return print(arr[end-1])

def size():
    print(len(arr))

def empty():
    if len(arr) == 0 : print(1)
    else : print(0)

def top():
    if len(arr) == 0 : print(-1)
    else:
        print(arr[len(arr)-1])

n = int(input())

for i in range(n):
    cmd = input().split()
    
    if cmd[0] == "push":
        push(i[1])
    elif cmd[0] == "pop":
        pop()
    elif cmd[0] == "size":
        size()
    elif cmd[0] == "empty":
        empty()
    elif cmd[0] == "top":
        top()
    