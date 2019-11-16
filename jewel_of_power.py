import random
import spell

jewel_dict = {
    '1': ['Spell Jewel', 'A spellcaster can cast the spell contained once a day, without rolling.', 'CORE1', '185'],
    '2': ['Multiple Spell Jewel', 'A spellcaster can cast each spell contained within once a day, without rolling.',
          'CORE1', '185'],
    '3': ['Energy Jewel', 'PENDING', 'CORE1', '185']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_jewel():
    jewel_roll = random.randint(1, 100)
    if jewel_roll <= 50:
        object_id = '1'
    elif jewel_roll <= 60:
        object_id = '2'
    elif jewel_roll <= 100:
        object_id = '3'
    chosen_object = jewel_dict[object_id]
    name = chosen_object[0]
    if object_id == '1':
        name += ' (' + spell.pick_spell() + ')'
    elif object_id == '2':
        number_of_spells = random.randint(1, 3)+1
        for power in range(0, number_of_spells):
            name += ' (' + spell.pick_spell() + '),'
        name = name[:-1]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    print(final_object)
    return final_object

pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()
pick_jewel()

