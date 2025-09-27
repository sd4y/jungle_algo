import sys

input = sys.stdin.readline

# 펜윅 트리(Fenwick Tree) 또는 이진 인덱스 트리(BIT) 클래스
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    # 특정 인덱스에 값을 1 증가 또는 감소
    def update(self, index, diff):
        index += 1 # 1-based index로 변환
        while index < len(self.tree):
            self.tree[index] += diff
            index += (index & -index)

    # 0부터 특정 인덱스까지의 누적 합을 구함
    def query(self, index):
        index += 1 # 1-based index로 변환
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= (index & -index)
        return s

# --- 메인 로직 ---
N = int(input())
all_coords = set()  #의미 있는 좌표만 남기고 중복 제거
events = []

# 1. 이벤트 포인트 생성 및 좌표 수집
for _ in range(N):
    x, r = map(int, input().split())
    left, right = x - r, x + r
    events.append((left, 'open', right))
    events.append((right, 'close', left))
    all_coords.add(left)
    all_coords.add(right)

# 2. 좌표 압축
# 모든 좌표들을 정렬하고, 각 좌표에 0부터 시작하는 고유 번호를 부여
sorted_coords = sorted(list(all_coords))
coord_map = {coord: i for i, coord in enumerate(sorted_coords)}
tree_size = len(sorted_coords)

# 3. 이벤트 정렬
# 좌표가 같으면 open 이벤트를 먼저 처리
events.sort(key=lambda e: (e[0], -1 if e[1] == 'open' else 1))

# 4. 스위핑 실행
bit = FenwickTree(tree_size)
intersections = 0
tangent_containments = 0

i = 0
while i < len(events):
    current_coord = events[i][0]
    
    opens_at_this_coord = []
    closes_at_this_coord = []
    
    # 현재 x좌표에서 발생하는 모든 이벤트를 그룹화
    j = i
    while j < len(events) and events[j][0] == current_coord:
        event = events[j]
        if event[1] == 'open':
            opens_at_this_coord.append(event)
        else:
            closes_at_this_coord.append(event)
        j += 1

    # --- 'open' 이벤트 처리 ---
    # 4-1. 현재 열리는 원들이 '이전에 열린' 원들과 맺는 관계 계산
    for _, _, other_coord in opens_at_this_coord:
        left_idx = coord_map[current_coord]
        right_idx = coord_map[other_coord]

        # 교차(Intersection): L1 < L2 < R1 < R2
        # 활성 원들 중 right 좌표가 (현재 L, 현재 R) 사이에 있는 원의 개수
        intersections += bit.query(right_idx - 1) - bit.query(left_idx)
        
        # 내접(Tangent Containment): L1 < L2 and R1 == R2
        # 활성 원들 중 right 좌표가 현재 R과 같은 원의 개수
        tangent_containments += bit.query(right_idx) - bit.query(right_idx - 1)

    # 4-2. '현재 같이 열리는' 원들끼리의 관계 계산
    # L좌표가 같은 원들은 서로 교차하지 않고 내접/포함 관계만 맺음
    k = len(opens_at_this_coord)
    tangent_containments += k * (k - 1) // 2

    # 4-3. 현재 열린 원들을 펜윅 트리에 추가 (활성 상태로 전환)
    for _, _, other_coord in opens_at_this_coord:
        right_idx = coord_map[other_coord]
        bit.update(right_idx, 1)

    # --- 'close' 이벤트 처리 ---
    # 원들을 활성 상태에서 제거
    for coord, _, _ in closes_at_this_coord:
        right_idx = coord_map[coord]
        bit.update(right_idx, -1)
    
    i = j # 다음 좌표의 이벤트로 이동

# 5. 최종 영역의 개수 계산 (1 + N + I + T)
total_areas = 1 + N + intersections + tangent_containments
print(total_areas)
