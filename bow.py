import random



bow_list =[1,1,1,2,2,3,3,4,4,4]


bow_dict ={
'1': ['Bow of Distance' ,'All ranges are doubled for this bow.', 'AN', '44'],
'2': ['Bow of Enchantment' ,'Arrows fired from this bow count as magical.', 'AN', '44'],
'3': ['Bow of Might' ,'It has a Strength Rating of 1d6 + 3 (minimum 5 for an elven bow).', 'AN', '44'],
'4': ['Bow of Seeking' ,"Gives a bonus to the user's BS", 'AN', '44']
}


#this function picks a random object
#from the list, then takes the information from
#the corresponding dictionary
#entry.

#the randomness added on the ifs is for
#sub-classes or specifics
#within a given magic item

def pick_bow():
    choice=str(random.choice(bow_list))
    chosen_object = bow_dict[choice]    
    object_id=choice
    name=chosen_object[0]
    bow_type=random.randint(1,10)
    if bow_type<=3:
        name='Short '+name
    elif bow_type<=6:
        pass
    elif bow_type<=8:
        name='Long '+name
    elif bow_type<=10:
        name='Elf '+name
    if object_id =='3':
        strength=str(random.randint(1,6)+3)
        if int(strength)<5 and (bow_type ==9 or bow_type == 10):
            name+=', 5 Str.'
        else:    
            name+=', '+strength+' Str.'
    elif object_id =='4':
        roll=random.randint(1,10)
        if roll<=4:
            name+=', +5 BS'
        elif roll<=7:
            name+=', +10 BS'
        elif roll<=9:
            name+=', +15 BS'
        elif roll==10:
            name+=', +25 BS'

    description=chosen_object[1]
    source=chosen_object[2]
    page=chosen_object[3]
    final_object = [object_id,name,description, source,page]
    return(final_object)

