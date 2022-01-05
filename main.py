import random

# Lists of submssions based on body part and difficulty
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

# Defining variables for randomizing submission suggestion
random_all_body = random.choice(arm + leg + neck)
random_arm_body = random.choice(arm)
random_leg_body = random.choice(leg)
random_neck_body = random.choice(neck)

random_all_difficulty = random.choice(beginner + intermediate + hard)
random_beginner_difficulty = random.choice(beginner)
random_intermediate_difficulty = random.choice(intermediate)
random_hard_difficulty = random.choice(hard)

# Function for generating a random submission to practice; removes random submission from lists after
def practice_submission_body():
    body_part = input('Choose from all, or more specifically, arm, leg, or neck submissions: ')
    if body_part == 'all' and random_all_body in arm or leg or neck:
        return random_all_body
    elif body_part == 'arm':
        return random_arm_body
    elif body_part == 'leg':
        return random_leg_body
    elif body_part == 'neck':
        return random_neck_body
    else:
        return 'Please choose a valid submission category: all, arm, leg, or neck.'

# Function for generating a random submission based on difficulty
def practice_submission_difficulty():
    difficulty = input('Choose from all, or more specifically, beginner, intermediate, or hard submissions: ')
    if difficulty == 'all' and random_all_difficulty in beginner or intermediate or hard:
        return random_all_difficulty
    elif difficulty == 'beginner':
        return random_beginner_difficulty
    elif difficulty == 'intermediate':
        return random_intermediate_difficulty 
    elif difficulty == 'hard':
        return random_hard_difficulty
    else:
        return 'Please choose a valid submission category: all, beginner, intermediate, or hard.'
    
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
    
print(practice_submission_difficulty())