count = int(input())
numbers = list(map(int,input().split()))

sorted_nums = sorted(set(numbers))
index_dict = {}
for i, n in enumerate(sorted_nums):
    index_dict[n] = i

result = [index_dict[x] for x in numbers]
print(" ".join(map(str,result)))
