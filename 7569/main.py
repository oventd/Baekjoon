from collections import deque
m, n, h = map(int,input().split())
boxes = []
for _ in range(h):
    box = []
    for _ in range(n):
        row = list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

def bfs():
    queue = deque()
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    days = [[[False]*m for _ in range(n)] for _ in range(h)]
    dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
    
    for z, box in enumerate(boxes):
        for y, row in enumerate(box):
            for x, value in enumerate(row):
                if visited[z][y][x]:
                    continue
                if value == 1:
                    queue.append((z,y,x))
                    visited[z][y][x] = True
                    days[z][y][x] = 0
                elif value == -1:
                    visited[z][y][x] = True
                    days[z][y][x] = -1
    while queue:
        qz, qy, qx = queue.popleft()
        
        for dir in dirs:
            dz, dy, dx = qz + dir[0], qy + dir[1], qx + dir[2]
            if not (0<=dz<h and 0<=dy<n and 0<=dx<m):
                continue
            if visited[dz][dy][dx]:
                continue
            if boxes[dz][dy][dx] == -1:
                continue
            days[dz][dy][dx] = days[qz][qy][qx] + 1
            visited[dz][dy][dx] = True
            queue.append((dz,dy,dx))
    max_day = 0
    for day_z, day in enumerate(days):
        for day_y, day_row in enumerate(day):
            for day_x, day_value in enumerate(day_row):
                if day_value is False:
                    return -1
                if max_day < day_value:
                    max_day = day_value
    return max_day
print(bfs())
                