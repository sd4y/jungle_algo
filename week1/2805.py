n , m = 4 , 7
tree_arr = [20, 15, 10, 17]

def func(goal, cut_h, tree_arr, sum_tree, start, size): #목표값 , 자르는 높이, 나무 리스트, 자른 나무의 합, 자르기 시작할 인덱스
    
    # cut_h 로 tree_arr 역순으로 자르면서 더한 값이 | sum_tree - 목표값 | 보다 크면 탈출 작으면 해당 값을 sum_tree로 옮기기
    target = abs(goal - sum_tree)
    temp = 0
    half_cut = cut_h//2
    for i in range(size, -1, -1):
        if temp >= target:
            break
        tree_len = tree_arr[i] - half_cut
        temp += tree_len
    
    if True:
        next_cut_h = (half_cut + cut_h)//2
        func(goal, next_cut_h, tree_arr, )

    
    return 0
tree_arr.sort()

mid = max(tree_arr)

func(7, mid, tree_arr, 0, 0, len(tree_arr))