import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve_with_final_rules():
    """
    사용자가 고안한 최종 규칙(홀/짝, 시작점, 경로 선택)을 완벽하게 구현합니다.
    """
    N = 7
    Arr = [30, 29, 4, 9, 24, 7, 22]

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
        
        # 반복: Ltemp의 가장 작은 값과 Rtemp의 가장 큰 값을 번갈아 배치
        while Ltemp or Rtemp:
            if Ltemp:
                final_sequence.append(Ltemp.popleft())
            if Rtemp:
                final_sequence.append(Rtemp.pop())

    else:
        # N이 홀수인 경우의 규칙
        mid_index = N // 2
        Ltemp = deque(Arr[:mid_index])
        mid_value = Arr[mid_index]
        Rtemp = deque(Arr[mid_index + 1:])

        # [핵심 규칙] 단 한 번의 비교로 전체 경로를 결정
        diff_with_left_neighbor = abs(mid_value - Ltemp[-1])
        diff_with_right_neighbor = abs(Rtemp[0] - mid_value)

        final_sequence.append(mid_value)

        if diff_with_left_neighbor > diff_with_right_neighbor:
            # 경로 1: [Mid, L_max, R_max, L_min, R_mid, L_mid, R_min] 패턴
            final_sequence.append(Ltemp.pop()) # L_max
            while Ltemp or Rtemp:
                if Rtemp: final_sequence.append(Rtemp.pop())     # R_max
                if Ltemp: final_sequence.append(Ltemp.popleft()) # L_min
                if Rtemp: final_sequence.append(Rtemp.pop())     # R_penultimate
                if Ltemp: final_sequence.append(Ltemp.pop())     # L_penultimate
                if Rtemp: final_sequence.append(Rtemp.popleft()) # R_min

        else: # 차이가 같거나 오른쪽이 더 큰 경우
            # 경로 2: [Mid, R_max, L_min, R_min, L_max, ...] 패턴
            final_sequence.append(Rtemp.pop()) # R_max
            while Ltemp or Rtemp:
                if Ltemp: final_sequence.append(Ltemp.popleft()) # L_min
                if Rtemp: final_sequence.append(Rtemp.popleft()) # R_min
                if Ltemp: final_sequence.append(Ltemp.pop())     # L_max

    # 최종적으로 인접한 값들의 차이의 합을 계산합니다.
    # deque를 list로 변환하여 인덱싱
    final_list = list(final_sequence)
    total_sum = 0
    for i in range(N - 1):
        total_sum += abs(final_list[i] - final_list[i+1])
        
    print(total_sum)


# --- 메인 로직 ---
solve_with_final_rules()
