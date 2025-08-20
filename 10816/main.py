from collections import Counter

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
tests = list(map(int, input().split()))

count = Counter(nums)
print(' '.join(str(count[x]) for x in tests))
