import random


robe_list = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]


robe_dict = {
    '1': ['Robe of Disguise', 'The wearer can cast Assume Illusionary Appearance and Cloak Activity once per day. One'
                              ' in six can also cast Clone Image once per day.', 'AN', '45'],
    '2': ['Robe of Ethereality', 'Stores 7 magic points, which can be used to cast Become Ethereal. Needs adaptation'
                                 ' for 2e. See manual.', 'AN', '45'],
    '3': ['Robe of Fire Resistance', "Bestows the same effect as the Resist Fire spell, but each time it's exposed to"
                                     " magical fire, there's a 5% chance of it being destroyed.", 'AN', '45'],
    '4': ['Robe of Mist and Smoke', 'The wearer can cast Cloud of Smoke and Mist Cloud once per day.', 'AN', '45'],
    '5': ['Robe of the Shroud', 'Once per day, the wearer can cast Ghostly Appearance to mimic the assigned undead'
                                ' creatures, and gives immunity to fear by ethereal undead.', 'AN', '45'],
    '6': ['Robe of Toughness', "Gives a bonus to the wearer's TB. This is incompatible with armour or spells that"
                               " increase resistance. See manual.", 'AN', '45']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_robe():
    choice = str(random.choice(robe_list))
    chosen_object = robe_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '1':
        roll = random.randint(1, 6)
        if roll == 6:
            name += ', Greater'
        else:
            name += ', Normal'

    elif object_id == '5':
        roll = random.randint(1, 10)
        if roll <= 5:
            name += ', any Undead form'
        elif roll <= 9:
            name += ', any non-Ethereal Undead'
        elif roll == 10:
            name += ', Ethereal Undead'
    elif object_id == '6':
        roll = random.randint(1, 10)
        if roll <= 5:
            name += ', +1 TB'
        elif roll <= 9:
            name += ', +2 TB'
        elif roll == 10:
            name += ', +3 TB'        
    final_object = [object_id, name, description, source, page]
    return final_object
