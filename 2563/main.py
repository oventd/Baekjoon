squares_count = int(input())

squares = []
for i in range(squares_count):
    xy = list(map(int, input().split()))
    squares.append({"x":xy[0], "y":xy[1]})


blank_field = [[False for i in range(100)] for i in range(100)]
count = 0

for square in squares:
    for x in range(square["x"],square["x"]+10):
        for y in range(square["y"],square["y"]+10):
            if blank_field[x][y] is False:
                blank_field[x][y] = True
                count += 1
print( count)