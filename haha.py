import  random
player_count = 0
computer_count = 0

def playerChoice() :
    player_choice = input("Enter r for rock , p for paper and s for scissors(press x to exit) : ")
    if player_choice == 'r' :
        print('You chose rock')
    elif player_choice == 'p' :
        print('You chose paper ')
    elif player_choice == 's' :
        print('You chose scissors')
    elif player_choice == 'x' :
        print("Thankyou")
        exit()

    else :
        print("Sorry i don't understand, please try again")
        playerChoice()
    return player_choice


def computerChoice() :
    computer_choice = random.randint(1,3)
    if computer_choice == 1 :
        computer_choice = 'r'
    elif computer_choice == 2 :
        computer_choice = 'p'
    elif computer_choice == 3 :
        computer_choice = 's'

    return computer_choice

def count():
    print("")
    print(' Player Wins = ' ,player_count)
    print(' Computer Wins = ', computer_count)
    print("")


while True :
    player_choice = playerChoice()
    computer_choice = computerChoice()
    if player_choice == 'r':
        if computer_choice == 'r':
            print("Computer also chose rock . Its a tie ")
            count()
        elif computer_choice == 'p' :
            print("Computer chose paper . Computer wins")
            computer_count += 1
            count()
        elif computer_choice == 's' :
            print("Computer chose scissors . You win ")
            player_count += 1
            count()



    if player_choice == 'p':
        if computer_choice == 'p':
            print("Computer also chose paper . Its a tie ")
            count()
        elif computer_choice == 's' :
            print("Computer chose scissors . Computer wins")
            computer_count += 1
            count()
        elif computer_choice == 'r' :
            print("Computer chose rock . You win ")
            player_count += 1
            count()

    if player_choice == 's':
        if computer_choice == 's':
            print("Computer also chose scissors . Its a tie ")
            count()
        elif computer_choice == 'r' :
            print("Computer chose rock . Computer wins")
            computer_count += 1
            count()
        elif computer_choice == 'p' :
            print("Computer chose paper . You win ")
            player_count += 1
            count()