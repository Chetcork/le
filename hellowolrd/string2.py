#                   1
#         012345678901234
parrot = "norwegian blue"

print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Ne

number= "9,223;372:036 854,775;807"
print(number[1::4])
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


