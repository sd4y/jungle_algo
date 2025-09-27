import sys
input = sys.stdin.readline

# N: 멀티탭 구멍의 개수, K: 전기용품의 총 사용횟수
N, K = map(int, input().split())

# 전기용품 사용 순서
schedule = list(map(int, input().split()))

# 현재 멀티탭에 꽂혀있는 전기용품
multitap = set()

# 플러그를 뽑은 횟수
unplugs = 0 

for i, item in enumerate(schedule):
    
    # 1. 꽂으려는 전기용품이 이미 멀티탭에 있는 경우
    if item in multitap:
        continue
        
    # 2. 멀티탭에 빈자리가 있는 경우
    if len(multitap) < N:
        multitap.add(item)
        continue
        
    # 3. 멀티탭이 꽉 차서 하나를 뽑아야 하는 경우
    item_to_unplug = 0      # 뽑을 아이템
    latest_use_index = -1   # 가장 나중에 사용될 시점의 인덱스

    # 현재 꽂혀있는 플러그들 중에서 교체할 플러그를 찾기
    for plugged_item in multitap:
        try:
            # 현재 사용 순서 이후에 해당 플러그가 언제 다시 사용되는지 탐색
            next_use_index = schedule[i + 1:].index(plugged_item)
        except ValueError:
            # 만약 앞으로 사용할 리스트에 없다면, 그 플러그를 바로 뽑는다.
            item_to_unplug = plugged_item
            break
            
        # 더 나중에 사용되는 플러그를 교체 대상으로 기록한다.
        if next_use_index > latest_use_index:
            latest_use_index = next_use_index
            item_to_unplug = plugged_item
            
    # 위 반복문이 끝난 후 결정된 플러그를 뽑고 새로운 플러그를 꽂는다.
    multitap.remove(item_to_unplug)
    multitap.add(item)
    unplugs += 1

print(unplugs)
        