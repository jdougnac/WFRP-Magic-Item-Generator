import random

wand_list = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7]


wand_dict = {
    '1': ['Blackwand', 'PENDING', 'AN', '46'],
    '2': ['Wand of Absorption', 'PENDING', 'AN', '46'],
    '3': ['Wand of Corrosion', 'PENDING', 'AN', '46'],
    '4': ['Wand of Fear', 'PENDING', 'AN', '46'],
    '5': ['Wand of Jade',
          'When casting a spell with a range other than Touch or Personal, the user may make a WP check to increase its range by 2d6 yards.',
          'CORE1', '188'],
    '6': ['Wand of Jet', 'PENDING', 'CORE1', '188'],
    '7': ['Wand of Onyx', 'PENDING', 'CORE1', '188']

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
    final_object = [object_id, name, description, source, page]
    return final_object

