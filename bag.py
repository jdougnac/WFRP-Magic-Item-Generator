import random


bag_list = [1, 1, 1, 1, 1, 1, 2, 2, 3, 3]


bag_dict = {
    '1': ['Bag of Lightness', 'Objects placed in the bag weigh 1/10 their normal weight. Can carry up to 2D6*100'
                              ' encumbrance points. See manual.', 'AN', '43'],
    '2': ['Bag of Middenheim', 'Like a Bag of Lightness, but it can carry (2D6+3)*100 encumbrance points, and is'
                               ' resistant'
                               ' to fire and water. See manual.', 'AN', '43'],
    '3': ['Bag of Resource', 'Once per day, the bearer can retrieve the necessary materials for a single spell.', 'AN',
          '43']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

# the randomness added on the ifs is for
# sub-classes or specifics
# within a given magic item

def pick_bag():
    choice = str(random.choice(bag_list))
    chosen_object = bag_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '1':
        roll = (random.randint(1, 6)+random.randint(1, 6))
        name += ': '+str((roll+6)*100)+' encumbrance'        
    elif object_id == '2':
        roll = (random.randint(1, 6)+random.randint(1, 6))
        name += ': '+str((roll+3)*100)+' encumbrance'
    final_object = [object_id, name, description, source, page]
    return final_object
