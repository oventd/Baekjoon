from collections import deque

n, m = map(int, input().split())

field = []
for _ in range(n):
    field.append(list(input().rstrip()))

visited = [[False]*m for _ in range(n)]

cnt = 0
for y, row in enumerate(field):
    for x, value in enumerate(row):
        if visited[y][x]:
            continue
        if value != "#":
            continue
        queue = deque()
        queue.append((y, x))
        cnt += 1
        visited[y][x] = True
        while queue:
            qy, qx = queue.popleft()
            dirs = [(qy+1,qx), (qy-1,qx), (qy,qx+1), (qy,qx-1)]
            for dy, dx in dirs:
                if not (0 <= dy < n and 0 <= dx < m):
                    continue
                if visited[dy][dx]:
                    continue
                if field[dy][dx] != "#":
                    continue
                visited[dy][dx] = True
                queue.append((dy, dx))
print(cnt)