N, K = map(int, input().split())

Data = []

for i in range(N):
    W, V = map(int, input().split())
    Data.append((W, V))

BagCase = [0] * (K+1)


for W, V in Data:
    for i in range(K, W-1, -1):
        itemsValue = BagCase[i - W] + V            

        if itemsValue > BagCase[i]:   
            BagCase[i] = itemsValue       

print(BagCase[K])
