import sys
from collections import deque

input = sys.stdin.readline

computer_n = int(input().strip())
edge_n = int(input().strip())

adj = [[] for _ in range(computer_n + 1)]
for _ in range(edge_n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (computer_n + 1)
q = deque([1])
visited[1] = True
infected = 0

while q:
    cur = q.popleft()
    for nxt in adj[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)
            infected += 1

print(infected)