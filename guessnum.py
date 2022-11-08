# NUMBER GAME EXPERIMENT
#Write a program whereby the computer will pick a number between 1 to 15 for you
# You need to guess the number.But here is the challenge.
# To win the game,you need to make a correct guess within three attempts.
# Note another point: Each time you play the game,the computer can pick a different number for you. If the attempts guess is right,let your program print the number of attempts which produced the correct guess. If it is a wrong guess after the third attempt,the user has lost the game.

# import random
# number = random.randint(1, 15)
# attempts = 0  # count no of attempts to guess the number
# guess = 0
# while guess != number:
#     guess = eval(input('Guess a number: '))
#     attempts += 1
#     if guess == number:
#         print('Correct! You used', attempts, 'attempts!')
#         break
#     elif guess < number:
#         print('Go higher!')
#     else:
#         print('Go lower!')


# This is a guess the number game.



#Write a program whereby the computer will pick a number between 1 to 15 for you
# You need to guess the number.But here is the challenge.
# To win the game,you need to make a correct guess within three attempts.
# Note another point: Each time you play the game,the computer can pick a different number for you. If the attempts guess is right,let your program print the number of attempts which produced the correct guess. If it is a wrong guess after the third attempt,the user has lost the game.

# SECOND APPROACH
# BETTER PROGRAM FOR A GUESS NUMBER GAME
import random
guesstry = 0
print('Hello! This is a Number Guess Game')
myName = input("Enter your Name:>>>>>")
number = random.randint(1, 15)
print('Play this game, ' + myName + ', Enter a number between 1 and 15.')
while guesstry < 3:
    print('Ready to make a guess?') # There are four spaces in front of print.
    guess = int(input('Enter a Guess:>>>'))
    guesstry = guesstry + 1
    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    guesstry = str(guesstry)
    print('Good job, ' + myName + '! You guessed my number in ' + guesstry + ' guesses!')
if guess != number:
        number = str(number)
        print('Game Over,You did not win!','The Correct Number is', ''  + number)
        print('Try Harder next time'  ' ' + myName + '! You guess total is', guesstry)



        #Write a program whereby the computer will pick a number between 1 to 15 for you
# You need to guess the number.But here is the challenge.
# To win the game,you need to make a correct guess within three attempts.
# Note another point: Each time you play the game,the computer can pick a different number for you. If the attempts guess is right,let your program print the number of attempts which produced the correct guess. If it is a wrong guess after the third attempt,the user has lost the game.



# Write a program whereby the computer will pick a number between 1 to 15 for you
# You need to guess the number.