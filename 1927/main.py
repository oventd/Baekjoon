import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, n)