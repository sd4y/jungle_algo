N = list(map(int ,input().split()))

x = N[0]
y = N[1]
w = N[2]
h = N[3]

xlen = w - x
ylen = h - y

X_value = 0
Y_value = 0

if x <= xlen : X_value = x
else : X_value = xlen

if y <= ylen : Y_value = y
else : Y_value = ylen

if X_value >= Y_value : print(Y_value)
else : print(X_value)