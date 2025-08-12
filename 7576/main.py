from collections import deque
m, n = map(int,input().split())
boxes = []
for _ in range(n):
    row = list(map(int,input().split()))
    boxes.append(row)


def bfs(boxes):
    queue = deque()
    visited = [[False]*m for _ in range(n)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for y, row in enumerate(boxes):
        for x, value in enumerate(row):
            if visited[y][x]:
                continue
            if value == 1:
                visited[y][x] = (y,x,0)
                queue.append((y,x,0))
            elif value == -1:
                visited[y][x] = (y,x,0)
    while queue:
        qy, qx, qd = queue.popleft()
        for i in range(4):
            ny, nx = qy+dy[i], qx+dx[i]
            if not (0<=ny<len(boxes) and 0<=nx<len(boxes[0])):
                continue
            if visited[ny][nx]:
                continue
            if boxes[ny][nx] != 0:
                continue
            visited[ny][nx] = (ny,nx,qd+1)
            queue.append((ny,nx,qd+1))
    days = []
    for py in visited:
        for px in py:
            if not px:
                return -1
            days.append(px[2])
    return max(days) if days else 0

print(bfs(boxes))