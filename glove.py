import random

glove_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3]

glove_dict = {
    '1': ['Gloves of Archery', 'Gives a +10 bonus to BS, cumulative with that of magical bow or arrows.', 'AN', '44'],
    '2': ['Gloves of the Cobra', 'On an unarmed impact against skin, injects venom into the victim. See manual.', 'AN',
          '44'],
    '3': ['Gloves of Nimbleness',
          'Give a +10 bonus to Agi, as well as proficiency in Sleight of Hand and Pick Lock, or a +10 if the wearer'
          ' has them.',
          'AN', '44']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

def pick_glove():
    choice = str(random.choice(glove_list))
    chosen_object = glove_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    return final_object
