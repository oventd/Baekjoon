from collections import deque

n, m = map(int,input().split())
canvas = []
for i in range(n):
    canvas.append(list(map(int, input().split()))) 

def dfs(canvas):
    queue = deque()
    n, m = len(canvas), len(canvas[0])
    visited = [ [False]*m for i in range(n)] 
    count = 0
    sizes = []

    for y, row in enumerate(canvas):
        for x, value in enumerate(row):
            if value == 0:
                continue
            if visited[y][x] is True:
                continue
            queue.append((y,x))
            count += 1
            size = 0
            
            while len(queue) != 0:
                qy, qx = queue.popleft()
                if visited[qy][qx] is True:
                    continue
                visited[qy][qx] = True
                size += 1
                dirs = [[qy+1,qx], [qy-1,qx], [qy,qx+1], [qy,qx-1]]
                
                for dir in dirs:
                    dy, dx = dir[0], dir[1]
                    if not (0 <= dy < n and 0 <= dx < m):
                        continue
                    if visited[dy][dx] is True:
                        continue
                    if canvas[dy][dx] != 1:
                        continue
                    queue.append((dy,dx))
            sizes.append(size)
    return count, max(sizes)

p_count, p_size = dfs(canvas)
print(p_count)
print(p_size)
