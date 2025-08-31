from collections import deque
import sys

N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
    command_input = sys.stdin.readline().rstrip()
    if " " in command_input:
        command, num = command_input.split()
    else:
        command = command_input
    
    if command == "push":
        stack.append(num)
    elif command == "pop":
        print(stack.pop() if stack else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        print(stack[-1] if stack else -1)
