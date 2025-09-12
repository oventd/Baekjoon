
n, m = map(int, input().split())

gcd = 1

for i in range(min((n,m)),1,-1):
    if n % i == 0 and m % i == 0:
        gcd = i
        break

lcd = n * m // gcd
print(f"{gcd}\n{lcd}")