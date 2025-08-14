from collections import deque

n, m = map(int, input().split())
miro = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fire_time = [[-1]*m for _ in range(n)]
jihun_time = [[-1]*m for _ in range(n)]
queue = deque()

for y in range(n):
    for x in range(m):
        if miro[y][x] == 'F':
            fire_time[y][x] = 0
            queue.append(('F', y, x))

while queue:
    obj, y, x = queue.popleft()
    if obj != 'F':
        continue
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if miro[ny][nx] != '#' and fire_time[ny][nx] == -1:
                fire_time[ny][nx] = fire_time[y][x] + 1
                queue.append(('F', ny, nx))

for y in range(n):
    for x in range(m):
        if miro[y][x] == 'J':
            jihun_time[y][x] = 0
            queue.append(('J', y, x))

while queue:
    obj, y, x = queue.popleft()
    if obj != 'J':
        continue
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if not (0 <= ny < n and 0 <= nx < m):
            print(jihun_time[y][x] + 1)
            exit()
        if miro[ny][nx] != '#' and jihun_time[ny][nx] == -1:
            if fire_time[ny][nx] == -1 or fire_time[ny][nx] > jihun_time[y][x] + 1:
                jihun_time[ny][nx] = jihun_time[y][x] + 1
                queue.append(('J', ny, nx))

print("IMPOSSIBLE")
