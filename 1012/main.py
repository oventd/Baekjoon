from collections import deque
def bfs(field):
    m = len(field[0])
    n = len(field)
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for y, row in enumerate(field):
        for x, value in enumerate(row):
            if value is False:
                continue
            if visited[y][x]:
                continue
            visited[y][x] = True
            queue.append((y,x))
            count += 1
            while queue:
                qy, qx = queue.popleft()
                for i in range(4):
                    ny, nx = qy+dy[i], qx+dx[i]
                    if not (0<=ny<n and 0<=nx<m):
                        continue
                    if visited[ny][nx]:
                        continue
                    if field[ny][nx] is False:
                        continue
                    visited[ny][nx] = True
                    queue.append((ny,nx))
    return count

test = int(input())
for _ in range(test):
    m, n, c = map(int, input().split())
    field = [[False]*m for _ in range(n)]
    for i in range(c):
        x, y  = map(int,input().split())
        field[y][x] = True
    print(bfs(field))
    
