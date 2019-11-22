import random


bow_list = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4]


bow_dict = {
    '1': ['Bow of Distance', 'All ranges are doubled for this bow.', 'AN', '44'],
    '2': ['Bow of Enchantment', 'Arrows fired from this bow count as magical.', 'AN', '44'],
    '3': ['Bow of Might', 'It has a Strength Rating of 1d6 + 3 (minimum 5 for an elven bow).', 'AN', '44'],
    '4': ['Bow of Seeking', "Gives a bonus to the user's BS.", 'AN', '44'],
    '5': ['Magic Bow', "Can have special properties. See manual.", 'Apo2', '92']
}
    

# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

# the randomness added on the ifs is for
# sub-classes or specifics
# within a given magic item

def pick_bow():
    bow_choice = random.randint(1, 10)
    if bow_choice <= 4:
        choice = str(random.choice(bow_list))
    else:
        choice = '5'
    chosen_object = bow_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    bow_type = random.randint(1, 10)
    if bow_type <= 3:
        name = 'Short '+name
    elif bow_type <= 6:
        pass
    elif bow_type <= 8:
        name = 'Long '+name
    elif bow_type <= 10:
        name = 'Elf '+name
    if object_id == '3':
        strength = str(random.randint(1, 6)+3)
        if int(strength) < 5 and (bow_type == 9 or bow_type == 10):
            name += ', 5 Str.'
        else:    
            name += ', '+strength+' Str.'
    elif object_id == '4':
        roll = random.randint(1, 10)
        if roll <= 4:
            name += ', +5 BS'
        elif roll <= 7:
            name += ', +10 BS'
        elif roll <= 9:
            name += ', +15 BS'
        elif roll == 10:
            name += ', +25 BS'
    elif object_id == '5':
        bow_properties_roll = random.randint(1, 100)  # TEST
        if bow_properties_roll <= 50:
            bow_properties = 0
        elif bow_properties_roll <= 75:
            bow_properties = 1
        elif bow_properties_roll <= 90:
            bow_properties = 2
        elif bow_properties_roll <= 99:
            bow_properties = 3
        elif bow_properties_roll <= 100:
            bow_properties = 4

        if bow_properties == 0:
            name += ' (no special properties, arrows fired from it count as magical)'
        else:
            bow_enchantments = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8]
            bow_enchantment_list = []
            name += ' ('

            while len(bow_enchantment_list) < bow_properties:
                bow_enchantment = random.choice(bow_enchantments)
                if bow_enchantment not in bow_enchantment_list:
                    bow_enchantment_list.append(bow_enchantment)
                    if bow_enchantment == 1:
                        name += 'Accuracy: '
                        bow_accuracy = random.randint(1, 10)
                        if bow_accuracy <= 4:
                            name += '+5 WS'
                        elif bow_accuracy <= 7:
                            name += '+10 WS'
                        elif bow_accuracy <= 9:
                            name += '+15 WS'
                        elif bow_accuracy <= 10:
                            name += '+20 WS'
                    elif bow_enchantment == 2:
                        name += 'Extra Damage: '
                        bow_damage = random.randint(1, 100)
                        if bow_damage <= 50:
                            name += '+1'
                        elif bow_damage <= 75:
                            name += '+2'
                        elif bow_damage <= 90:
                            name += '+3'
                        elif bow_damage <= 95:
                            name += '+4'
                        elif bow_damage <= 98:
                            name += '*2'
                        elif bow_damage <= 100:
                            name += '*2, +4'
                    elif bow_enchantment == 3:
                        name += 'Flame Attack'
                    elif bow_enchantment == 4:
                        name += 'Extra Range: '
                        bow_range = random.randint(1, 10)
                        if bow_range <= 5:
                            name += '*1 1/2'
                        elif bow_range <= 8:
                            name += '*2'
                        elif bow_range <= 10:
                            name += '*3'
                    elif bow_enchantment == 5:
                        name += 'Mighty Strike'
                    elif bow_enchantment == 6:
                        name += 'Markmanship'
                    elif bow_enchantment == 7:
                        name += 'Protection'
                    elif bow_enchantment == 8:
                        name += 'Self-Firing'
                    else:
                        name += 'ERROR'
                    name += ', '
            name = name[:-2]
            name +=')'
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    return final_object


print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
print(pick_bow())
