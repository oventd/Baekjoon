n, m = map(int,input().split())
poketmons = {}
for i in range(n):
    name = input()
    poketmons[name] = i + 1
    poketmons[i + 1] = name
print("--------")
for _ in range(m):
    test = input()
    try:
        print(poketmons.get(int(test)))
    except:
        print(poketmons.get(test))
