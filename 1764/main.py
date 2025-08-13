n, m = map(int,input().split())
listen_only = []
for _ in range(n):
    listen_only.append(input())
see_only = []
for _ in range(m):
    see_only.append(input())

set_l = set(listen_only)
set_s = set(see_only)

list_l_s = list(set_l & set_s)
list_l_s.sort()
print(len(list_l_s))
for p in list_l_s:
    print(p)