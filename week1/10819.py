import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve_with_final_rules():
    """
    사용자가 고안한 최종 규칙(홀/짝 구분)을 완벽하게 구현합니다.
    """
    N = 5
    Arr = [1,2,3,101,102]

    # 1. 배열을 오름차순으로 정렬합니다.
    Arr.sort()

    if N <= 1:
        print(0)
        return
        
    # 2. 최종 순서를 담을 deque 생성
    final_sequence = deque()
    
    if N % 2 == 0:
        # N이 짝수인 경우의 규칙
        Ltemp = deque(Arr[:N//2])
        Rtemp = deque(Arr[N//2:])

        # 시작: Rtemp의 가장 왼쪽 값
        final_sequence.append(Rtemp.popleft())
        
        while Ltemp or Rtemp:
            # Ltemp의 가장 왼쪽 값
            if Ltemp:
                final_sequence.append(Ltemp.popleft())
            # Rtemp의 가장 오른쪽 값
            if Rtemp:
                final_sequence.append(Rtemp.pop())

    else:
        # N이 홀수인 경우의 규칙
        # 1. 중앙값 찾기
        mid_index = N // 2
        mid_value = Arr.pop(mid_index)
        final_sequence.append(mid_value)
        
        # 남은 배열로 deque 생성
        temp_deque = deque(Arr)

        # 2. 중앙값과 양 끝 값의 차이를 비교하여 다음 수 결정
        diff_with_left = abs(mid_value - temp_deque[0])
        diff_with_right = abs(mid_value - temp_deque[-1])

        if diff_with_right > diff_with_left:
            final_sequence.append(temp_deque.pop()) # 가장 큰 값
        else:
            final_sequence.append(temp_deque.popleft()) # 가장 작은 값
        
        # 3. 나머지 값들을 지그재그로 배치
        while temp_deque:
            final_sequence.append(temp_deque.popleft()) # 남은 것 중 가장 작은 값
            if temp_deque:
                final_sequence.append(temp_deque.pop()) # 남은 것 중 가장 큰 값

    # 최종적으로 인접한 값들의 차이의 합을 계산합니다.
    total_sum = 0
    for i in range(N - 1):
        total_sum += abs(final_sequence[i] - final_sequence[i+1])
        
    print(total_sum)


# --- 메인 로직 ---
solve_with_final_rules()
        