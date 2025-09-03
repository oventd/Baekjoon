import sys

input = sys.stdin.readline

def check_vps(string):
    stack = []
    for c in string:
        if c=="(":
            stack.append(c)
        elif c==")":
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

N = int(input())
for _ in range(N):
    print(check_vps(input().rstrip("\n")))