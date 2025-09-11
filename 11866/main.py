import sys
from collections import deque

input = sys.stdin.readline

queue = deque()

N, K  = map(int, input().split())

for i in range(N):
    queue.append(i+1)
result  = []
while queue:
    queue.rotate(-(K-1))
    result.append(queue.popleft())

print(f"<{', '.join(map(str, result))}>")