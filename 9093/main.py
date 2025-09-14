import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    string = input().rstrip()+" "
    words = [[]]
    index =  0
    for c in string:
        if c == " ":
            words[index].reverse()
            index += 1
            words.append([])
        else:
            words[index].append(c)
    print(" ".join([ "".join(word) for word in words]))