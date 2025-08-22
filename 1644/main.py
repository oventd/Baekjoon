

N = int(input())

def is_prime(num: int) -> bool:
    """Check if num is prime."""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
def next_prime(n: int) -> int:
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1
def priv_prime(n:int):
    candidate = n - 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate -= 1

left = 2
right = N if is_prime(N) else priv_prime(N)
count = 0
while left<=right:
    s = 0
    n = left
    while True:
        s += n
        if n == right:
            break
        n = next_prime(n)
    if s == N:
        count += 1
        left = next_prime(left)
        right =  priv_prime(N)
    if s > N:
        left = next_prime(left)
    elif s < N:
        right = priv_prime(right)

print(count)


