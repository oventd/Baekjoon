from collections import deque

test_count = int(input())
test_cases = [] 
for _ in range(test_count):
    map_n = int(input())
    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    test_cases.append((map_n,start,end))

def bfs(case):
    n = case[0]
    start_x, start_y = case[1]
    end_pos = case[2]
    queue = deque()
    visited = [[False]*n for _ in range(n)]
    dirs = [(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1)]
    
    queue.append((start_y,start_x,0))
    visited[start_y][start_x] =True

    while queue:
        qy, qx, distance = queue.popleft()
        for dir in dirs:
            dy, dx = qy + dir[0], qx + dir[1]
            if not (0<=dy<n and 0<=dx<n):
                continue
            if visited[dy][dx]:
                continue
            if (dx, dy) == end_pos:
                return distance + 1
            queue.append((dy,dx,distance + 1))
            visited[dy][dx] = True
    return 0
    
for test_case in test_cases:
    print(bfs(test_case))

