import random

def pull_slots(slots): # argument is any list
    result = [] # empty list.
    for i in range(3): # iterates through list 3 times.
        item = random.choice(slots) # randomly chooses an item from the list.
        result.append(item) # appends (adds to empty list) the selected item.
    return result # returns the empty list (which now contains 3 randomly selected items).

slots = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
pull = pull_slots(slots)
print(pull)
