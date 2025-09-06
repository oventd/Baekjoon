import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n, m = map(int,input().split())
    nums = list(map(int,input().split()))

    queue = deque()
    for i, p in enumerate(nums):
        queue.append((p, i))
    count = 0
    while queue:
        qp, qi = queue.popleft()
        if qp < max(queue):
            queue.append((qp, qi))
            continue
        count += 1
        if qi == m:
            print(count)