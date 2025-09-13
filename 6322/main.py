import sys
import math

input = sys.stdin.readline

cases = []

while True:
    string = input().rstrip()
    if string == "0 0 0":
        break
    cases.append(list(map(int,string.split())))

result = []
for i, c in enumerate(cases):
    xi = c.index(-1)
    a,b,c = c[0], c[1], c[2]
    print(f"Triangle #{i+1}")
    if xi == 0:
        if c <= b:
            print("Impossible.")
        else:
            r = math.sqrt(pow(c,2) - pow(b,2))
            print(f"a = {r:.3f}")
    elif xi == 1:
        if c <= a:
            print("Impossible.")
        else:
            r = math.sqrt(pow(c,2) - pow(a,2))
            print(f"b = {r:.3f}")
    elif xi == 2:
        r = math.sqrt(pow(a,2) + pow(b,2))
        print(f"c = {r:.3f}")
    print()