def push_maxHeap(heap, value):
    heap.append(value)

    current_idx = len(heap) - 1
     
    while current_idx > 1 and heap[current_idx] > heap[current_idx // 2]:
        parent_idx = current_idx // 2
        heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
        current_idx = parent_idx


def pop_maxHeap(heap):
    if len(heap) <= 1:
        return None
    
    max_val = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    current_idx = 1

    while True:
        left_child_idx = current_idx * 2
        right_child_idx = current_idx * 2 + 1
        largest_idx = current_idx

        if left_child_idx < len(heap) and heap[left_child_idx] > heap[largest_idx]:
            largest_idx = left_child_idx
        if right_child_idx < len(heap) and heap[right_child_idx] > heap[largest_idx]:
            largest_idx = right_child_idx
        
        if largest_idx == current_idx:
            break

        heap[current_idx], heap[largest_idx] = heap[largest_idx], heap[current_idx]
        current_idx = largest_idx
    return max_val

def push_minHeap(heap, value):
    heap.append(value)

    current_idx = len(heap) - 1
     
    while current_idx > 1 and heap[current_idx] < heap[current_idx // 2]:
        parent_idx = current_idx // 2
        heap[current_idx], heap[parent_idx] = heap[parent_idx], heap[current_idx]
        current_idx = parent_idx

def pop_minHeap(heap):
    if len(heap) <= 1:
        return None
    
    min_val = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    current_idx = 1

    while True:
        left_child_idx = current_idx * 2
        right_child_idx = current_idx * 2 + 1
        smallest_idx = current_idx

        if left_child_idx < len(heap) and heap[left_child_idx] < heap[smallest_idx]:
            smallest_idx = left_child_idx
        if right_child_idx < len(heap) and heap[right_child_idx] < heap[smallest_idx]:
            smallest_idx = right_child_idx

        if smallest_idx == current_idx:
            break

        heap[current_idx], heap[smallest_idx] = heap[smallest_idx], heap[current_idx]
        current_idx = smallest_idx
    
    return min_val

N = int(input())

max_heap = [None]
min_heap = [None]

for i in range(N):
    num = int(input())

    if len(max_heap) == len(min_heap):
        push_maxHeap(max_heap, num)
    else:
        push_minHeap(min_heap, num)

    if len(min_heap) > 1 and max_heap[1] > min_heap[1]:
        max_val = pop_maxHeap(max_heap)
        min_val = pop_minHeap(min_heap)

        push_maxHeap(max_heap, min_val)
        push_minHeap(min_heap, max_val)

    print(max_heap[1])
