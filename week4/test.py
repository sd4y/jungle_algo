N = int(input())
String = input()

Integers = []
Operators = []
int_string = ""

# 데이터 입력 받기
for char in String:
    try:
        int(char)
        int_string += char
    except ValueError:
        Integers.append(int(int_string))
        int_string = ""
        Operators.append(char)

if int_string:
    Integers.append(int(int_string))

count = len(Integers)

dp = [[None] * N for _ in range(N)]

def math(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b

# start ~ end 까지의 연산 결과 중 최소, 최댓값 반환
def func(start, end):
    # 마지막 숫자
    if start == end:
        num = Integers[start]
        return (num, str(num), num, str(num))
    
    # start~end 까지 연산 한 적 있는 경우
    if dp[start][end] is not None:
        return dp[start][end]
    
    min_result = float('inf')
    max_result = float('-inf')

    min_result_str = ""
    max_result_str = ""

    # start ~ end 사이 모든 연산 가능한 경우의 수 반복문 돌며 재귀
    for i in range(start, end):
        op = Operators[i]
        min_l, min_str_l, max_l, max_str_l = func(start, i)
        min_r, min_str_r, max_r, max_str_r = func(i + 1, end)

        #struct 용도 (최솟값, 최댓값을 int, string 형태로 보관)
        Data = [ 
            (min_l, min_str_l, min_r, min_str_r),
            (min_l, min_str_l, max_r, max_str_r),
            (max_l, max_str_l, min_r, min_str_r),
            (max_l, max_str_l, max_r, max_str_r),
            ]
        
        # struct Data 데이터 math 함수 이용해서 연산 + print할 "(내용)" 저장
        for iLeft, sLeft, iRight, sRight in Data: 
            current_math_val = math(iLeft, op, iRight)
            current_math_str = f"({sLeft}{op}{sRight})"

            if current_math_val > max_result:
                max_result = current_math_val
                max_result_str = current_math_str

            if current_math_val < min_result:
                min_result = current_math_val
                min_result_str = current_math_str

    dp[start][end] = (min_result, min_result_str, max_result, max_result_str)
    return dp[start][end]

A, B, C, D = func(0,count - 1)
print(C)
print(D)