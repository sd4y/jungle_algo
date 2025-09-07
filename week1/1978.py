N = int(input())
N_list = list(map(int, input().split()))

result = 0

for num in N_list:
    if num < 2:
        continue
    is_prime = True
    i = 2
    while i*i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime: 
        result += 1

print(result)

