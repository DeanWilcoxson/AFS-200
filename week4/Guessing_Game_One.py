import random


def guessFunction():
    play = True
    guessCount = 0
    randomNumber = int(random.randint(1, 9))
    while play != False:
        # print(randomNumber, guessCount)
        userNumber = input('Please Guess a number between 1 & 9:')
        if userNumber.lower().__contains__('exit'):
            play = False

        elif int(userNumber) < randomNumber:
            print('Try Again!! That number is too low!')
            guessCount = guessCount + 1

        elif int(userNumber) > randomNumber:
            print('Try Again!! That number is too high!')
            guessCount = guessCount + 1

        elif int(userNumber) == int(randomNumber):
            print('You got it!! Please play again!!')

            # play = False


guessFunction()
