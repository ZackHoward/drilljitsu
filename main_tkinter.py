from tkinter import *
from tkinter import ttk
import random
my asshole is bleached
# Lists of submssions based on body part and difficulty
# Might be able to compile body part and difficulty into same list instead NESTED LISTS
arm = [
    'Straight Armbar', 'Americana Armbar', 'Kimura Armlock', 'Biceps Slicer', 'Omoplata', 'Wristlock', 'Inverse Armbar', 'Marceloplata', 'Baratoplata', 'Monoplata', 'Mir Lock', 'Hammerlock' 
]

leg = [
    'Straight Ankle Lock', 'Kneebar', 'Knee Slicer', 'Figure 4 Toehold', 'Heel Hook', 'Reverse Heel Hook', 'Banana Split Hiplock', 'Calf Slicer' 
]

neck = [
    'Rear Naked Choke', 'Triangle Choke', 'Bow and Arrow Choke', 'Ezekiel Choke', 'Guillotine', 'Cross Collar Choke', 'Short Choke', 'Baseball Choke', 'D\'Arce Choke', 'Head and Arm Choke', 'North-South Choke', 'Crucifix Choke', 'Thrust Choke', 'Anaconda Choke', 'Neck Crank', 'Twister', 'Peruvian Necktie', 'Loop Choke', 'Papercutter Choke', 'Gogoplata', 'Step Over Choke', 'Von Flue Choke', 'Lapel Half Nelson'
]

hard = ['Biceps Slicer', 'Marceloplata', 'Baratoplata', 'Monoplata', 'Hammerlock', 'Knee Slicer', 'Reverse Heel Hook', 'Banana Split Hip Lock', 'Crucifix Choke', 'Anaconda Choke', 'Peruvian Necktie', 'Gogoplata', 'Step Over Choke', 'Von Flue Choke', 'Lapel Half Nelson'
    
]

intermediate = ['Omoplata', 'Wristlock','Inverse Armbar', 'Mir Lock', 'Straight Ankle Lock', 'Kneebar', 'Figure 4 Toehold', 'Heel Hook', 'Calf Slicer', 'Bow and Arrow Choke', 'Ezekiel Choke', 'Guillotine', 'Baseball Choke', 'D\'Arce Choke', 'Head and Arm Choke', 'North-South Choke', 'Thrust Choke', 'Neck Crank', 'Twister', 'Loop Choke', 'Papercutter Choke', 
    
]

beginner = ['Straight Armbar', 'Americana Armbar', 'Kimura Armlock', 'Rear Naked Choke', 'Triangle Choke', 'Cross Collar Choke', 'Short Choke', 
    
]

# Function for generating a random submission to practice; removes random submission from lists after
def practice_submission_body():
    body_parts = body_part.get()
    if body_parts == 'all':
        return submission.set(random.choice(arm + leg + neck))
    elif body_parts == 'arm':
        return submission.set(random.choice(arm))
    elif body_parts == 'leg':
        return submission.set(random.choice(leg))
    elif body_parts == 'neck':
        return submission.set(random.choice(neck))
    else:
        return

# Function for generating a random submission based on difficulty
def practice_submission_difficulty():
    difficulty = body_part.get()
    if difficulty == 'beginner':
        return submission.set(random.choice(beginner))
    elif difficulty == 'intermediate':
        return submission.set(random.choice(intermediate))
    elif difficulty == 'hard':
        return submission.set(random.choice(hard))
    else:
        return
    
# Function for adding submissions into lists    
def add_submission():
    add_which = input('Would you like to add an arm, leg, or neck submission?: ')
    if add_which == 'arm':
        return arm.extend(input('What arm submission would you like to add?: '))
    elif add_which == 'leg':
        return leg.extend(input('Which leg submission would you like to add?: '))
    elif add_which == 'neck':
        return neck.extend(input('Which neck submission would you like to add?: '))
    else:
        return 'Please choose a valid submission to add: arm, leg or neck.'

# Function for removing submissions from lists
def remove_submission():
    remove_which = input('Which submission would you like to remove?: ')
    if remove_which in arm:
        return arm.remove(remove_which)
    elif remove_which in leg:
        return leg.remove(remove_which)
    elif remove_which in neck:
        return neck.remove(remove_which)
    else:
        return 'The submission you entered is not in the application.'
    
root = Tk()
root.title("Drill-Jitsu")

mainframe = ttk.Frame(root, padding = '3 3 12 12')
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

body_part = StringVar()
body_part_entry = ttk.Entry(mainframe, width = 10, cursor = 'pirate', textvariable = body_part)
body_part_entry.grid(column = 3, row = 1, sticky = (W, E))

#difficulty = StringVar()
#difficulty_entry = ttk.Entry(mainframe, width = 10, cursor = 'pirate', textvariable = difficulty)
#difficulty_entry.grid(column = 3, row = 3, sticky = (W, E))

submission = StringVar()
ttk.Label(mainframe, textvariable = submission).grid(column = 3, row = 4, stick = (W, E))

ttk.Label(mainframe, text = 'Enter body part or difficulty').grid(column = 2, row = 1, sticky = W)

#ttk.Label(mainframe, text = 'or').grid(column = 2, row = 2, sticky = W)

#ttk.Label(mainframe, text = 'Enter difficulty').grid(column = 2, row = 3, sticky = W)

ttk.Button(mainframe, text = 'DRILL', command = lambda:[(practice_submission_body(), practice_submission_difficulty())]).grid(column = 2, row = 4, sticky = W)

# Look into "list comprehension"
# Look into OOP for adding and removing moves

for child in mainframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

body_part_entry.focus()
root.bind('<Return>', submission)

root.mainloop()