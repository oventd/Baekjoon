from collections import deque
import sys 

input = sys.stdin.readline 

N = int(input())
queue = deque()

for _ in range(N):
    usr_input = input()
    if " " in  usr_input:
        command, num = usr_input.split()
        num = int(num)
    else:
        command = usr_input

    if command == "push":
        queue.append(num)
    elif command == "pop":
        print(queue.popleft() if queue else -1)
    elif command == "size":
        print(len(queue))
    elif command == "empty":
            print(1 if queue else 0)
    elif command == "front":
        print(queue[0] if queue else -1)
    elif command == "back":
        print(queue[-1] if queue else -1)
