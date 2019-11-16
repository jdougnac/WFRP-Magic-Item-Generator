import random



base_list = []


base_dict ={


}


#this function picks a random object
#from the list, then takes the information from
#the corresponding dictionary
#entry.


def pick_base():
    choice=str(random.choice(base_list))
    chosen_object = base_dict[choice]    
    object_id=choice
    name=chosen_object[0]
    description=chosen_object[1]
    source=chosen_object[2]
    page=chosen_object[3]
    final_object = [object_id,name,description, source,page]
    return(final_object)


    if object_id == '':
        roll = random.randint(1,10)
        if roll <=:
            name += ''
        elif roll <=:
            name += ''
        elif roll ==10:
            name += ''

print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
print(pick_base())
