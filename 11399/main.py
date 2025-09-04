import sys

input = sys.stdin.readline

N = int(input())
ps = list(map(int,input().split()))

ps.sort()

result = 0
n = 0
for p in ps:
    result += n + p
    n += p

print(result)