import random

def play():
    player = input("what's your choice? stone 's' , paper 'p' ,scissor 'r': \n")
    opponent = random.choice(['s','p','r'])

    if player == opponent:
        print('tie!!')
    elif is_win(player,opponent):
        print('win!!')
    else:
        print('loose!!')

def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

##game logic

game_on = True
while game_on:
    print("\nLet's Play!!\n")
    print(play())
    re_game = input("Do you want to play the next game? 'y' or 'n'")
    if re_game == 'y':
        game_on = True
    else:
        game_on = False
    
