import sys
import math

input = sys.stdin.readline

while True:
    num = int(input())
    if num == -1:
        break
    divisors = [1]
    n = 1
    while n <= math.sqrt(num):
        if num % n == 0:
            divisors.append(n)
            divisors.append(num // n)
        n += 1
    divisors.sort()
    divisors.pop()
    if sum(divisors) == num:
        print(f"{num} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{num} is NOT perfect.")