
#round using item and wanted decimal places
def round_custom(var_amount, var_round_to):
    return round(var_amount, var_round_to)


list_to_round = [53.1317,36.8734,90.00002]
rounded_list = []

for item in list_to_round:
    rounded_item = round_custom(item,2)
    rounded_list.append(rounded_item)
    
print(rounded_list)