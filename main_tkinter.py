# Look into "list comprehension"
# Might be able to compile body part and difficulty into same list instead (NESTED LISTS)

from tkinter import *
from tkinter import ttk
import random
import re
import webbrowser

root = Tk()
root.title("Drill-Jitsu")
root.iconbitmap(r"C:\Users\zhowa\Desktop\Code\Projects\Drilljitsu\drilljitsu_icon.ico")

tabs = ttk.Notebook(root)

tab1 = ttk.Frame(tabs, padding = '3 3 12 12')
tab1.grid(column = 0, row = 0, sticky = (N, W, E, S))

tab2 = ttk.Frame(tabs, padding = '3 3 12 12')
tab2.grid(column = 0, row = 0, sticky = (N, W, E, S))

tabs.add(tab1, text = 'App')
tabs.add(tab2, text = 'Settings')
tabs.pack(expand = 1, fill = 'both')

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

submission_list = StringVar()
submission_list.set('All')
drop_menu = OptionMenu(tab1, submission_list, 'All', 'Arm', 'Leg', 'Neck', 'Beginner', 'Intermediate', 'Hard')
drop_menu.grid(column = 3, row = 1, sticky = W)

submission = StringVar()
output_submission = ttk.Label(tab1, textvariable = submission, font = 8, borderwidth = 4, width = 19).grid(column = 3, row = 4, stick = (W, E))

selection_label = ttk.Label(tab1, text = 'Select body part or difficulty').grid(column = 2, row = 1, sticky = W)

drill_button = ttk.Button(tab1, text = 'DRILL', width = 20, command = lambda:[(practice_submission_body(), practice_submission_difficulty())]).grid(column = 2, row = 4, sticky = W)

search_youtube_button = ttk.Button(tab1, text = 'LEARN', width = 20, command = lambda: search_youtube()).grid(column = 2, row = 5, sticky = W)

youtube_label = ttk.Label(tab1, text = 'Click LEARN!').grid(column = 3, row = 5, sticky = (W, E))

for child in tab1.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)
    
for child in tab2.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

drop_menu.focus()

# Lists of submissions based on body part and difficulty
arm = [
    'Straight Armbar', 'Americana Armbar', 'Kimura Armlock', 'Biceps Slicer', 'Omoplata', 'Wristlock', 'Inverse Armbar', 'Marceloplata', 'Baratoplata', 'Monoplata', 'Mir Lock', 'Hammerlock' 
]

leg = [
    'Straight Ankle Lock', 'Kneebar', 'Knee Slicer', 'Figure 4 Toehold', 'Heel Hook', 'Reverse Heel Hook', 'Banana Split Hiplock', 'Calf Slicer' 
]

neck = [
    'Rear Naked Choke', 'Triangle Choke', 'Bow and Arrow Choke', 'Ezekiel Choke', 'Guillotine', 'Cross Collar Choke', 'Short Choke', 'Baseball Choke', 'D\'Arce Choke', 'Head and Arm Choke', 'North-South Choke', 'Crucifix Choke', 'Thrust Choke', 'Anaconda Choke', 'Neck Crank', 'Twister', 'Peruvian Necktie', 'Loop Choke', 'Papercutter Choke', 'Gogoplata', 'Step Over Choke', 'Von Flue Choke', 'Lapel Half Nelson'
]

list_of_submissions = Listbox(tab2, height = 7, width = 25, bg = 'white', activestyle = 'dotbox')
list_of_submissions.grid(column = 3, row = 1, sticky = W)
for c in arm + leg + neck:
    list_of_submissions.insert(END, c)

hard = ['Biceps Slicer', 'Marceloplata', 'Baratoplata', 'Monoplata', 'Hammerlock', 'Knee Slicer', 'Reverse Heel Hook', 'Banana Split Hip Lock', 'Crucifix Choke', 'Anaconda Choke', 'Peruvian Necktie', 'Gogoplata', 'Step Over Choke', 'Von Flue Choke', 'Lapel Half Nelson'
    
]

intermediate = ['Omoplata', 'Wristlock','Inverse Armbar', 'Mir Lock', 'Straight Ankle Lock', 'Kneebar', 'Figure 4 Toehold', 'Heel Hook', 'Calf Slicer', 'Bow and Arrow Choke', 'Ezekiel Choke', 'Guillotine', 'Baseball Choke', 'D\'Arce Choke', 'Head and Arm Choke', 'North-South Choke', 'Thrust Choke', 'Neck Crank', 'Twister', 'Loop Choke', 'Papercutter Choke', 
    
]

beginner = ['Straight Armbar', 'Americana Armbar', 'Kimura Armlock', 'Rear Naked Choke', 'Triangle Choke', 'Cross Collar Choke', 'Short Choke', 
    
]

# Function for generating a random submission to practice; removes random submission from lists after
def practice_submission_body():
    body_part = submission_list.get()
    if body_part == 'All':
        return submission.set(random.choice(arm + leg + neck))
    elif body_part == 'Arm':
        return submission.set(random.choice(arm))
    elif body_part == 'Leg':
        return submission.set(random.choice(leg))
    elif body_part == 'Neck':
        return submission.set(random.choice(neck))
    else:
        return

# Function for generating a random submission based on difficulty
def practice_submission_difficulty():
    difficulty = submission_list.get()
    if difficulty == 'Beginner':
        return submission.set(random.choice(beginner))
    elif difficulty == 'Intermediate':
        return submission.set(random.choice(intermediate))
    elif difficulty == 'Hard':
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
    
def search_youtube():
    def urlify(s):
        s = re.sub(r"\s+", '+', s) 
        return s   
    no_space_submission = urlify(submission.get())
    webbrowser.open('https://www.youtube.com/results?search_query=' + no_space_submission)

root.mainloop()