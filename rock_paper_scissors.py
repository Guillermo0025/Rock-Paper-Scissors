import random as rnd

def r_p_s (player_choice):
    computer_choice = rnd.choice(['r', 'p', 's'])
    if (player_choice == 'r' and computer_choice == 'p') or (player_choice == 'p' and computer_choice == 's') or (player_choice == 's' and computer_choice == 'r'):
        player_winner = False
    else:
        player_winner = True
    
    return player_winner, computer_choice


def winner (player_winner, computer_choice, player_choice):
    while player_choice != computer_choice:
        if player_winner == True:
            print("YOU WON!")
        elif player_winner == False:
            print("YOU LOST! HA HA")
        
        break
    else:
        print("TIE")

    print(f"eleccion de la computadora: {computer_choice}")
    



player_choice = input(f"please, PLEASEEEE man, rock, paper or scissors? ('r' for rock, 'p' for paper and 's' for scissors): \n").lower()

while player_choice != 'r' and player_choice != 'p'  and player_choice != 's' :
    player_choice = input("please provide a proper command: ").lower()
else:
    print("thank you!")

player_winner, computer_choice = r_p_s(player_choice)

winner(player_winner, computer_choice, player_choice)













