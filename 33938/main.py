from collections import deque
import sys

input = sys.stdin.readline

n, goal = map(int, input().rstrip().split())
if n == 0:
    print(-1)
    sys.exit()

p_list = list(map(int, input().rstrip().split()))
if goal == 0:
    print(0)
    sys.exit()
if goal in p_list:
    print(1)
    sys.exit()

visited = set()

queue = deque()
for p in p_list:
    queue.append((1,[p]))
    visited.add((p,))

while queue:
    q_cnt, q_l = queue.popleft()
    for p in p_list:
        if sum(q_l)+p == goal:
            print(q_cnt+1)
            sys.exit()
        d_l = [ q for q in q_l]
        d_l.append(p)
        d_l.sort()
        if tuple(d_l) in visited:
            continue
        visited.add(tuple(d_l))
        if abs(goal-sum(q_l)) < abs(goal-sum(d_l)):
            continue
        d_cnt = q_cnt+1
        queue.append((d_cnt, d_l))
print(-1)