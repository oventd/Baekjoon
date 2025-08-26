import bisect
N = int(input())
tests = sorted(list(map(int,input().split())))

groups = []
for c_i, c in enumerate(tests):
    left = 0
    right = N-1
    while left <= right:
        s = tests[left] + tests[right] + c
        if s >= 0:
            if s == 0 and c_i != left != right:
                group = sorted([c_i,left,right])
                if group not in groups:
                    groups.append(group)
            right -= 1
        elif s < 0:
            left += 1
    
print(len(groups))