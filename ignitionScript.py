import random
import time
subjects = ["Cities & Capitals (1)", "Math: Operations (2)", "Python (3)"]

def mathFunction():
    print("-------------------------------------------------------")
    print("Welcome, I'm your math assistant.")
    time.sleep(2)
    answer = input("Are you ready for the quiz? (yes/no): ")
    if answer == "yes":
        print("-------------------------------------------------------")
        answer = input("Would you like to practice addition (1), subtraction (2), multiplication (3), division (4): ")

        if answer == "1":
            print("-------------------------------------------------------")
            points = 0
            for x in range(7):
                randomVar = random.randint(1,50)
                randomVar2 = random.randint(1,50)
                sumOfRand = randomVar + randomVar2
                print("What is..")
                print(randomVar)
                print("+")
                answer = int(input(randomVar2))
                if answer == sumOfRand:
                    print("Correct!")
                    points = points + 1
                else:
                    print("Incorrect")
            print("You had", points, "/ 7 points")
            percentScore = points / 7
            print("You scored", round(percentScore * 100), "%")

        if answer == "2":
            print("-------------------------------------------------------")
            points = 0
            for x in range(7):
                randomVar = random.randint(1,50)
                randomVar2 = random.randint(1,50)
                sumOfRand = randomVar - randomVar2
                print("What is..")
                print(randomVar)
                print("-")
                answer = int(input(randomVar2))
                if answer == sumOfRand:
                    print("Correct!")
                    points = points + 1
                else:
                    print("Incorrect")
            print("You had", points, "/ 7 points")
            percentScore = points / 7
            print("You scored", round(percentScore * 100), "%")

        if answer == "3":
            print("-------------------------------------------------------")
            points = 0
            for x in range(7):
                randomVar = random.randint(1,14)
                randomVar2 = random.randint(1,14)
                sumOfRand = randomVar * randomVar2
                print("What is..")
                print(randomVar)
                print("*")
                answer = int(input(randomVar2))
                if answer == sumOfRand:
                    print("Correct!")
                    points = points + 1
                else:
                    print("Incorrect")
            print("You had", points, "/ 7 points")
            percentScore = points / 7
            print("You scored", round(percentScore * 100), "%")

        if answer == "4":
            print("-------------------------------------------------------")
            points = 0
            for x in range(7):
                randomVar = random.randint(30,50)
                randomVar2 = random.randint(1,10)
                sumOfRand = randomVar / randomVar2
                print("What is..")
                print(randomVar)
                print("/")
                answer = float(input(randomVar2))
                if answer == sumOfRand:
                    print("Correct!")
                    points = points + 1
                else:
                    print("Incorrect")
            print("You had", points, "/ 7 points")
            percentScore = points / 7
            print("You scored", round(percentScore * 100), "%")
            
    if answer == "no":
        print("We will resort you back to the beginning.")
        time.sleep(2)
        introFunction()

def codeFunction():
    print("-------------------------------------------------------")
    print("Welcome, I'm your Python assistant!")
    time.sleep(2)
    answer = input("Are you ready for the quiz? (yes/no)")
    if answer == "yes":
        print("-------------------------------------------------------")
        points = 0
        print("How do you find the length of a string?")
        answer = input("Is it: len(str): (1),  length(str): (2), findlen(str) (3)")
        if answer == "1":
            print("Correct")
            points = points + 1
        else:
            print("Incorrect")

        print("Who invented Python?")
        answer = input("Is it: Bjarne Stroustrup (1), James Gossling (2), Guido Van Rossum (3)")
        if answer == "3":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect..")

        print("Which is NOT a loop in Python?")
        answer = input("Is it: For (1), While (2), Do-While (3)")
        if answer == "3":
            print("Correct")
            points = points + 1
        else:
            print("Incorrect")

        print("What is the keyword used to define a function?")
        answer = input("Is it: define (1), def (2), dfine (3)")
        if answer == "2":
            print("Correct")
            points = points + 1
        else:
            print("Incorrect!")

        print("What keyword is used to display text?")
        answer = input("Is it: print (1), input (2), enter (3)")
        if answer == "1":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("You had", points, "/ 5 total points")
        percentScore = points / 5
        print("You scored", round(percentScore * 100), "%")
        
    if answer == "no":
        print("We will resort you back to the beginning.")
        time.sleep(2)
        introFunction()
        
        
def geoFunction():
    print("-------------------------------------------------------")
    print("Welcome, I'm your geography assistant.")
    time.sleep(2)
    answer = input("Are you ready for the quiz? (yes/no)")
    if answer == "yes":
        print("-------------------------------------------------------")
        points = 0
        print("What is the capital of Canada?")
        answer = input("Is it: Ottawa (1), Toronto (2), Montreal (3)")
        if answer == "1":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("What is the capital of the USA?")
        answer = input("Is it: Los Angeles (1), Washington DC (2), New York City (3)")
        if answer == "2":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("How many provinces and territories does Canada have?")
        answer = input("10 (1), 13 (2), 12 (3)")
        if answer == "2":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("How many states are there in America?")
        answer = input("51 (1), 45 (2), 50 (3)")
        if answer == "3":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("What is the most populated Canadian city?")
        answer = input("Calgary (1), Vancouver (2), Toronto (3)")
        if answer == "3":
            print("Correct!")
            points = points + 1
        else:
            print("Incorrect")

        print("-------------------------------------------------------")
        print("You will have 5 guesses for the following question.")
        print("Try to get as many correct answers as possible.")
        print("You will get a point for every correct guess you complete.")
        time.sleep(5)
        print("-------------------------------------------------------")
        for x in range(5):
            answer = input("Name a province in Canada: ")
            if answer in ("Alberta", "British Columbia", "B.C.", "BC", "Manitoba", "New Brunswick", "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Quebec", "PEI", "P.E.I.", "P.E.I", "Prince Edward Island", "Saskatchewan"):
                print("Correct!")
                points = points + 1
            else:
                print("Incorrect")
    
        print("You had", points, "/ 10 total points")
        percentScore = points / 10
        print("You scored", round(percentScore * 100), "%")
        
    if answer == "no":
        print("We will resort you back to the beginning.")
        time.sleep(2)
        introFunction()
        
            
def introFunction():
    print("-------------------------------------------------------")
    print("This project was made by Fawz and Fiza Mehfil,\nfor the Ignition Hacks 2020 Hackathon.")
    print("Text will be outputted every few seconds.")
    answer = input("Type 'exit' to exit, or press the enter key to continue: ")
    if answer.lower().strip() == "exit":
        print("Goodbye.")
        print("-------------------------------------------------------")
    else:
        print("-------------------------------------------------------")
        print("Welcome to Quizzard || Your Personal Quiz Wizard")
        time.sleep(1)
        print("We help you master a subject of your choice!")
        time.sleep(1)
        print("We'll give you a quiz based on the subject you choose.")
        time.sleep(1)
        print("")
        print("Please select one of the following subjects: ")
        answer = input(subjects)
        if answer == "1":
            geoFunction()
        if answer == "2":
            mathFunction()
        if answer == "3":
            codeFunction()

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    introFunction()
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
print("Thanks for playing!")
print("-------------------------------------------------------")
