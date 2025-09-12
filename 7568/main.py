import sys

input = sys.stdin.readline

N = int(input())
mens = []
for _ in range(N):
    mens.append(list(map(int,input().split())))
result = []
for i in range(len(mens)):
     count = 1
     for j in range(len(mens)):
         if i == j:
             continue
         if mens[i][0] < mens[j][0] and mens[i][1] < mens[j][1]:
             count += 1
     result.append(str(count))
print(" ".join(result))