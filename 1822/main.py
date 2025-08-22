a_n, b_n = map(int, input().split())
a_l = set(map(int,input().split()))
b_l = set(map(int,input().split()))

result = sorted(list(a_l - b_l))
print(len(result))
print(" ".join(map(str,result)))