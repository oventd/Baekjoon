n_num = int(input())
ns = set(map(int, input().split()))
m_num = int(input())
ms = list(map(int, input().split()))

for m in ms:
    print(1 if m in ns else 0)