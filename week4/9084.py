T = int(input())

for _ in range(T):
    coin_count = int(input())
    coins = list(map(int, (input().split())))
    target_money = int(input())

    dp = [0] * (target_money + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, target_money+1):
            dp[i] += dp[i - coin]

    print(dp[target_money])
