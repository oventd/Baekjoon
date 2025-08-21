n_max = int(input())
data = []
for _ in range(n_max):
    data.append(int(input()))
data_set = set(data)

sum_list = []
for i in range(n_max):
    for j in range(i, n_max):
        sum_list.append(data[i]+data[j])
sum_list.sort()

result = 0

for t in data[2:]:
    for sn in sum_list:
        if sn > t:
            break
        if t- sn in data_set:
            if result < t:
                result = t
print(result)