import random

arrow_list = [1, 2, 3, 4, 5, 6, 7, 8]

arrow_dict = {
    '1': ['Arrow of Banefulness', 'Double damage to the creatures of the assigned type.', 'AN', '42'],
    '2': ['Arrow of Bleeding',
          "If it hits, it absorbs 15% of the target's blood, removes 1/4 of its wounds, and falls to the ground. See"
          " manual.",
          'AN', '43'],
    '3': ['Arrow of Division',
          'It spreads into 1d6 projectiles when fired, each of which can target the same target or a random one. One'
          ' hit and damage roll for each projectile.',
          'AN', '43'],
    '4': ['Arrow of Doom',
          'If it hits a creature of the assigned type, it must make a Magic check or die. If it survives, it receives'
          ' double damage.',
          'AN', '43'],
    '5': ['Arrow of Grappling', 'Upon firing, turns into a hook that can hang on to almost any surface. See manual.',
          'AN', '43'],
    '6': ['Arrow of Potency', 'It causes 1 more wound upon impact.', 'CORE1', '184'],
    '7': ['Arrow of Sure Striking', 'Gives a bonus to the BS skill for the attack.', 'AN', '43'],
    '8': ['Arrow of True Flight',
          "It always hits, though it's still necessary to roll in order to determine where it hits.", 'CORE1', '184']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

# the randomness added on the ifs is for
# sub-classes or specifics
# within a given magic item

def pick_arrow():
    choice = str(random.choice(arrow_list))
    chosen_object = arrow_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '1':
        roll = random.randint(1, 100)
        if roll <= 5:
            name = 'Arrow of Banefulness: Goblins and Snotlings'
        elif roll <= 10:
            name = 'Arrow of Banefulness: Hobgoblins'
        elif roll <= 20:
            name = 'Arrow of Banefulness: Orcs and Half-Orcs'
        elif roll <= 25:
            name = 'Arrow of Banefulness: All goblinoids'
        elif roll <= 27:
            name = 'Arrow of Banefulness: Elementals'
        elif roll <= 30:
            name = 'Arrow of Banefulness: Demons'
        elif roll <= 35:
            name = 'Arrow of Banefulness: Undead and Ethereal Creatures'
        elif roll <= 45:
            name = 'Arrow of Banefulness: Creatures of Chaos (including Chaos warriors, etc.'
        elif roll <= 50:
            name = 'Arrow of Banefulness: Dragons, Wyverns, and Jabberwocks'
        elif roll <= 55:
            name = 'Arrow of Banefulness: Elvess'
        elif roll <= 60:
            name = 'Arrow of Banefulness: Dwarves, Gnomes and Halflings'
        elif roll <= 65:
            name = 'Arrow of Banefulness: Fimir'
        elif roll <= 70:
            name = 'Arrow of Banefulness: Monstrous animals (Manticores, Griffins, etc)'
        elif roll <= 75:
            name = 'Arrow of Banefulness: Skaven'
        elif roll <= 80:
            name = 'Arrow of Banefulness: Lizardmen and Troglodytes'
        elif roll <= 85:
            name = 'Arrow of Banefulness: Giants'
        elif roll <= 90:
            name = 'Arrow of Banefulness: Ogres and Trolls'
        elif roll <= 95:
            name = 'Arrow of Banefulness: Werecreatures'
        elif roll <= 100:
            name = 'Arrow of Banefulness: Vampires'

    elif object_id == '4':
        roll = random.randint(1, 100)
        if roll <= 5:
            name = 'Arrow of Doom: Goblins and Snotlings'
        elif roll <= 10:
            name = 'Arrow of Doom: Hobgoblins'
        elif roll <= 20:
            name = 'Arrow of Doom: Orcs and Half-Orcs'
        elif roll <= 25:
            name = 'Arrow of Doom: All goblinoids'
        elif roll <= 27:
            name = 'Arrow of Doom: Elementals'
        elif roll <= 30:
            name = 'Arrow of Doom: Demons'
        elif roll <= 35:
            name = 'Arrow of Doom: Undead and Ethereal Creatures'
        elif roll <= 45:
            name = 'Arrow of Doom: Creatures of Chaos (including Chaos warriors, etc'
        elif roll <= 50:
            name = 'Arrow of Doom: Dragons, Wyverns, and Jabberwocks'
        elif roll <= 55:
            name = 'Arrow of Doom: Elves'
        elif roll <= 60:
            name = 'Arrow of Doom: Dwarves, Gnomes and Halflings'
        elif roll <= 65:
            name = 'Arrow of Doom: Fimir'
        elif roll <= 70:
            name = 'Arrow of Doom: Monstrous animals (Manticores, Griffins, etc)'
        elif roll <= 75:
            name = 'Arrow of Doom: Skaven'
        elif roll <= 80:
            name = 'Arrow of Doom: Lizardmen and Troglodytes'
        elif roll <= 85:
            name = 'Arrow of Doom: Giants'
        elif roll <= 90:
            name = 'Arrow of Doom: Ogres and Trolls'
        elif roll <= 95:
            name = 'Arrow of Doom: Werecreatures'
        elif roll <= 100:
            name = 'Arrow of Doom: Vampires'

    elif object_id == '7':
        roll = random.randint(1, 10)
        if roll <= 4:
            name = 'Arrow of Sure Striking +10'
        elif roll <= 7:
            name = 'Arrow of Sure Striking +20'
        elif roll <= 9:
            name = 'Arrow of Sure Striking +30'
        elif roll == 10:
            name = 'Arrow of Sure Striking +40'
    final_object = [object_id, name, description, source, page]
    return final_object
