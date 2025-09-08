def merge(arr, left, mid, right):
    Lsize = mid - left + 1
    Rsize = right - mid

    Ltemp = [0] * Lsize
    Rtemp = [0] * Rsize

    for i in range(Lsize):
        Ltemp[i] = arr[left + i]
    for i in range(Rsize):
        Rtemp[i] = arr[mid + 1 + i]

    L, R, P = 0, 0, left

    while L < Lsize and R < Rsize:
        if len(Ltemp[L]) < len(Rtemp[R]):
            arr[P] = Ltemp[L]
            L += 1
        elif len(Ltemp[L]) > len(Rtemp[R]):
            arr[P] = Rtemp[R]
            R += 1
        else:
            if Ltemp[L] < Rtemp[R]:
                arr[P] = Ltemp[L]
                L += 1
            else:
                arr[P] = Rtemp[R]
                R += 1
        P += 1

    while L < Lsize:
        arr[P] = Ltemp[L]
        P += 1
        L += 1

    while R < Rsize:
        arr[P] = Rtemp[R]
        P += 1
        R += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().strip()) 

unique_arr = list(set(arr))

merge_sort(unique_arr, 0, len(unique_arr) - 1)

for word in unique_arr:
    print(word)
