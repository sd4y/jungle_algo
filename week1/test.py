""" print("Hello World")

result = []

result.append(A+B)
result.append(A-B)
result.append(A*B)
result.append(A/B)
result.append(A%B)

for i in result:
    print(i) """

# ----------------------------
""" result = []
numA = 472
numB = "385"
count = len(numB)

for i in range(count):
    result.append(int(numB[count - i - 1]) * numA)

for i in range(count):
    print(result[i])

print(int(numB)*numA) """

#----------------------------

""" N = int(input())

if 100 >= N >= 90:
    print("A")
elif 89 >= N >= 80:
    print("B")
elif 79 >= N >= 70:
    print("C")
elif 69 >= N >= 60:
    print("D")
else:
    print("F")
 """

#--------------------------------------


""" def is_4x(num):
    if num % 4 == 0 : return True
    else : return False

def is_not_100x(num):
    if num % 100 == 0 : return False
    else : return True

def is_400x(num):
    if num % 400 == 0: return True
    else : return False

N = int(input())

if is_400x(N) : print(1)
elif is_not_100x(N) and is_4x(N): print(1)
else : print(0) """

#-----------------------------------------

""" x, y, w, h = map(int, input().split())

xlen = w - x
ylen = h - y

if x <= xlen and x <= y and x <= ylen: print(x)
elif xlen < x and xlen < y and xlen < ylen : print(xlen)
elif y < ylen and y < x and y < ylen : print(y)
else : print(ylen) """

#---------------------------------------

""" N = int(input())

for i in range(1, 10):
    result = N*i
    print(f"{N} * {i} = {result}") """

#---------------------------------------

""" N = int(input())

for i in range(N):
    a,b = map(int, input().split())
    print(f"{a+b}") """

#----------------------------------------

""" N = int(input())

for i in range(N): 
    for j in range(i + 1):
        print("*", end="")
    print() """

#---------------------------------------

""" N, X = map(int, input().split())

A = list(map(int, input().split()))

for i in A:
    if i < X : print(i) """

#-------------------------------------------

""" N = []

for i in range(9):
    N.append(int(input()))

temp = N[0]
index = 0

for i in range(8):
    if temp < N[i+1] : 
        temp = N[i+1]
        index = i+1

print(temp)
print(index+1)  """

#----------------------리스트에 --------------------

""" N = int(input())

T = []

for i in range(N):
    T.append(input())
             
for i in range(N):
    result = 0
    point = 0
    for j in range(len(T[i])):
        if T[i][j] == "O" :
            point += 1
            result += point
        else:
            point = 0
    print(result) """

#-----------------자르고 일괄 int 변경 후 리스트---------------------

""" C = int(input())

N = []

for i in range(C):
    T = list(map(int, input().split()))  ## 자른 다음 일관 int로 바꾸려면 map?
    N.append(T)


for i in range(C):
    arg = 0
    count = 0
    students = N[i][0]
    for j in range(1, students+1):
        arg += N[i][j]
    arg /= (students)
    
    for k in range(1, students+1):
        if N[i][k] > arg :
            count += 1
    
    print(f"{count / students * 100 :.3f}%") """

#---------------------------------------

""" A = int(input())
B = int(input())
C = int(input())

Arr = [0] * 10

result = str(A*B*C)

for i in range(len(result)) :
    num = int(result[i])
    for j in  range(10):
        if num == j:
            Arr[j] += 1

for i in range(10):
    print(Arr[i]) """

#------------------------------------------

""" def solve(a: list) -> int:
    result = 0
    for i in range(len(a)):
        result += a[i]
    return result """

#--------------------아스키--------------------
""" 
print(ord(input()))

 """
#----------------------------------------

""" arr = list(input().split())
print(len(arr)) """

#-------------------숫자 뒤집기--------------------

""" A, B = input().split()

re_A = "" 
re_B = ""

for i in range(2, -1, -1):
    re_A += A[i]
    re_B += B[i]

re_A = int(re_A)
re_B = int(re_B)

if re_A > re_B : 
    print(re_A)
else:
    print(re_B) """

#------------------퀵정렬----------------------
""" def quick (arr, left, right):
    low = left
    high = right
    pivot = arr[(left+right)//2]

    while low <= high:
        while low <= high and arr[low] <= pivot :
            low += 1
        while high >= low and arr[high] >= pivot:
            high -= 1

        if low <= high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp

    return high

def partition(arr, left, right):
    if left < right :
        pivot = quick(arr, left, right)

        partition(arr, left, pivot-1)
        partition(arr, pivot+1, right)

def quick_sort(arr :list):
    partition(arr, 0, len(arr) - 1)

Arr = [5,4,7,6,9,1,2,3] """

#--------------------------------------------------

def Quick_sort(arr, left, right):
    if(right > left):
        pivot = partition(arr, left, right)

        Quick_sort(arr, left, pivot - 1)
        Quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    pivot = arr[(right+left)//2]
    L = left
    R = right

    while L <= R:
        while L <= R and arr[L] < pivot:
            L += 1
        while L >= R and arr[R] > pivot:
            R -= 1

        if L < R:
            temp = arr[L]
            arr[L] = arr[R]
            arr[R] = temp
            L += 1
            R += 1

    return R

