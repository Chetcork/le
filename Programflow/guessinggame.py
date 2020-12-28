answer = 5

print("please guess number bettween 1 and 10: ")
guess = int(input())

if guess == answer:
    print("you got it first time")
else:
    if guess < answer:
        print("please guess higher")
    else:  # guess mst be greather than answer
        print("polease guess lower")
    guess = int(input())
    if guess < answer:
        print("well done, you guessed correctly")
    else:
        print("sorry, you have not guessed correctly")

# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("sorry, you have not guessed corretly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guess it")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
#     print("you got it first time")
