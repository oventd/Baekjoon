K, N = map(int,input().split())
data = []
for i in range(K):
    data.append(int(input()))

start = 1
end = max(data)
max_length = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for num in data:
        count += num // mid
    if count < N:
        end = mid - 1
    elif count >= N:
        max_length = mid
        start = mid +1
print(max_length)