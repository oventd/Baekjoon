from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
goal = []
for _ in range(N):
    goal.append(int(input()))

stack = deque()
n = 1
i=0
result=[]
while i<N:
    if n <= goal[i]:
        stack.append(n)
        result.append("+")
        if n == goal[i]:
            stack.pop()
            result.append("-")
            i+=1
        n+=1
    elif n>goal[i]:
        if stack[-1] == goal[i]:
            stack.pop()
            result.append("-")
            i+=1
        else:
            print("NO")
            sys.exit()

print("\n".join(result))