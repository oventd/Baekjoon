GENDER = "gender"
NUMBER = "number"

BOY = 1
GIRL = 2

def boy(switches, number):
    multiple = number
    count = 1
    while True:
        if multiple > len(switches):
            break
        index = multiple - 1
        switches[index] = (switches[index] + 1) % 2
        
        count = count + 1
        multiple = number * count


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
        switches[i] = (switches[i] + 1)% 2

def main():
    switch_count = int(input())
    switches = list(map(int,input().split(" ")))

    player_count = int(input())
    players = []
    for i in range(player_count):
        gender, number = list(map(int,input().split(" ")))
        player = {GENDER:gender, NUMBER:number} 
        players.append(player)

    for i in range(player_count):
        player = players[i]
        if player[GENDER] == BOY:
            boy(switches, player[NUMBER])
        elif player[GENDER] == GIRL:
            girl(switches, player[NUMBER])

    print(" ".join(map(str, switches))[:-1])

main()