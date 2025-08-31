from collections import deque

N = int(input())
queue = deque()
for n in range(N):
    usr_input = input()
    if " " in  usr_input:
        command, num = usr_input.split()
        num = int(num)
    else:
        command = usr_input

    if command == "push":
        queue.append(num)
    elif command == "pop":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if len(queue) ==0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[0])
    elif command == "back":
        if len(queue) == 0:
            print(-1)
            continue
        print(queue[-1])
