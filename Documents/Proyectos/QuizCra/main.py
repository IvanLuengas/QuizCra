import random

userChoose = 0
playerTurn = 1
gamer = ["One", "Two"]
scoreGame = [0, 0]

print("Quizcra")
print("1. Strat game")
userChoose = int(input("Choose your option: "))

if userChoose == 1:
    i = 0


    while i <= 10:
        if playerTurn == 1:
            print("Turno del jugador ", gamer[0])
            scoreGame[0] += int(random.randint(1, 10))
            playerTurn = 2
            
        if playerTurn == 2:
            print("Turno del jugador ", gamer[1])
            scoreGame[1] += int(random.randint(1, 10))
            playerTurn = 1
        i += 1

    print("The score is: ", )
    for i, j in zip(gamer, scoreGame):
        print("Gamer ", i, " score: ", j)
