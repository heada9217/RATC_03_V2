#import statements
import math
import pandas

#functions go here

def yes_no(question):

    yes_no_answers = ["yes", "no","y","n"]

    valid = False 
    while not valid:

        response = input(question).lower().strip()

        for var_item in yes_no_answers:
            if response == var_item:
                return response
            elif response == var_item:
                return var_item
        
        print("Please enter either yes or no...\n")

def numb_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)
    
    valid = False 
    while not valid:

        try:
            response = float(input(question)) 
            
            if low_num < response < high_num:
                return response
            
            else:
                print (error)
        
        except ValueError:
            print(error)

def string_check(choice, options, error):

        for var_list in options:

            #if side/angle is one in the list return the full
            if choice in var_list:

                #Get full name of side/angle 
                chosen = var_list[0].title()
                is_valid = "yes"
                break

            #if choice is not valid, set is_valid to no 
            else:
                is_valid = "no"
            
        #if the side/angle is not valid ask question again 
        if is_valid == "yes":
            return chosen
        else:
            print(error)
            return "Invalid choice"
            
def get_sides():

    sides = []

    used_sides = []


    side_options = [["opposite", "oppo", "opp", "o"], 
    ["adjacent", "adj", "a"], 
    ["hypotenuse", "hyp", "h"],
    ]

    side_error = "Please enter a valid side (o,a,h)"

    desired_side = ""
    while desired_side != "xxx":



        sides_row = []

        #Ask user for a side
        desired_side = input("What side do you have?").lower().strip()

        if desired_side == "xxx":
            return sides
        
        #check if desired side is valid

        valid_side = string_check(desired_side,side_options,side_error)


        #checks if valid side has been used before
        if valid_side in used_sides:
            print("You cannot have 2 of the same side.")
            valid_side = "Invalid choice"
        
        
        #ask user for length size if choice is valid
        if valid_side != "Invalid choice":

            side_length = numb_check("How big?: ", 0, 100)
            
            #add amount to side row and side length to side row and used_sides
            sides_row.append(side_length)
            sides_row.append(valid_side)

            used_sides.append(valid_side)
        
        #check that side is not the exit code before adding
        if valid_side != "xxx" and valid_side != "Invalid choice":
            sides.append(sides_row)
        
        #if user has already given 2 sides, continue
        if len(sides) == 2:
            return sides

def pythag(hyp,opp,adj):
    

    calculated_side = []

    if hyp == []:
        calculated_side.append("Hypotenuse")
        hyp = math.sqrt(adj ** 2 + opp ** 2)
        calculated_side.append(hyp)
        

    if opp == []:
        calculated_side.append("Opposite")
        opp = math.sqrt(hyp ** 2 - adj **2)
        calculated_side.append(opp)
        

    if adj == []:
        calculated_side.append("Adjacent")
        adj = math.sqrt(hyp ** 2 - opp ** 2)
        calculated_side.append(adj)
        
    return calculated_side

def sides_trig(hyp,opp,adj,angle):

    hyp_row = ["Hypotenuse"]
    opp_row = ["Opposite"]
    adj_row = ["Adjacent"]

    calculated_sides = []



    if hyp != []:
        opp = math.sin(angle * (math.pi / 180)) * hyp
        opp_row.append(opp)
        adj = math.cos(angle * (math.pi/180)) * hyp
        adj_row.append(adj)
        
        calculated_sides.append(opp_row)
        calculated_sides.append(adj_row)
        
        return calculated_sides

    if opp != []:
        adj = opp / math.tan(angle * (math.pi / 180))
        adj_row.append(adj)
        hyp = opp / math.sin(angle * (math.pi / 180))
        hyp_row.append(hyp)

        calculated_sides.append(adj_row)
        calculated_sides.append(hyp_row)

        return calculated_sides

    if adj != []:
        opp = adj / (math.tan(angle * (math.pi / 180)))
        opp_row.append(opp)
        hyp = adj / (math.sin(angle * (math.pi / 180)))
        hyp_row.append(hyp)

        calculated_sides.append(opp_row)
        calculated_sides.append(hyp_row)

        return calculated_sides

def angles(hyp, opp):
    calculated_angles = []
    #calculate first angle using trig
    angle_1 = math.asin(opp / hyp)
    angle_1 = angle_1 * (180 / math.pi)

    #second angle is found 
    angle_2 = 90 - angle_1
    #third angle is always 90
    angle_3 = 90
    
    #add angles to list
    calculated_angles.append(angle_1)
    calculated_angles.append(angle_2)
    calculated_angles.append(angle_3)

    return calculated_angles

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return ((math.floor(n*multiplier + 0.5)) / multiplier)


#Main routine

# set up dictionary / lists to hold data

opp = []
adj = []
hyp = []
angle = []

#lists to store lengths data

sides_data_dict = {
    "Hypotenuse": hyp,
    "Opposite": opp,
    "Adjacent": adj
}

sides_length_headings = ['Hypotenuse:', 'Opposite:', 'Adjacent:']

sides_length_data = []

#lengths dictionary
sides_lengths_dict = {
    'Side': sides_length_headings,
    'Length': sides_length_data
}

angle_1 = []
angle_2 = []
angle_3 = []


angles_data_dict = {
    "Opposite angle:": angle_1,
    "Adjacent angle:": angle_2,
    "Hypotenuse angle:": angle_3    
}

angle_headings = ["Opposite angle:", "Adjacent angle:", "Hypotenuse angle:"]

angle_data = []

angle_dict = {
    "Angle": angle_headings,
    "Degrees": angle_data
    
}

sides_info = get_sides()

#if user only has 1 side, ask for angle aswell
if len(sides_info) == 1:
        angle = numb_check("Angle?: ", 0, 90)

print("***Current Information***")

for item in sides_info:
    print(item)

if angle != []:
    print("Angle: {} degrees".format(angle))

print()

# side info is a list including the sides and lengths given.
side_1 = sides_info[0]
length_1 = side_1[0]
type_1 = side_1[1]


# if sides given is equal to a length, define the side with length amount
if type_1 == "Opposite":
    opp = length_1

elif type_1 == "Adjacent":
    adj = length_1

elif type_1 == "Hypotenuse":
    hyp = length_1



# if 2 sides are given, identify second side
if len(sides_info) == 2:
    side_2 = sides_info[1]
    length_2 = side_2[0]
    type_2 = side_2[1]

    if type_2 == "Opposite":
        opp = length_2

    elif type_2 == "Adjacent":
        adj = length_2

    elif type_2 == "Hypotenuse":
        hyp = length_2

    # if user has 2 sides, use pythag to find last side
    if angle == []:
        pythag_side = pythag(hyp, opp, adj)
        # identify the last side to use to find angle


        if pythag_side[0] == "Hypotenuse":
            hyp = pythag_side[1]
        if pythag_side[0] == "Opposite":
            opp = pythag_side[1]   
        if pythag_side[0] == "Adjacent":
            adj = pythag_side[1]
        
        sides_list = (hyp, opp, adj)
        

    
        
        
# if user has 1 side and 1 angle, calculate and identify lengths
else: 
    trig_side = sides_trig(hyp,opp,adj,angle)
    

    side_trig_1 = trig_side[0]
    trig_length_1 = side_trig_1[1]
    type_length_1 = side_trig_1[0]

    if type_length_1 == "Opposite":
        opp = trig_length_1
    if type_length_1 == "Adjacent":
        adj = trig_length_1
    if type_length_1 == "Hypotenuse":
        hyp = trig_length_1

    side_trig_2 = trig_side[1]
    trig_length_2 = side_trig_2[1]
    type_length_2 = side_trig_2[0]
    
    if type_length_2 == "Opposite":
        opp = trig_length_2
    if type_length_2 == "Adjacent":
        adj = trig_length_2
    if type_length_2 == "Hypotenuse":
        hyp = trig_length_2
        
    sides_list = (hyp, opp, adj)
    
    
    
    
#ask user for wanted decimal places and
round_decimal = int(numb_check("What decimal place would you like to round to?", 0, 5))

print (sides_list)
for item in sides_list:
    sides_length_data.append(item)

    
#calculate angles using hyp and opp 
calculate_angles = angles(hyp,opp)
hyp_angle = calculate_angles[0]
opp_angle = calculate_angles[1]
adj_angle = calculate_angles[2]



#create sides frame
calculated_sides_info_frame = pandas.DataFrame(sides_lengths_dict)
calculated_sides_info_frame = calculated_sides_info_frame.set_index("Side")
    
pandas.set_option('display.max_columns', None)

#print sides frame
print("*** Full sides information ***")
print(calculated_sides_info_frame)

print()

for item in calculate_angles:
    angle_data.append(item)
    
calculated_angle_info_frame = pandas.DataFrame(angle_dict)
calculated_sides_info_frame = calculated_angle_info_frame.set_index("Angle")

pandas.set_option('display.max_columns', None)

#print angles frame
print("*** Full angles information ***")
print(calculated_angle_info_frame)