N, M = map(int,input().split())

n_g = {}
g_n = {}

for _ in range(N):
    group_name = input()
    group_count = int(input())
    g_n[group_name] = []
    for _ in range(group_count):
        name = input()
        n_g[name] = group_name
        g_n[group_name].append(name)

for _ in range(M):
    test_str = input()
    test_case = int(input())
    if test_case == 1:
        print(n_g[test_str])
    elif test_case == 0:
        for n in g_n[test_str]:
            print(n)
    