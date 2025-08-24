N = int(input())
tests = list(map(int,input().split()))

count = 0
def is_prime(num: int) -> bool:
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
for t in tests:
    if is_prime(t):
        count += 1
print(count)