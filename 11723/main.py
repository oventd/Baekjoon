n = int(input())
result = []

def add(num):
    if num in result:
        return
    result.append(num)
def remove(num):
    if num not in result:
        return
    result.remove(num)
def check(num):
    if num in result:
        print(1)
        return
    print(0)
def toggle(num):
    if num in result:
        result.remove(num)
    elif num not in result:
        result.append(num)

def all():
    result.clear()
    for i in range(1,21):
        result.append(i)

def empty():
    result.clear



for i in range(n):
    inputs = input().split()
    if len(inputs) == 2:
        command = inputs[0]
        number = int(inputs[1])
        exec(f"{command}({number})")
    else:
        command = inputs[0]
        exec(f"{command}()")
    