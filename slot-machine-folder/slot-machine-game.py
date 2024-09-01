# version 0.1.7
import random
import os

def clear_screen(): # function to clear screen.
    os.system('cls' if os.name == 'nt' else 'clear')


def betting(wallet): # takes wallet as argument
    bet_amount = 10
    while True:
        menu = """- - - - - - - - - - - - - - - - - 
press 'ENTER' to add 10$
type 'max' to bet maximum (500$)
type 'done' to stop betting
- - - - - - - - - - - - - - - - - 
"""
        clear_screen()
        print(menu)
        amount = input("> ")

        if amount == 'done': # tells user current betting amount and ends function
            clear_screen()
            print(menu)
            print(f"You are currently Betting {bet_amount}$")
            return bet_amount # returns bet_amount

        elif bet_amount >= 500: # checks if bet is higher than max (500).
            clear_screen()
            print(menu)
            print(f"You are currently Betting {bet_amount}$")
            print("You can not bet any higher.")

        elif bet_amount >= 10: # checks if bet is higher than min (10).

            if amount == "": # adds 10 to bet when user presses 'ENTER'
                clear_screen()
                print(menu)
                bet_amount += 10
                print(f"You are currently Betting {bet_amount}$")

            elif amount == "max": # sets bet to 500 when user types 'max'
                clear_screen()
                print(menu)
                bet_amount = 500
                print(f"You are currently Betting {bet_amount}$")

            else: # for errors
                clear_screen()
                print(menu)
                print("Error")
        else: # for errors
            clear_screen()
            print("Error")

# slot machine slots function.
def pull_slots(slots, bet): # argument is any list
    result = [] # Initialize empty list.
    bet_amount = bet
    for i in range(3): # iterates through list(slots) 3 times.
        item = random.choice(slots) # randomly chooses an item from the list.
        result.append(item) # appends (adds to empty list) the selected item.
    return result, bet_amount # returns the empty list (which now contains 3 randomly selected items).


def check_win(slots_result): # checks if result is a win or lose.

    win_earnings = {
        "🍎": 100,
        "🥖": 500,
        "🍒": 1000,
        "🍩": 5000,
        "🐘": 7500,
        "🌸": 10000,
        "🍇": 15000,
        "❤️": 20000,
        "🍦": 50000
    }


    if all(item == slots_result[0] for item in slots_result): # checks if all items are the same as item 0. Iterates through list checking if item is == to item [0].
        earnings = win_earnings.get(slots_result[0], 0) # sets earnings as int var.
        win_message = f"You won {earnings}$" # prints win message with earnings.
        return win_message, earnings # returns win_message and earnings.
    else:
        return 0, "You didn't win." # returns 0$ and tells user they didn't win.


slots = ["🍎", "🥖", "🍒", "🍩", "🐘", "🌸", "🍇", "❤️", "🍦"] # list of possible slots.

wallet = 1000
bet = 10

while True:
    # updates menu each iteration to ensure wallet is updated.
    menu = f"""- - - - - - - - - - - - - - - - - 
    my wallet: {wallet}

    Press 'ENTER' to Pull Lever! 
    Type 'BET' to wager.
    - - - - - - - - - - - - - - - - - 
    """
    print(menu) # prints menu

    user_pull = input("")
    clear_screen() # clears the screen
    if wallet > 0: # checks if wallet is empty.

        if user_pull == "": # if user presses enter key.
            print(menu)
            slots_result, bet_amount = pull_slots(slots, bet) # calls function and stores result list as var pull.
            wallet = wallet - bet_amount # updates wallet value by subtracting bet
            print(slots_result) # prints the slot machine result

            earnings, win_message = check_win((slots_result)) # unpacks the earnings (if any) and win message.
            wallet += earnings # updates wallet (if user won anything).
            print(win_message) # prints win message.

        elif user_pull == "bet": # allows user to wager bet.
            bet = betting(wallet)
            wallet -= bet # updates bet var

        elif user_pull == "stop": # stops program
            print("Program stopped.")
            break

        else: # for errors
            print("Unknown Input")

    elif wallet <= 0: # if wallet is empty
        print("You are out of money!")
        print(f"Current balance {wallet}")

    else: # for errors
        print("Error")