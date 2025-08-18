n, goal = map(int, input().split())

trees = list(map(int, input().split())) 

def cut(trees, num):
    result = 0
    for tree in trees:
        if tree > num:
            result += tree - num

    return result

low = 0
high = max(trees)
result = 0
while low <= high:
    mid = (low + high) // 2
    total_cut = cut(trees, mid)
    if total_cut >= goal:
        result = mid
        low = mid + 1
    else:
        high = mid -1

print(result)