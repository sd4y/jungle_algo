T = int(input())

def func(N,start,mid,end,moves):            # 목표 : 모든 원반을 도착지점으로 이동하기
    if N == 1:                              # 원판이 1개라면
        moves.append((start, end))          # 시작지점에서 도착지점으로 원판 옮겨라
    else:                                   # 원판이 2개 이상이라면
        func(N-1,start, end, mid, moves)    # 하나를 제외한 나머지 원판을 mid로 옮겨라 -> start의 모든 원판을 mid로 옮겨라
        moves.append((start, end))          # 시작지점에 있는 원판을 도착지점으로 옮겨라
        func(N-1,mid, start, end, moves)    # mid에 있던 원판을 모두 도착지점으로 옮겨라 -> mid의 모든 원판을 end로 옮겨라

total_moves = 2**T -1
print(total_moves)

if T <= 20:
    moves = []
    func(T, 1, 2, 3, moves)
    for s, e in moves:
        print(s, e)
    
