###
# A program that enables a user to challenge a computer.
# The computer throws dice. Then, the user then tries to guess
# the number from dice by entering a number from 1 to 6
# from the keyboard. If the user has guessed the number
# from the dice, the computer prints True. Otherwise,
# the computer prints False.
#
import random
# COMPUTER TURN
print('Throwing a dice...')
print('...')
computer = random.randint(1, 6)
print('Guess a number (1 to 6)')
# YOUR TURN
print(computer)
you = int(input("" #koniecznie tutaj int, inaczej nie dziala bo wtedy to tekst a nie liczba
            ""))

you_won = computer==you

print(f'You won: {you_won}')