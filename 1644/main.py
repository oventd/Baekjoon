def get_primes(n):
    """에라토스테네스의 체로 n 이하의 소수 리스트 리턴"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

N = int(input())
primes = get_primes(N)

count = 0
left = right= 0
s=0

while True:
    if s >=N:
        if s == N:
            count +=1
        s -= primes[left]
        left += primes[left]
    elif right == len(primes):
        break
    else:
        s += primes[right]
        right += 1

print(count)