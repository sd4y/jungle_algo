import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve_with_final_rules():
    """
    사용자가 고안한 최종 규칙(홀/짝, 시작점, 지그재그)을 완벽하게 구현합니다.
    """
    N = 5
    Arr = [1, 2, 10, 11, 20]

    # 1. 배열을 오름차순으로 정렬합니다.
    Arr.sort()

    if N <= 1:
        print(0)
        return
        
    # 2. 결과와 이전 값을 저장할 변수 초기화
    result = 0
    last_num = 0
    
    # 3. 남은 숫자들을 관리할 deque 생성
    remaining_deque = deque(Arr)

    # 4. [핵심 규칙] N의 홀/짝 여부에 따라 시작점(last_num)을 결정합니다.
    if N % 2 == 0:
        # 짝수일 경우: 중간 그룹의 가장 작은 값(Rtemp[0])으로 시작
        # deque의 중간 인덱스를 찾아 해당 값을 pop합니다.
        mid_index = N // 2
        last_num = remaining_deque[mid_index]
        del remaining_deque[mid_index]
    else:
        # 홀수일 경우: 배열의 정중앙 값으로 시작
        mid_index = N // 2
        last_num = remaining_deque[mid_index]
        del remaining_deque[mid_index]

    # 5. [핵심 규칙] 남아있는 모든 숫자를 처리할 때까지 반복합니다.
    #    가장 작은 값(왼쪽 끝)과 가장 큰 값(오른쪽 끝)을 번갈아 선택합니다.
    while remaining_deque:
        # 가장 작은 값을 다음 수로 선택
        next_num = remaining_deque.popleft()
        result += abs(last_num - next_num)
        last_num = next_num

        # 아직 남은 수가 있다면, 가장 큰 값을 다음 수로 선택
        if remaining_deque:
            next_num = remaining_deque.pop()
            result += abs(last_num - next_num)
            last_num = next_num
            
    print(result)

# --- 메인 로직 ---
solve_with_final_rules()
