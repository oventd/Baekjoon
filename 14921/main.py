import bisect
N = int(input())
data = list(map(int,input().split()))

# Two Pointers
left = 0
right = N-1
closet = float('inf')
result = None
while left < right:
    s = data[left] + data[right]
    if abs(s) < closet:
        closet = abs(s)
        result = s
    if s > 0:
        right = right-1
    elif s < 0:
        left = left+1
    elif s == 0:
        break
print(result)