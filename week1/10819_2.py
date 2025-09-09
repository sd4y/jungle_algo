# 입력 받기
n = 7
numbers = [3, 13, 20, 1, 26, 30, 17]

# 정렬
numbers.sort()

# 차이의 합 계산
ans = 0
mid = n // 2

# 절반씩 번갈아 계산
for i in range(mid):
    ans += numbers[n - i - 1] - numbers[i]

# 총합의 두 배
ans *= 2

# 중앙 값 처리 (홀수/짝수 구분)
if n % 2 == 1:
    ans -= min(numbers[mid] - numbers[mid - 1], numbers[mid + 1] - numbers[mid])
else:
    ans -= numbers[mid] - numbers[mid - 1]

# 결과 출력
print(ans)