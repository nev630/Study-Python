import random

def game_start():
    count = 1
    random_number = random.randrange(1, 100)
    
    print('숫자 맞히기 게임을 시작합니다!')

    for i in range(100):
        user_number = input('1 ~ 99 중의 숫자 중 하나를 입력하세요! >> ')
        if (random_number == int(user_number)):
            print('정답입니다!')
            print(count, '회 시도했습니다!')
            break
        elif (random_number > int(user_number)):
            print('UP!')
            count = count + 1
        elif (random_number < int(user_number)):
            print('DOWN!')
            count = count + 1

game_start()

while True:
    game_status = input ('계속하시겠습니까? (y / n) >> ')

    if (game_status == 'y'):
        game_start()
    else:
        break