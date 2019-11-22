import random


boot_list = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]


boot_dict = {
    '1': ['Boots of Bovva', 'Allows the bearer to make a single STR 6 kick attack instead of any other attacks.',
          'CORE1', '184'],
    '2': ['Boots of Command', 'If someone other than their owner dons them, the owner can give them commands. See'
                              ' manual.', 'CORE1', '185'],
    '3': ['Boots of Concealment', 'Has hidden pockets, which can conceal objects of up to 2-foot cube in volume, or a'
                                  ' single large object like a greatsword, up to 250 Enc.', 'CORE1', '184'],
    '4': ['Boots of Leaping', 'Adds an extra 1d6 yards to any leap the wearer makes.', 'CORE1', '184'],
    '5': ['Boots of Silence', 'While moving at walking speed, the wearer only is heard if they roll 95+, and then only'
                              ' up to 8 yards. The chance is 50% if they move faster.', 'AN', '44'],
    '6': ['Boots of Speed', 'They allow the bearer to move at double their speed.', 'CORE1', '184'],
    '7': ['Boots of Tracelessness', "The wearer leaves no footprints of any kind (even on mud or sand) and can't be"
                                    " tracked normally, though other senses, such as smell, work as usual.", 'AN', '44']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

# the randomness added on the ifs is for
# sub-classes or specifics
# within a given magic item

def pick_boot():
    choice = str(random.choice(boot_list))
    chosen_object = boot_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    return final_object
