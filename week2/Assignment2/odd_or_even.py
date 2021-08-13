#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
userNum = int(input("Please Enter your Favorite Number: "))
def OddorEven():
    if userNum % 2 == 0:
        print(str(userNum) + " is Even")
    else:
        print(str(userNum) + " is Odd")
OddorEven()

# ExtraCredit
#If the number is a multiple of 4, print out a different message.
def ifMultipleOf4():
    if userNum % 4 == 0:
        print(str(userNum) + " is a multiple of Four.")
    else:
        print(str(userNum) + " is not a multiple of Four.")
ifMultipleOf4()

#Ask the user for two numbers: one number to check(call it num) and one number to divide by(check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
def checkNums(number1, number2):
    if number1 % number2 == 0:
        print(str(number1) + " is divisible by " +
              str(number2) + "  =  " + str(int(number1) / int(number2)))
    else:
        print(str(number1) + " is not divisible by " + str(number2) +
              " evenly " + "  =  " + str(int(number1) / int(number2)))
checkNums(num1, num2)
