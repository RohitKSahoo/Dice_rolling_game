import random
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 135) #sets the rate of speech

while True:
    try:                        # try: This block contains the code that might cause an error.
        num_dice = int(input("How many dice do you want to roll? "))
        if num_dice < 1:
            print("You must roll at least one die.")
            engine.say("You must roll at least one die.")
            engine.runAndWait()
        else:
            break
    except ValueError:          # except: If an error occurs inside the try block, the except block catches the error and executes alternative code instead of stopping the program.
        print("Please enter a valid number.")
        engine.say("Please enter a valid number.")
        engine.runAndWait()

choice = input("Roll the dice? (y/n): ").lower()

while True:
    if choice == "y":
        dice_results = [random.randint(1, 6) for _ in range(num_dice)]  # The loop runs as many times as num_dice.
                        # _ is used as a throwaway variable since we don’t need the loop index.
                        # Each iteration rolls a random die and prints the result.
        print(f'Dice rolled: {dice_results}')
        print("Thank you for playing!")
        engine.say("Thank you for playing!")
        engine.runAndWait()
        break
    elif choice == "n":
        print("Thank you for playing!")
        engine.say("Thank you for playing!")
        engine.runAndWait()
        break
    else:
        print("Invalid input!")
        engine.say("Invalid input!")
        engine.runAndWait()
        break





