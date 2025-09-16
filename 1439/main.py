import sys

input = sys.stdin.readline

string = input().rstrip()
string = "0" + string if string[0] == "1" else "1" + string

c01 = string.count("01")
c10 = string.count("10")

print(c01 if c01 < c10 else c10)
