import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    case_list = []
    for _ in range(N) :
        doc_rank, interview_rank = map(int, input().split())
        case_list.append([doc_rank, interview_rank])
    
    case_list.sort()

    count = 1

    Ref_rank = case_list[0][1]

    for i in range(1, N):
        if case_list[i][1] <= Ref_rank:
            count += 1
            Ref_rank = case_list[i][1]

    print(count)