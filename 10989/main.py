import sys

input = sys.stdin.readline

N = int(input())

counts = [0]*10001

ns = []
for _ in range(N):
    n = int(input())
    counts[n] +=1
for i in range(1,10001):
    if counts[i]>0:
        for _ in range(counts[i]):
            print(i)