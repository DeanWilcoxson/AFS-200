robert_tuple = ("Robert", "Crenshaw", 1991, "Walk the Line",
          2005, "Web Developer", "Chicago, Il")
number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def getName():
  print(robert_tuple[0])


def getNums():
  print(number_tuple[1:4])


if __name__ == "__main__":
  getName()
  getNums()
