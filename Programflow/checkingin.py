parrot = "Norwegian Blue"

letters = input("enter a character: ")

if letters in parrot:
    print("{} is in {}".format(letters, parrot))
else:
    print("i don't need that letter")