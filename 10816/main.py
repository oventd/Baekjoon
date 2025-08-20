n_max = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
tests = list(map(int, input().split()))

def bs(n):
    low = 0
    high = len(nums)
    while low < high:
        index = (low + high)//2
        if nums[index] == n:
            return index
        elif nums[index] > n:
            high = index - 1
        elif nums[index] < n:
            low = index +1
    return -1
def get_count(n):
    index = bs(n)
    if index == -1:
        return 0
    count = 1
    low = index-1
    high = index+1
    while low > 0:
        if nums[low] == n:
            low -= 1
            count += 1
        else:
            break
    while high<len(nums):
        if nums[high] == n:
            high += 1
            count += 1
        else:
            break
    return count
            

result = []
for test in tests:
    result.append(get_count(test))

print(" ".join(map(str, result)))