from collections import deque

def paint(canvas, square):
    y1, x1 = square[0]
    y2, x2 = square[1]

    for y in range(y1, y2):
        for x in range(x1, x2):
            canvas[y][x] = True
# def print_canvas(canvas):
#     for y in range(len(canvas)-1,-1,-1) :
#         for x in range(len(canvas[0])):
#             if canvas[y][x]:
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")
#         print()
def bfs(canvas):
    visited = [[False]*len(canvas[0]) for _ in range(len(canvas))]
    extents = []
    queue = deque()

    for y, row in enumerate(canvas):
        for x, value in enumerate(row):
            if visited[y][x]:
                continue 
            if value:
                continue

            queue.append((y,x))
            visited[y][x]= True
            extent = 0
            while queue:
                qy, qx = queue.popleft()
                
                extent += 1
                
                dirs = [(qy+1,qx), (qy-1,qx), (qy,qx+1), (qy, qx-1)]
                for dy, dx in dirs:
                    if not (0 <= dy < len(canvas) and 0 <= dx < len(canvas[0])):
                        continue
                    if visited[dy][dx]:
                        continue
                    if canvas[dy][dx]:
                        continue
                    
                    visited[dy][dx] = True
                    queue.append((dy, dx))
            
            extents.append(extent)
    
    return extents

n, m, k = map(int,input().split())
squares = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    squares.append([(y1, x1), (y2, x2)])

canvas = [[False]*m for _ in range(n)]


for square in squares:
    paint(canvas, square)


extents = bfs(canvas)
extents.sort()
print(len(extents))
print(" ".join(map(str,extents)))