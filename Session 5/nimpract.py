# You need to replace 'pass' with your code
#
from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
hum_take= 0
comp_tale= 1
# 0= human 1= computer
strategy = randint(0, 1)
#computer smart= 0 and dumb = 1
computer_pick = [3, 7, 15, 31, 63]

def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    while pile > 0:
        if turn == 1:
            #computers turn
            if pile == 1:
                return False
                # Take the last marble.                
            elif strategy == 1 or pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                while hum_take < 1 or hum_take > pile_size //2:
                    hum_take = int(input('Please pick a number of marbles between 1 and %d: ' %(pile // 2)))
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
                pass
            # Update pile
            pass
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")

            take = int(input("How many marbles will you take? "))
            # Force the user to take a legal number of marbles.
            pass

            # Update pile
            pass
            print("Now the pile has", pile, "marbles in it.\n")
            turn = COMPUTER

    return turn == COMPUTER

if nim():
    print("You Won!")
else:
    print("The computer won!")