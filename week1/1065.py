N = input()

N_int = int(N)

count = 0

if N_int < 100 :
    print(N_int)
else:
    count = 99
    for i in range(100, N_int+1):
        I_str = str(i)
        a = int(I_str[0])
        b = int(I_str[1])
        c = int(I_str[2])

        if a - b == b - c :
            count += 1
    print(count)