import random

wand_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7]

wand_dict = {
    '1': ['Blackwand', 'Once per day, the bearer can cast shadowcloak (ROS 2 p. 164), affecting allies up to'
                       '4 yards away. Plus, once per day can discharge 1d6 projectiles coated in Manbane. See'
                       'manual. ', 'AN', '46'],
    '2': ['Wand of Absorption', 'Can absorb spell points cast at the user with a channeling test, and then use those'
                                ' to cast spells. If the caster goes beyond the amount the wand can hold, it explodes. '
                                'See manual. ', 'AN', '46'],
    '3': ['Wand of Corrosion', 'At dawn each day, roll 1d6. That is the amount of times the wand can be '
                               'used. It affects all items held by one person with the spell Curse of Rust ('
                               'ROS 2, p. 159).', 'AN', '46'],
    '4': ['Wand of Fear', 'PENDING', 'AN', '46'],
    '5': ['Wand of Jade',
          'When casting a spell with a range other than Touch or Personal, the user may make a WP check to increase its'
          ' range by 2d6 yards.',
          'CORE1', '188'],
    '6': ['Wand of Jet', 'When casting a spell, the user may make a WP test. If successful, its TN is reduced'
                         'by 1d4.', 'CORE1', '188'],
    '7': ['Wand of Onyx', 'Works as a Jewel of Energy. Once per day, can add the amount in parentheses to a'
                          ' spellcasting roll, even after rolling the dice.', 'CORE1', '188'],
    '8': ['Rod of Power',
          'The bearer can store a spell in it by casting it. It can later be cast without needing a roll.'
          ' The spells cannot be accessed by a different spellcaster. Stores up to three spells', 'ROS1', '160'],
    '9': ['Staff of Damnation', 'Empowers Undead. See manual.', 'ROS1', '160']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_wand():
    choice = str(random.choice(wand_list))
    chosen_object = wand_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '2':
        wand_capacity = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + \
                        random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        current_usage = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        if current_usage > wand_capacity:
            current_usage = wand_capacity
        name += ' (capacity ' + str(wand_capacity) + ' points, ' + str(current_usage) + ' points are already in use)'
    elif object_id == '7':
        bonus = str(random.randint(1, 6))
        name += ' (' + bonus + ')'
    final_object = [object_id, name, description, source, page]
    return final_object
