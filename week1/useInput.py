name = input("Please provide your full name:")
age = int(input("Please provide your age:"))
year = int(input("Enter the Year:"))
year100 = int(year) - int(age) + 100

print("Hello " + name + " you are " + str(age) +
      " years old, and will turn 100 in the year " + str(year100))
