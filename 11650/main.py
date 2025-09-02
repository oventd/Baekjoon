import sys
input = sys.stdin.readline

N= int(input())
xys = []
for i in range(N):
    x,y = map(int,input().split())
    xys.append((x,y))
xys.sort()
print("\n".join([ f"{x[0]} {x[1]}" for x in xys]))