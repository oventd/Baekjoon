tests = []
while True:
    i_nums = sorted(list(map(int, input().split())))
    if i_nums[0] == i_nums[1] == i_nums[2] == 0:
        break
    tests.append(i_nums)

def check(test):
    s1 = test[0]
    s2 = test[1]
    s3 = test[2]
    if pow(s3,2) == pow(s1,2)+pow(s2,2):
        return True
    return False
for test in tests:
    if check(test):
        print("right")
    else:
        print("wrong")
