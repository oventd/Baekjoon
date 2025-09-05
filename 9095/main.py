import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    n = int(input())
    visited = set()
    s = [1]*n
    queue.append(s)
    visited.add(tuple(s))
    while queue:
        qn = queue.popleft()

        for i in range(len(qn)-1):
            sn = qn[i] + qn[i+1]
            if sn >3:
                continue
            exclude_indices = {i, i+1}
            new = [v for i, v in enumerate(qn) if i not in exclude_indices]
            new.insert(i,sn)
            if tuple(new) in visited:
                continue
            if sum(new) != n:
                continue
            visited.add(tuple(new))
            queue.append(new)
    print(len(visited))