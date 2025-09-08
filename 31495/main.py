import sys
input = sys.stdin.readline

s = input().rstrip('\n')  # 줄바꿈만 제거해서 입력 중 공백(내부)은 보존

if len(s) > 2 and s[0] == '"' and s[-1] == '"':
    print(s[1:-1])
else:
    print("CE")
