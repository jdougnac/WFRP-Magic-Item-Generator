import random
import extras

special_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


special_dict ={
    '1': ['Dagger of Halflings',
          'For a non-halfling, it works as a magical dagger. For a halfling, it counts as a sword, and gives +10 to'
          ' WS.', 'AN', '47'],
    '2': ['Harness of Fearlessness',
          'When fitted to a horse (not any other rideable creature) it becomes immune to Fear, though not Terror.',
          'AN', '47'],
    '3': ['Lantern of Days', 'Its oil burns very slowly: 1 pint will fuel it for 1d4 days.', 'AN', '47'],
    '4': ['Lens of Detection', 'Allows the user to see illusions for what they truly are. See manual.', 'AN', '47'],
    '5': ['Lyre of Melody', 'It gives +20 to music and busk tests.', 'AN', '47'],
    '6': ['Purse of Teeth',
          'If someone other than the owner tries to take money from it, they take damage. See manual.', 'AN', '47'],
    '7': ['Ring of Comprehension',
          'Allows the wearer to read and write their own language. 50% of them also give knowledge on how to read and'
          ' write 1d3 additional languages.',
          'AN', '47'],
    '8': ['Sand of Flinging',
          'When thrown at a location, all creatures within a four yard radius are blinded, making missile fire and'
          ' spellcasting impossible.', 'AN', '47'],
    '9': ['All-Seeing Mirror',
          'These come in pairs, each seeing the reflection on the other through unlimited distances by land, or up to'
          ' 500 miles of sea.', 'CORE1', '183'],
    '10': ['Enchanted Rope', 'A magical rope that obeys the commands of its owner. See manual.', 'CORE1', '185']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_special():
    choice = str(random.choice(special_list))
    chosen_object = special_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '7':
        roll = random.randint(1, 2)
        if roll == 1:
            name += ': '
            extra_languages = random.randint(1, 3)
            language_list = random.sample(extras.languages, k=extra_languages)
            for item in language_list:
                name += item + ', '
            name = name[:-2]
        elif roll == 2:
            name += ': no extra languages'
                    
    elif object_id == '8':
        roll = str(random.randint(1, 4))
        if roll == '1':
            name += ': '+roll+' use'
        else:
            name += ': '+roll+' uses'

    elif object_id == '10':
        name += ' ('
        roll = str(random.randint(1, 6)+2)
        owner = random.randint(1, 2)
        name += roll + ' feet, '
        if owner == 1:
            name += 'no current owner)'
        elif owner == 2:
            name += 'its owner still lives)'

    final_object = [object_id, name, description, source, page]
    return final_object


print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())
print(pick_special())