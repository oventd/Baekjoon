import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
result = []
for _ in range(N):
    n = int(input())
    if n == 0:
        result.append(str(-heapq.heappop(heap)) if heap else str(0))
    else:
        heapq.heappush(heap, -n)
print("\n".join(result))