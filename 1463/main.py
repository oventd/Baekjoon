import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

visited = [False] * (n + 1)
visited[n] = True

queue = deque([(n, 0)])

while queue:
    qn, qc = queue.popleft()
    if qn == 1:
        print(qc)
        break

    if qn % 3 == 0 and not visited[qn // 3]:
        visited[qn // 3] = True
        queue.append((qn // 3, qc + 1))

    if qn % 2 == 0 and not visited[qn // 2]:
        visited[qn // 2] = True
        queue.append((qn // 2, qc + 1))

    if qn - 1 > 0 and not visited[qn - 1]:
        visited[qn - 1] = True
        queue.append((qn - 1, qc + 1))
