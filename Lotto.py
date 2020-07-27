import random  # importing random
import datetime  # importing datetime


lottoNumbers = []  # empty list of numbers


for i in range(0, 6):
    number = random.randint(1, 49)

    while number in lottoNumbers:

        number = random.randint(1, 49)   # Selecting random numbers from 1-49

    lottoNumbers.append(number)


lottoNumbers.sort()  # sorting lotto numbers in order

try:
 age = int(input("Enter Age Here: "))
except ValueError:
    print("Sorry please enter a number next time")
    exit()


def user_age(age):
    """
    >>> user_age(17)
    You are too young,sorry
    """
    if age >= 18:
        print("You are old enough to play,enjoy!!")
    else:
        print("You are too young to play,sorry")
        exit()


print(user_age(age))


user = []
for i in range(0, 6):  # User input asking for 6 inputs and checking if its correctly inserted
    try:
        number = int(input("Please enter a number between 1 and 49."))
    except ValueError:
        print("Please enter a number")

    if number > 49:
        print("Please enter a number below 49")
    elif number <= 0:
        print("Please enter a positive number")

    user.append(number)


user.sort()  # sorting user numbers in order

print("Today's lotto numbers are:")
print(lottoNumbers)

print("Your numbers are:")
print(user)


counter = 0  # Counter with explanation of amount of money
for number in user:
    if number in lottoNumbers:
        counter += 1
        if counter == 6:
            print("You won R10 000 000.00 for getting 6 numbers correct")
        elif counter == 5:
            print("You won R80 000.00 for getting 5 numbers correct")
        elif counter == 4:
            print("You won R20 000.00 for getting 4 numbers correct")
        elif counter == 3:
            print("You won R1000.00 for getting 3 numbers correct")
        elif counter == 2:
            print("You won R100.00 for getting 2 numbers correct")
        elif counter == 1:
            print("You won R20.00 for getting 1 numbers correct")
        else:
            print("Sorry you have no matching numbers.Please try again.")

print("You have guessed " + str(counter) + " number(s) correctly.")
print("Remember to play responsibly!!")

filename = datetime.datetime.now()


def create_file():
    # Function creates an empty file
    # %d - date, %B - month, %Y - Year
    with open(filename.strftime("%d %B %Y") + "Lotto" + "Receipt.txt", "w") as file:
        file.write("Thank you for playing lotto.The correct numbers are:" + str(lottoNumbers) + ".\n")
        file.write("Your Lotto numbers are:" + str(user) + ".\n")
        file.write("Your prize is:Nothing!!!" + ".\n")
        file.close()


create_file()









