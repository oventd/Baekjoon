dict_n, test_n = map(int,input().split())
password_dict = {}
for i in range(dict_n):
    key, value = input().split()
    password_dict[key] = value

for j in range(test_n):
    key = input()
    print(password_dict[key])