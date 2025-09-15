import sys
input = sys.stdin.readline

N = int(input())

texts = set()
for _ in range(N):
    text = input().rstrip()
    texts.add(text)
    if text[::-1] in texts:
        print(f"{len(text)} {text[len(text)//2]}")
        break
