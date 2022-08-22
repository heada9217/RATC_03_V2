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

def each_info(opp_s,hyp_s,adj_s,opp_a,hyp_a,adj_a):
    
    side_or_angle_options = ["side", "s", "sides"], ["angle", "a", "angles"]
    
    side_or_angle_error = "Please enter either side or angle."
    
    side_angles_options = [["opposite", "oppo", "opp", "o"], 
    ["adjacent", "adj", "a"], 
    ["hypotenuse", "hyp", "h"],
    ]
    
    side_angle_error = "Please enter a valid side (o,a,h)"
    
    want_info = ""
    while want_info != "xxx":
        
        
        #ask user whether they want angle or side 
        side_angle = input("Side or angle?: ").lower()
        
        
        if side_angle == "xxx":
            break
        
        side_angle_check = string_check(side_angle, side_or_angle_options, side_or_angle_error)
        

        
        #if side, ask which side
        if side_angle_check == "Side" and side_angle_check != "Invalid_choice":
            
            side_check = "Invalid choice"
            while side_check == 'Invalid choice':    
                
                #ask user which side     
                which_side = input("Which side?: ").lower()
                side_check = string_check(which_side, side_angles_options, side_angle_error)
                print()
            

                if side_check == "Hypotenuse":
                    print("Hypotenuse side: {}".format(hyp_s))
                if side_check == "Opposite":
                    print("Opposite side: {}".format(opp_s))
                if side_check == "Adjacent":
                    print("Adjacent side: {}".format(adj_s))
                print()
        
        #if angle, ask which angle        
        elif side_angle_check == "Angle" and side_angle_check != "Invalid_choice":

            angle_check = "Invalid choice"
            while angle_check == "Invalid choice":
                
                
                #ask user which angle they want
                which_angle = input("Which angle?: ").lower()
                angle_check = string_check(which_angle, side_angles_options, side_angle_error)
                print()
            
           
                if angle_check == "Hypotenuse":
                    print("Hypotenuse angle: {}".format(hyp_a))
                if angle_check == "Opposite":
                    print("Opposite angle: {}".format(opp_a))
                if angle_check == "Adjacent":
                    print("Adjacent angle: {}".format(adj_a))
                    
                print()
            
            
                    
                
hyp_s = 5
opp_s = 4
adj_s = 3

hyp_a = 90
opp_a = 53.13
adj_a = 36.87
        
seperate_info = each_info(opp_s,hyp_s,adj_s,opp_a,hyp_a,adj_a)