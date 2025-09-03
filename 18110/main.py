import sys
input = sys.stdin.readline
N = int(input())

opinions = []

for _ in range(N):
    opinions.append(int(input()))
opinions.sort()

if N ==0:
    print(0)
else:    
    cut_n = round(N *0.15)
    trimmed = opinions[cut_n:N-cut_n]
    count = N-cut_n*2

    print(round( sum(opinions[cut_n:-cut_n])/count))