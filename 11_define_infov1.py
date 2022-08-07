def define(chosen,chosen_int, option_1, option_2, option_3, int_1, int_2, int_3):
    if chosen == option_1:
        chosen_int == int_1
        return chosen_int

    if chosen == option_2:
        chosen_int == int_2
        return chosen_int
        
    if chosen == option_3:
        chosen_int == int_3
        return chosen_int
    
opp = 4
hyp = 5 
adj = 3

desired_side = "Opposite"

chosen_int = ""

define_side = define(desired_side, chosen_int, "Hypotenuse", "Opposite", "Adjacent", hyp, opp, adj)
print(define_side)
    