import random

potion_list = ['1', '2', '3', '4', '5', '6', '7', '8']

potion_dict = {
    '1': ['Potion of Disguise',
          'The user will seem to turn into the first object they concentrate on, as in the level 1 spell Assume'
          ' Illusionary Appearance, for 1d6*10 turns.',
          'CORE1', '186'],
    '2': ['Potion of Flight',
          'The user is able to fly, as per the level 1 spell Flight for 1d6*10 turns, though a check is needed to'
          ' control their movement. See manual.',
          'CORE1', '186'],
    '3': ['Potion of Healing', 'Restores 2d6 wounds and heals all poisons. See manual.', 'CORE1', '186'],
    '4': ['Potion of Invisibility',
          'Turns the user invisible for 1d6*10 turns: -40 to all attacks if they stay motionless, -20 otherwise.'
          ' Casting spells or using magic items ends the effect.',
          'CORE1', '186'],
    '5': ['Potion of Strength', 'Increases Strength by 20 for 1d6*10 rounds.', 'CORE1', '186'],
    '6': ['Potion of Tongues',
          'Allows the user to understand and speak any language or other form of sound communication for 1d6*10 turns.',
          'CORE1', '186'],
    '7': ['Potion of Water Walking', 'The user may walk on water as if it was a solid surface for 1d6*10 turns.',
          'CORE1', '186'],
    '8': ['Cursed Potion: ', 'Gives a damaging effect. See the word document.', 'CORE1', '187']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_potion():
    choice = str(random.choice(potion_list))
    chosen_object = potion_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '8':
        roll = random.randint(1, 55)
        if roll <= 30:
            minus_roll = random.randint(1, 100)
            if minus_roll <= 10:
                name += ' -10 WS'
            elif minus_roll <= 20:
                name += ' -10 BS'
            elif minus_roll <= 30:
                name += ' -10 Str'
            elif minus_roll <= 40:
                name += ' -10 T'
            elif minus_roll <= 50:
                name += ' -10 WP'
            elif minus_roll <= 60:
                name += ' -1 Mag'
            elif minus_roll <= 70:
                name += ' -10 Agi'
            elif minus_roll <= 75:
                name += ' -' + str(random.randint(1, 3) * 10) + ' WS'
            elif minus_roll <= 80:
                name += ' -' + str(random.randint(1, 3) * 10) + ' BS'
            elif minus_roll <= 85:
                name += ' -' + str(random.randint(1, 3) * 10) + ' S'
            elif minus_roll <= 90:
                name += ' -' + str(random.randint(1, 3) * 10) + ' T'
            elif minus_roll <= 95:
                name += ' -' + str(random.randint(1, 3)) + ' Mag'
            elif minus_roll <= 100:
                name += ' -' + str(random.randint(1, 3) - 10) + ' Agi'
        elif roll <= 35:
            name += 'Backfire'
        elif roll <= 40:
            shining_skin_roll = random.randint(1, 40)
            if shining_skin_roll <= 10:
                name += ' Shining Skin, Red'
            elif shining_skin_roll <= 20:
                name += ' Shining Skin, Blue'
            elif shining_skin_roll <= 30:
                name += ' Shining Skin, Yellow'
            elif shining_skin_roll <= 40:
                name += ' Shining Skin, Green'
        elif roll <= 45:
            name += ' Stuck Tongue'
        elif roll <= 50:
            name += ' Baleful Illusion, '
            illusion_roll = random.randint(1, 100)
            if illusion_roll <= 5:
                name += 'Goblin'
            elif illusion_roll <= 10:
                name += 'Hobgoblin'
            elif illusion_roll <= 20:
                name += 'Orc'
            elif illusion_roll <= 25:
                name += 'Human'
            elif illusion_roll <= 27:
                name += 'Bloodletter'
            elif illusion_roll <= 30:
                name += 'Horse'
            elif illusion_roll <= 35:
                name += 'Zombie'
            elif illusion_roll <= 45:
                name += 'Chaos Warrior'
            elif illusion_roll <= 50:
                name += 'Dragon'
            elif illusion_roll <= 55:
                name += 'Troll'
            elif illusion_roll <= 60:
                name += 'Dwarf'
            elif illusion_roll <= 65:
                name += 'Elf'
            elif illusion_roll <= 70:
                name += 'Pink Horror'
            elif illusion_roll <= 75:
                name += 'Lizardman'
            elif illusion_roll <= 80:
                name += 'Skaven'
            elif illusion_roll <= 85:
                name += 'Giant'
            elif illusion_roll <= 90:
                name += 'Ogre'
            elif illusion_roll <= 95:
                name += 'Werewolf'
            elif illusion_roll <= 100:
                name += 'Vampire'
        elif roll <= 55:
            name += ' Mutation'

    final_object = [object_id, name, description, source, page]
    return final_object
