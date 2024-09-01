# version 0.1.6
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

    win_message = {
        "🍎": "You win 10$",
        "🥖": "You win 50$",
        "🍒": "You win 100$",
        "🍩": "You win 500$",
        "🐘": "You win 750$",
        "🌸": "You win 1000$",
        "🍇": "You win 1200$",
        "❤️": "You win 1500$",
        "🍦": "You win 2000$"
    }

    if all(item == result[0] for item in result): # checks if all items are the same as item 0. Iterates through list checking if item is == to item [0].
        return win_message.get(result[0], f"You won {result[0]}") # If all items are the same, .get correct key and return value.
    else:
        return "You didn't win."


slots = ["🍎", "🥖", "🍒", "🍩", "🐘", "🌸", "🍇", "❤️", "🍦"] # list of possible slots.

print("Press 'ENTER' to Pull Lever!")
while True:

    user_pull = input("")
    clear_screen() # clears the screen

    if user_pull == "": # if user presses enter key.
        print("Press 'ENTER' to Pull Lever!")
        slots_result = pull_slots(slots) # calls function and stores result list as var pull.
        print(slots_result)
        checks_win = check_win((slots_result))
        print(checks_win)
    elif user_pull == "stop": # stops program
        print("Program stopped.")
        break

    else: # for errors
        print("Unknown Input")