import random


amulet_list = [1, 1, 2, 3, 3, 4, 5, 6, 7, 8]

amulet_dict = {
    '1': ['Amulet of Thrice-Blessed Copper', 'One less wounds from impacts with a non-magical weapon, +20 poison'
                                             ' resistance, detects poison at 5 cm.', 'CORE1', '183'],
    '2': ['Amulet of Adamantine', "Increases the user's Toughness to 70. See manual.", 'CORE1', '184'],
    '3': ['Amulet of Enchanted Jade', "Bearer regenerates like a troll, except they can't regenerate lost limbs or"
                                      " deadly criticals.", 'CORE1', '184'],
    '4': ['Amulet of Coal', 'Can contain up to 3 fireball spells. It recharges by casting Fireball at it.', 'CORE1',
          '184'],
    '5': ['Amulet of Iron', 'This needs GM input to be adapted to 2nd edition. See manual.', 'CORE1', '184'],
    '6': ['Amulet of Righteous Silver', 'Gives immunity to psychological effects caused by undead.', 'CORE1', '184'],
    '7': ['Amulet of Law', 'Gives bonuses to resist Chaotic Magic and pyschological effects from creatures of Chaos.'
                           ' See manual.', 'AN', '42'],
    '8': ['Amulet of Watchfulness', 'If a creature wants to harm the bearer while they sleep, they wake up. See'
                                    ' manual.', 'AN', '42']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

# The boolean parameters
# are there so the user can decide whether to
# include them or not

# the randomness added on the ifs is for
# sub-classes or specifics
# within a given magic item

def pick_amulet(is_rune=False):
    choice = str(random.choice(amulet_list))
    chosen_object = amulet_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '5':
        roll = random.randint(1, 10)
        if roll <= 6:
            name = 'Amulet of Iron +10'
        elif roll <= 9:
            name = 'Amulet of Iron +20'
        elif roll == 10:
            name = 'Amulet of Iron +30'
    final_object = [object_id, name, description, source, page]
    return final_object
