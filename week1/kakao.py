def solution(friends, gifts):
    answer = 0
    
    size = len(friends)
    
    if not friends:
        return 0
    
    Vec_Data = [[0] * size for _ in range(size)]
    
    diff = [0] * size
    
    map_Data = {name:i for i , name in enumerate(friends)}

    for i in gifts:
        A, B = i.split()
        A_idx = map_Data[A]
        B_idx = map_Data[B]

        Vec_Data[A_idx][B_idx] += 1

        diff[A_idx] += 1
        diff[B_idx] -= 1

    next = [0]*size

    for i in range(size):
        for j in range(i+1, size):
            itoj = Vec_Data[i][j]
            jtoi = Vec_Data[j][i]

            if itoj > jtoi:
                next[i] += 1
            elif itoj < jtoi:
                next[j] += 1
            else:
                if diff[i] > diff[j]:
                    next[i] += 1
                elif diff[i] < diff[j]:
                    next[j] += 1
    
    if next :
        answer = max(next)
    else:
        answer = 0
                
    return answer