S = input()

count_0 = 0
count_1 = 0
prev = -1

for char in S:
    if prev is not char:
        prev = char
        if prev is not '0':
            count_1 += 1
        else:
            count_0 += 1
    
if count_1 > count_0:
    print(count_1)
else:
    print(count_0)
