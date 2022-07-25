import math
from this import d
from xmlrpc.server import SimpleXMLRPCDispatcher
import pandas


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

def int_check(question, low_num, high_num):

    error = "Please enter a whole number between {} and {}".format(low_num, high_num)
    
    valid = False 
    while not valid:

        try:
            response = int(input(question)) 
            
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

        
        
        #ask user for length size if choice is valid
        if valid_side != "Invalid choice":

            side_length = int_check("How big?: ", 0, 100)
            
            sides_row.append(side_length)
            sides_row.append(valid_side)
        
        #check that side is not the exit code before adding
        if valid_side != "xxx" and valid_side != "Invalid choice":
            sides.append(sides_row)
   
        if len(sides) == 2:
            return sides


          
    
        
#Main routine    

sides_info = get_sides()
angle = ""

#if user only has 1 side, ask for angle aswell
if len(sides_info) == 1:
        angle = int_check("Angle?: ", 0, 90)

for item in sides_info:
    print(item)

if angle != "":
    print("Angle: {}".format(angle))


    



    
    

    
        

    


        

    

    
    

    






