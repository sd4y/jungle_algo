""" N = int(input())

arr = []

for i in range(N):
    temp = int(input())
    if not temp == 0:
        arr.append(temp)
    else:
        if len(arr) > 0:
            arr.sort()
            print(arr[-1])
            arr.pop()
        else:
            print(0)


import sys """

import sys
input = sys.stdin.readline

# --- 힙 연산 함수 ---

def push_heap(heap, value):
    """heap 리스트에 value를 추가하고 힙 속성을 유지합니다."""
    # 1. 가장 마지막에 원소 추가
    heap.append(value)
    current_idx = len(heap) - 1
    
    # 2. 부모 노드와 비교하며 sift-up
    # 현재 노드가 루트(인덱스 1)보다 크고, 부모보다 값이 크면 swap
    while current_idx > 1 and heap[current_idx] > heap[current_idx // 2]:
        parent_idx = current_idx // 2
        heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
        current_idx = parent_idx

def pop_heap(heap):
    """heap 리스트에서 최댓값을 반환하고 힙 속성을 유지합니다."""
    # 힙이 비어있으면 0을 반환 (문제의 조건)
    if len(heap) <= 1:
        return 0
    
    # 최댓값 (루트)
    max_val = heap[1]

    # 1. 루트에 가장 마지막 원소를 가져오고, 마지막 원소는 제거
    heap[1] = heap[-1]
    heap.pop()

    # 힙에 원소가 하나만 있었을 경우 바로 반환
    if len(heap) <= 1:
        return max_val
    
    # 2. 자식 노드와 비교하며 sift-down
    current_idx = 1
    while True:
        left_child_idx = current_idx * 2
        right_child_idx = current_idx * 2 + 1
        largest_idx = current_idx

        # 왼쪽 자식과 비교
        if left_child_idx < len(heap) and heap[left_child_idx] > heap[largest_idx]:
            largest_idx = left_child_idx
        
        # 오른쪽 자식과 비교
        if right_child_idx < len(heap) and heap[right_child_idx] > heap[largest_idx]:
            largest_idx = right_child_idx
        
        # 현재 노드가 자식들보다 크면 제자리를 찾은 것
        if largest_idx == current_idx:
            break
        
        # 자식 중 더 큰 값과 swap
        heap[current_idx], heap[largest_idx] = heap[largest_idx], heap[current_idx]
        current_idx = largest_idx
        
    return max_val

# --- 문제 풀이 로직 ---
N = int(input())
heap = [None] # 힙으로 사용할 리스트 (1-based 인덱싱)

for _ in range(N):
    command = int(input())
    if command != 0:
        push_heap(heap, command)
    else:
        print(pop_heap(heap))
