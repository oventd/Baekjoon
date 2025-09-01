from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
        continue
    stack.append(num)
    
print(sum(stack) if stack else 0) 