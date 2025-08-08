BOY = 1
GIRL = 2

def boy(switches, number):
    for index in range(number-1, len(switches), number):
        switches[index] ^= 1

def girl(switches, number):
    if number < 1 or number > len(switches):
        return
    
    front_index = number - 1
    back_index = number - 1
    while True:
        if front_index-1 < 0 or back_index+1 >= len(switches):
            break
        if switches[front_index-1] != switches[back_index+1]:
            break
        front_index = front_index - 1
        back_index = back_index + 1
    for i in range(front_index,back_index+1):
        switches[i] ^= 1

def main():
    switch_count = int(input())
    switches = list(map(int,input().split()))

    player_count = int(input())
    for i in range(player_count):
        gender, number = list(map(int,input().split()))

        if gender == BOY:
            boy(switches, number)
        elif gender == GIRL:
            girl(switches, number)

    for i in range(0, switch_count, 20):
        print(" ".join(map(str, switches[i:i+20])))

main()