n, m = map(int, input().split())

count = 0
num = 0
l = []
while True:
    num += 1
    count += num
    l.extend([num]*num)
    if count > m:
        break
print(sum(l[n-1:m]))
