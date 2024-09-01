# version 0.1.5
import random
import os


def clear_screen(): # function to clear screen.
    os.system('cls' if os.name == 'nt' else 'clear')

# slot machine slots function.
def pull_slots(slots): # argument is any list
    result = [] # Initialize empty list.
    for i in range(3): # iterates through list(slots) 3 times.
        item = random.choice(slots) # randomly chooses an item from the list.
        result.append(item) # appends (adds to empty list) the selected item.
    return result # returns the empty list (which now contains 3 randomly selected items).


def check_win(result): # checks if result is a win or lose.
    if all(item == result[0] for item in result): # checks if all items are the same as item 0. Itterates through list checking if item is == to item [0].
        if result[0] == "🍎": # checks which emoji won.
            print("You win 10$")
        if result[0] == "🥖":
            print("You win 100$")
        if result[0] == "🍒":
            print("You win 500$")
        if result[0] == "🍩":
            print("You win 1000$")
        if result[0] == "🐘":
            print("You win 1500$")
        if result[0] == "🌸":
            print("You win 2000$")
        if result[0] == "🍇":
            print("You win 5000$")
        if result[0] == "❤️":
            print("You win 7500$")
        if result[0] == "🍦":
            print("You win 10,000$")
    else:
        print("You lose.")


slots = ["🍎", "🥖", "🍒", "🍩", "🐘", "🌸", "🍇", "❤️", "🍦"] # list of possible slots.

print("Press 'ENTER' to Pull Lever!")
while True:
    user_pull = input("")
    clear_screen() # clears the screen

    if user_pull == "": # if user presses enter key.
        print("Press 'ENTER' to Pull Lever!")
        result = pull_slots(slots) # calls function and stores result list as var pull.
        print(result)
        check_win((result))

    elif user_pull == "stop": # stops program
        print("Program stopping..")
        break

    else: # for errors
        print("Error")