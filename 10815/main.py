N = int(input())
haves = set(map(int,input().split()))
M = int(input())
tests = list(map(int, input().split()))

result = []
for t in tests:
    if t in haves:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str,result)))

