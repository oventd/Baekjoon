from collections import deque
n = int(input())
village = []
for _ in range(n):
    village.append(list(map(int,list(input()))))

def bfs():
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    sizes = []
    for y, row in enumerate(village):
        for x, value in enumerate(row):
            if visited[y][x]:
                continue
            if value == 0:
                continue
            queue.append((y,x))
            visited[y][x] = True
            size = 1
            while queue:
                qy, qx = queue.popleft()
                for i in range(4):
                    ny, nx = qy+dy[i], qx+dx[i]
                    if not (0<=ny<n and 0<=nx<n):
                        continue
                    if visited[ny][nx]:
                        continue
                    if village[ny][nx] != 1:
                        continue
                    visited[ny][nx] = True
                    size += 1
                    queue.append((ny,nx))
            sizes.append(size)
    return sizes
sizes = bfs()
print(len(sizes))
sizes.sort()
for size in sizes:
    print(size)
