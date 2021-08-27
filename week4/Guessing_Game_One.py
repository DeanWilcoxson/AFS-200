import random
randomNumber = random.randint(1, 9)
userNumber = input('Please Guess a number:')
guessCount = 0

while (int(userNumber) >= 1) & (int(userNumber) <= 9) & (userNumber != 'exit'):
    if (int(userNumber) < int(randomNumber)):
        print('That number is too low!')
        userNumber = int(input('Please Guess a number:'))
        guessCount + int(1)

    elif (int(userNumber) > int(randomNumber)):
        print('That number is too high!')
        userNumber = int(input('Please Guess a number:'))
        guessCount + int(1)

    elif (int(userNumber) == int(randomNumber)):
        print('RIGHT ON THE MONEY!! GOOD GUESS!!! Type "Exit" to close the game.')
        userNumber = input(
            'Type "Exit" to close the game, Please play again soon!:')
        guessCount + int(1)
        print('Total Guesses: ' + str(guessCount))
