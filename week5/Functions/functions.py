measuredString = input("Please enter a simple sentence: \n\t")
uppercaseLetters = 0
lowercaseLetters = 0
for letter in range(len(measuredString)):
    if(measuredString[letter] >= 'a' and measuredString[letter] <= 'z'):
        lowercaseLetters += 1

    elif(measuredString[letter] >= 'A' and measuredString[letter] <= 'Z'):
        uppercaseLetters += 1
print('Lower case letters =', lowercaseLetters)
print('Upper case letters =', uppercaseLetters)
