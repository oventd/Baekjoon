from collections import deque
n, m = map(int, input().split())
canvas = []
for _ in range(n):
    canvas.append(list(map(int,input().split())))

d_canvas = [[-1]*m for _ in range(n)]
for y, row in enumerate(canvas):
    for x, value in enumerate(row):
        if value == 0:
            d_canvas[y][x] = 0
def bfs():
    sy = sx = -1
    for y, row in enumerate(canvas):
        for x, value in enumerate(row):
            if value == 2:
                sy, sx = y, x
                break
        if sy != -1:
            break
    queue = deque()
    visited = [[False]*m for _ in range(n)]
    
    d_canvas[sy][sx] = 0
    visited[sy][sx] = True
    queue.append((sy, sx))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        qy, qx = queue.popleft()
        for i in range(4):
            ny, nx = qy+dy[i], qx+dx[i]
            if not(0<=ny<n and 0<=nx<m):
                continue
            if visited[ny][nx]:
                continue
            if canvas[ny][nx] == 0:
                continue
            visited[ny][nx] = True
            d_canvas[ny][nx] = d_canvas[qy][qx]+1
            queue.append((ny,nx))
bfs()
for row in d_canvas:
    print(" ".join(list(map(str, row))))
