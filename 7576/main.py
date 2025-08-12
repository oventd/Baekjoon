from collections import deque

m, n = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    queue = deque()
    days = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for y in range(n):
        for x in range(m):
            if boxes[y][x] == 1:
                queue.append((y, x))
                visited[y][x] = True
            elif boxes[y][x] == -1:
                visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and boxes[ny][nx] == 0:
                    visited[ny][nx] = True
                    days[ny][nx] = days[y][x] + 1
                    queue.append((ny, nx))

    max_day = 0
    for y in range(n):
        for x in range(m):
            if not visited[y][x] and boxes[y][x] == 0:
                return -1
            max_day = max(max_day, days[y][x])
    return max_day

print(bfs())