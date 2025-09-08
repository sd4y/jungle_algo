import sys

N, r, c = map(int, sys.stdin.readline().split())

# 최종 결과를 저장할 변수
result = 0

def solve(n, y, x):
    """
    한 변의 길이가 2**n인 정사각형에서 (y, x)의 방문 순서를 찾습니다.
    """
    global result

    # 가장 작은 1x1 정사각형에 도달하면 재귀를 종료합니다.
    if n == 0:
        return

    # 현재 정사각형의 한 변 길이의 절반
    half = 2**(n - 1)

    # 1사분면 (좌상단)에 목표 좌표가 있는 경우
    if y < half and x < half:
        # 이 사분면은 가장 먼저 탐색하므로, result에 아무것도 더하지 않습니다.
        solve(n - 1, y, x)
    
    # 2사분면 (우상단)에 목표 좌표가 있는 경우
    elif y < half and x >= half:
        # 1사분면을 이미 모두 방문했으므로, 그 크기만큼 result에 더해줍니다.
        result += half * half
        # 다음 탐색을 위해 좌표를 2사분면 내의 상대 좌표로 변경합니다. (x - half)
        solve(n - 1, y, x - half)

    # 3사분면 (좌하단)에 목표 좌표가 있는 경우
    elif y >= half and x < half:
        # 1, 2사분면을 이미 모두 방문했으므로, 그 크기만큼 result에 더해줍니다.
        result += 2 * half * half
        # 다음 탐색을 위해 좌표를 3사분면 내의 상대 좌표로 변경합니다. (y - half)
        solve(n - 1, y - half, x)

    # 4사분면 (우하단)에 목표 좌표가 있는 경우
    else:
        # 1, 2, 3사분면을 이미 모두 방문했으므로, 그 크기만큼 result에 더해줍니다.
        result += 3 * half * half
        # 다음 탐색을 위해 좌표를 4사분면 내의 상대 좌표로 변경합니다. (y - half, x - half)
        solve(n - 1, y - half, x - half)

# 가장 큰 정사각형(한 변 2**N)에서 (r, c)를 찾는 것으로 시작
solve(N, r, c)

print(result)