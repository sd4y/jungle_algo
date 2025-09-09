def func(N):   
    if N == 1:
        return 1    
    return func(N - 1) + 1
