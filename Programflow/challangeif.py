name = input("What is your name? ")
age = int(input("How old are you? "))
if 18 <= age < 30:
    print("You are welcome {0}".format(name))
else:
    print("access denied")