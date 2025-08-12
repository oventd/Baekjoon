from collections import deque
n = int(input())
canvas = []
for _ in range(n):
    canvas.append(list(input()))

def bfs_rgb():
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    r = 0
    g = 0
    b = 0
    for y, row in enumerate(canvas):
        for x, color in enumerate(row):
            if visited[y][x]:
                continue
            visited[y][x] = True
            queue.append((y, x))
            if color == "R":
                r += 1
            elif color == "G":
                g += 1
            elif color == "B":
                b += 1

            while queue:
                qy, qx = queue.popleft()
                for i in range(4):
                    ny, nx = qy+dy[i], qx+dx[i]
                    if not (0<=ny<n and 0<=nx<n):
                        continue
                    if visited[ny][nx]:
                        continue
                    if canvas[ny][nx] != color:
                        continue
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return r+g+b
def bfs_rg_b():
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    rg = 0
    b = 0
    for y, row in enumerate(canvas):
        for x, color in enumerate(row):
            if visited[y][x]:
                continue
            visited[y][x] = True
            queue.append((y, x))
            if color in ["R", "G"]:
                rg += 1
            elif color == "B":
                b += 1

            while queue:
                qy, qx = queue.popleft()
                for i in range(4):
                    ny, nx = qy+dy[i], qx+dx[i]
                    if not (0<=ny<n and 0<=nx<n):
                        continue
                    if visited[ny][nx]:
                        continue
                    if color == "B":
                        if canvas[ny][nx] != "B":
                            continue
                    if color in ["R", "G"]:
                        if canvas[ny][nx] not in ["R","G"]:
                            continue
                    visited[ny][nx] = True
                    queue.append((ny, nx))
    return rg + b
print(bfs_rgb(), bfs_rg_b())