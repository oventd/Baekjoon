N = int(input())
nums = set()
for i in range(N):
    nums.add(int(input()))
nums = sorted(list(nums))
for n in nums:
    print(n)
