scores = [ int(input()) for _ in range(10) ]
result = 0
for n in scores:
    if result + n <=100:
        result += n
    else:
        if abs(100-result) < abs(100 - (result+n)):
            break
        else:
            result + n
        break


print(result)