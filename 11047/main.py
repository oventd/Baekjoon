n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

count = 0
for coin in coins:
    if coin <= k:
        cn = k // coin
        k -= cn * coin
        count += cn
print(count)