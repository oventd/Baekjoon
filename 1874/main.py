from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
goal = []
for _ in range(N):
    goal.append(int(input()))

stack = deque()
n = 1
result=[]

for g in goal:
    while n<=g:
        stack.append(n)
        result.append("+")
        n+=1
    if stack[-1] == g:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit()

print("\n".join(result))