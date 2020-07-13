from random import randint
t=["rock", "paper", "scissors"]

computer = t[randint(0,2)]

player = False

while player == False: 
    player = input('rock , paper , scissors?')
    if player == computer: 
        print('Tie')

        # these are the qualifications for rock
    elif player == "rock":
        if computer == "paper":
                print("You're a Loser", computer, "covers", player)
        else:
                print("You're a wiener", player, "smashes", computer)

        # these are the qualifications for paper
    elif player == "paper":
        if computer == "scissors":
                print("You're a Loser", computer, "cut", player)
        else:
                print("You're a wiener", player, "covers", computer)

        # these are the qualifications for scissors
    elif player == "scissors":
        if computer == "rock":
                print("You're a Loser", computer, "smashes", player)
        else:
                print("You're a wiener", player, "cuts", computer)
    else:
                print("thats not a valid play try again")
player = False