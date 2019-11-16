import random



horn_list = [1,2,2,3,3,3,4,4,4,5]


horn_dict ={
'1': ['Horn of Banishment' ,'When blown, undead within 8 yards must check for instability with a -2 penalty, whether or not they are normally affected by it. Also, all control is broken and must be reestablished. Finally, demons must also check for instability with a -2', 'AN', '44'],
'2': ['Horn of Hounds' ,"When blown, 1d4+1 War Dogs appear the next round, following the bearer's instructions for one turn before disappearing.", 'AN', '45'],
'3': ['Horn of Plenty' ,'This horn gives bad-looking but delicious and nutritious food, as well as water. Enough for eight man-sized creatures to be fed for 24 hours.', 'AN', '45'],
'4': ['Horn of Valor' ,'When blown, all allies within 8 yards of the bearer get a +1 SR and +5 WS bonus for one hour.', 'AN', '45'],
'5': ['Unicorn Horn' ,'Has various effects. See manual.', 'AN', '45']
}


#this function picks a random object
#from the list, then takes the information from
#the corresponding dictionary
#entry.


def pick_horn():
    choice=str(random.choice(horn_list))
    chosen_object = horn_dict[choice]    
    object_id=choice
    name=chosen_object[0]
    description=chosen_object[1]
    source=chosen_object[2]
    page=chosen_object[3]
    final_object = [object_id,name,description, source,page]
    return(final_object)

