import math

from numpy import round_



def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return ((math.floor(n*multiplier + 0.5)) / multiplier)

#v2; trying to make the function work for several numbers in a list

for item in range(0,4):
    
    angles = []

    angle_1 = float(input("Angle: "))
    
    angle_2 = float(input("Angle 2: "))
    
    angle_3 = float(input("Angle 3: "))
    
    angles = (angle_1, angle_3, angle_3)
    
    decimal = int(input("How many decimal places do you want?: "))
    
    rounded_value = [round_half_up(item, decimal) for item in angles]
   
        
    for item in rounded_value:
        print(item)

    print()
