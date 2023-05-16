# Written by Sina Pirzadeh

game_Round = int(input('Enter the Game Round : '))
plyer_1 = 0
plyer_2 = 0


for i in range(game_Round):
    print('Help => [R : Rock , P : Paper , S : Scissor] ')
    p_1 = input("Plyer 1 => Enter your move : ")
    p_2 = input("Plyer 2 => Enter your move : ")

    if p_1 == 'R' and p_2 == 'P' or p_1 == 'P' and p_2 == 'S' or p_1 == 'S' and p_2 == 'R':
        print("plyer 2 Wins this Round!")
        plyer_2 += 1
    elif p_1 == 'R' and p_2 == 'S' or p_1 == 'P' and p_2 == 'R' or p_1 == 'S' and p_2 == 'P':
        print("plyer 1 Wins this Round!")
        plyer_1 += 1
    elif p_1 == p_2:
        print('You have Tied this Round')
        plyer_2 += 1
        plyer_2 += 1
    else:
        print('this number is not set 😒')


if plyer_1 >= plyer_2:
    print('plyer1 is win of Game => ', plyer_1)
elif plyer_1 <= plyer_2:
    print('plyer2 is win of Game => ', plyer_2)
else:
    print('the Game equalised')
