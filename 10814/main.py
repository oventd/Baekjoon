N = int(input())
people =[]
for i in range(N):
    age, name =input().split()
    people.append((int(age),name))
people.sort(key=lambda x: x[0])
for p in people:
    print(" ".join(map(str,p)))