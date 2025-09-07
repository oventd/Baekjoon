import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == ".":
        break
    stack = []
    passed = False
    for c in string:
        if c in "([":
            stack.append(c)
        elif c == ")":
            if not stack or stack.pop() != "(":
                passed = True
                break
        elif c == "]":
            if not stack or stack.pop() != "[":
                passed = True
                break
    if passed or stack:
        print("no")
    else:
        print("yes")

