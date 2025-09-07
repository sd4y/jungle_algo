

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
        if Ltemp[L] <= Rtemp[R]:
            arr[P] = Ltemp[L]
            P += 1
            L += 1
        else:
            arr[P] = Rtemp[R]
            P += 1
            R += 1

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


def bubble_sort(arr, size):
    while size > 0:
        count = 0
        while count < size - 1:
            if arr[count] > arr[count + 1]:
                temp = arr[count]
                arr[count] = arr[count + 1]
                arr[count + 1] = temp
            count += 1
        size -= 1
    return arr

def partition(arr, left, right):
    pivot = arr[(left+right)//2]
    low = left + 1
    high = right

    while(low <= high):
        while(low <= right and arr[low] <= pivot):
            low += 1
        while(high > left and arr[high] > pivot):
            high -= 1

        if low < high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp

    return high

def quick_sort(arr, left, right):
    if(left < right):
        mid = partition(arr, left, right)

        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid +1, right)


N = int(input())
Arr = []

for i in range(N):
    Arr.append(int(input()))

quick_sort(Arr, 0, N-1)


