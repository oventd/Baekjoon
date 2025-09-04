import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
ns = []
for _ in range(N):
    n = int(input())
    ns.append(n)

ns.sort()

print(round(sum(ns) / N))

print(ns[N // 2])

counter = Counter(ns)
freq = counter.most_common()
max_freq = freq[0][1]
modes = [num for num, cnt in freq if cnt == max_freq]

if len(modes) > 1:
    print(sorted(modes)[1])
else:
    print(modes[0])

print(ns[-1] - ns[0])
