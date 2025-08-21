import bisect

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()

sum_list = []
for i in range(n):
    for j in range(i, n):
        sum_list.append(data[i] + data[j])
sum_list.sort()

result = 0

for i in range(n):
    for j in range(i + 1):
        target = data[i] - data[j]
        idx = bisect.bisect_left(sum_list, target)
        if idx < len(sum_list) and sum_list[idx] == target:
            result = max(result, data[i])

print(result)
