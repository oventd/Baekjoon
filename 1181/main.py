import sys

input = sys.stdin.readline

N=int(input())
str_list=set()
for _ in range(N):
    st = input().rstrip()
    str_list.add((len(st),st))
str_list=sorted(list(str_list))

print("\n".join([c[1] for c in str_list]))