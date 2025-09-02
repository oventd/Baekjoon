import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0

for _ in range(N):
    n = int(input())
    cnt = 1
    
    while stack and stack[-1][0] <= n:
        result += stack[-1][1]
        if stack[-1][0] == n:
            cnt += stack[-1][1]
        stack.pop()
    
    if stack:
        result += 1
    
    stack.append((n, cnt))

print(result)
