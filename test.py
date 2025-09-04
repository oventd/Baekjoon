import sys

input = sys.stdin.readline

N = int(input())
ns = []
for _ in range(N):
    ns.append(int(input()))
ns.sort()
print("\n".join(map(str, ns)))
you are mine hello hello you