def solution(friends, gifts):
    answer = 0
    
    size = len(friends)
    
    Vec_Data = [[] * size for _ in range(size)]

    x, y = 0, 0
    for i in range(len(gifts)) :
        for j in range(size)
            temp = list(gifts[i].split())
            if temp[0] == friends[j]:
                x = j
            if temp[1] == friends[j]:
                y = j
        Vec_Data[x][y] += 1
        
    
            
                
    return answer