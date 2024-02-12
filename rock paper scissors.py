# rock , paper and scissors game
from random import randint

#moves for the player
moves= ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0,2)]
    #this means python will take a random integer from 0 to 2
    player= input("rock, paper or scissors? (or end the game) ").lower()
    #factors in if you put ROCK in caps
    if player == "end the game":
        print("the game has ended")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose", computer, "beats", player)
        else:
            print ("You win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
         print ("check your spelling!")
