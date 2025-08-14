from collections import deque
n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    flame_visited = [[False]*m for _ in range(n)]
    jihun_visited = [[False]*m for _ in range(n)]

    time = [[False]*m for _ in range(n)]
    queue = deque() 
    

    for y, row in enumerate(miro):
        for x, value in enumerate(row):
            if value == "#":
                jihun_visited[y][x] = True
                flame_visited[y][x] = True
                continue
            if value == "J":
                jihun_visited[y][x] = True
                time[y][x] = 0
                queue.append((y,x,"J"))
            if value == "F":
                flame_visited[y][x] = True
                queue.append((y,x,"F"))
    while queue:
        qy, qx, obj = queue.popleft()
        
        for i in range(4):
            ny, nx = qy+dy[i] , qx+dx[i]

            if not (0<=ny<n and 0<=nx<m):
                if obj == "J":
                    print(time[qy][qx] + 1)
                    return
                continue
            if obj == "F":
                if flame_visited[ny][nx]:
                    continue
                if miro[ny][nx]=="J":
                    print("IMPOSSIBLE")
                    return
                 
            if obj == "J":

            
        if obj == "J":
            miro[qy][qx] = "."
    print("IMPOSSIBLE")
    return
bfs()