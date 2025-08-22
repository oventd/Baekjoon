import bisect
N = int(input())
data = list(map(int,input().split()))

sums = []
for i in range(len(data)):
    for j in range(i, len(data)):
        sums.append(data[i]+data[j])
sums.sort()
result = bisect.bisect_left(sums, 0)
print(sums[result])
