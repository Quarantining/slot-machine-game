# 0.1.2
import random

# slot machine slots function.
def pull_slots(slots): # argument is any list
    result = [] # Initialize empty list.
    for i in range(3): # iterates through list(slots) 3 times.
        item = random.choice(slots) # randomly chooses an item from the list.
        result.append(item) # appends (adds to empty list) the selected item.
    return result # returns the empty list (which now contains 3 randomly selected items).


slots = ["A", "B", "C", "D", "E", "F", "G", "H", "I"] # list of possible slots.

while True:
    user_pull = input("Press 'ENTER' to Pull Lever!") # user input to pull lever

    if user_pull == "": # if user presses enter key.
        pull = pull_slots(slots) # calls function and stores result list as var pull.
        print(pull) # prints pull

    elif user_pull == "stop": # stops program
        print("Program stopping..")
        break

    else: # for errors
        print("Error")
