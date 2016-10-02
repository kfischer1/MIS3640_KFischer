from random import randrange
from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

twos = [3,7,15,31,63] 
# Create the initial pile, determine the starting player and computer's strategy.

def nim():
    pile = randint(10, 100)
    turn = randrange(0, 2)
    strategy = randint(0, 1)
    hum_take= 0
    comp_take= 1
    """
    return True if the winner is human, False if winner is computer.
    """
    #creating a loop that only breaks when the pile is two and the game is decided
    while pile > 1: 
        #all of the computer's decisions will be here, when it is the computer's turn
        if turn == 0: 
            print('Computer\'s Turn')
            #the computer will only take a random amount if it is dumb or if the pile size is a power of 2 minus 1
            if strategy == 1 or pile in twos:
                comp_take = randrange(1, pile // 2 + 1)
            #if the computer is smart and making the pile a power of 2 minus 1 is a legal move, it will do so
            else: 
                for power in twos:
                    #checks which power of 2 minus 1 can be created with a legal move
                    if (pile // 2 >= pile - power) and (pile - power > 0):
                        #the computer will take however many marbles it takes to make the pile the power of 2 minus one
                        comp_take = pile - power
                        break
            pile -= comp_take
            print("The computer took %d marbles, leaving %d.\n" % (turn, pile))
            #once the computer's turn is done, it changes the turn variable
            turn = 1
        #player's turn
        else:
            #preventing the human from having a turn if the pile is size 2, because the game is decided
            if pile == 2:
                break
            print("Your turn.   The pile currently has", pile, "marbles in it.")
            hum_take = 0
            take = int(input("How many marbles will you take? "))
            #forcing the user to input a valid move
            while hum_take < 1 or hum_take > pile // 2:
                hum_take = int(input('Please input an integer between 1 and %d: ' %(pile // 2)))
            pile -= hum_take
            #update pile
            print("Now the pile has", pile, "marbles in it.\n")
            #changing the turn back to the computer
            turn = 0

    return turn == 0

if nim():
    print("You Won!")
else:
    print("The computer won!")

nim()