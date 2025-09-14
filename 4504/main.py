import sys

input = sys.stdin.readline

n  = int(input())
while True:
    string  = input().rstrip()
    if string == "0":
        break
    num = int(string)
    if num % n == 0:
        print(f"{num} is a multiple of {n}.")
    else:
        print(f"{num} is NOT a multiple of {n}.")
