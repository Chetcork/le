if 0:
    print("True")
else:
    print("False")

name = input("please enter your name: ")
# if name:
if name != "":
    print("hello, {}".format(name))
else:
    print("are you the man with no name?")