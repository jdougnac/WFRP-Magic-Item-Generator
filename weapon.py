import random


weapon_enchantment_dict = {
    '1': 'Additional Damage',
    '2': 'Characteristic Gain',
    '3': 'Characteristic Drain',
    '4': 'Bane Weapon',
    '5': 'Flame Attack',
    '6': 'Poison Attack',
    '7': 'Degeneration Attack',
    '8': 'Freeze Attack',
    '9': 'Warp Attack',
    '10': 'Sleep',
    '11': 'Flight',
    '12': 'Breather Underwater',
    '13': 'Confusion',
    '14': 'Fear ',
    '15': 'Instability',
    '16': 'Protection',
    '17': 'Resist Fire',
    '18': 'Animated',
    '19': 'Invisibility',
    '20': 'Magic Damper',
    '21': 'Berserk',
    '22': 'Repel Undead',
    '23': 'Repel Demons',
    '24': 'Destroy Magical Weapon',
    '25': 'Spell Absorption',
    '26': 'Mighty Strike'
}

melee_weapon_enchantment_list = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                 '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2',
                                 '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4',
                                 '4', '4', '4', '4', '4', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
                                 '14', '15', '15', '16', '16', '17', '18', '19', '20', '21', '21', '22', '22', '23',
                                 '23', '24', '25', '25', '26', '26']

range_weapon_enchantment_list = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                                 '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2',
                                 '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '4',
                                 '4', '4', '4', '4', '4', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '15',
                                 '15', '16', '16', '17', '19', '20', '22', '22', '23', '23', '25', '25', '26', '26']

melee_weapon_list = ['1', '2', '2', '2', '3', '4', '5', '6', '7', '7', '8', '8', '9', '10', '11', '12', '13', '14',
                     '15', '15', '15', '16', '17', '18', '18', '18', '18', '18', '19', '19', '19', '19', '19']

range_weapon_list = ['1', '2', '2', '3', '4', '5', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                     '17']

melee_weapon_dict = {
    '1': ['Buckler', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '2': ['Dagger', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '3': ['Cavalry Spear', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '4': ['Flail', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '5': ['Foil', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '6': ['Knuckle-duster ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '7': ['Great Sword', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '8': ['Great Axe', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '9': ['Halberd', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '10': ['Lance', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '11': ['Main Gauche ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '12': ['Morning Star ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '13': ['Quarterstaff', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '14': ['Rapier ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '15': ['Shield ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '16': ['Spear ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '17': ['Sword-breaker ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '18': ['Hand Axe', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '19': ['Long Sword', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188']
}

range_weapon_dict = {
    '1': ['Blunderbuss', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '2': ['Pistol', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '3': ['Repeater Pistol', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '4': ['Bola', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '5': ['Crossbow', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '6': ['Crossbow Pistol ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '7': ['Javelin ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '8': ['Lasso', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '9': ['Net', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '10': ['Repeater Crossbow', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '11': ['Sling ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '12': ['Staff Sling', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '13': ['Throwing Axe', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '14': ['Throwing Hammer ', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '15': ['Throwing Dagger', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '16': ['Throwing Star', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188'],
    '17': ['Whip', 'Enchanted weapon. See manual for a description of its properties.', 'CORE1', '188']
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_weapon(is_rune = False, is_chaos = False):
    amount_properties_roll = random.randint(1, 100)  # TEST

    if amount_properties_roll <= 20:
        amount_properties = 0
    elif amount_properties_roll <= 70:
        amount_properties = 1
    elif amount_properties_roll <= 90:
        amount_properties = 2
    elif amount_properties_roll <= 95:
        amount_properties = 3
    elif amount_properties_roll <= 99:
        amount_properties = 4
    elif amount_properties_roll == 100:
        amount_properties = 5
    weapon_type_roll = random.randint(1, 100)
    if weapon_type_roll <= 70:
        choice = str(random.choice(melee_weapon_list))
        chosen_object = melee_weapon_dict[choice]
        enchantment_list = melee_weapon_enchantment_list
    elif weapon_type_roll <= 100:
        choice = str(random.choice(range_weapon_list))
        chosen_object = range_weapon_dict[choice]
        enchantment_list = range_weapon_enchantment_list
    object_id = choice
    name = chosen_object[0]

    if amount_properties == 0:
        name += ' (Magical, '
    elif amount_properties != 0:
        name += ' ('
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]

    object_enchantments = []
    while len(object_enchantments) < amount_properties:
        pick = random.choice(enchantment_list)
        if pick not in object_enchantments:
            object_enchantments.append(pick)
    for enchantment in object_enchantments:
        if enchantment == '1':
            damage_roll = random.randint(1, 100)
            name += 'Additional Damage ('
            if damage_roll <= 50:
                name += '+1), '
            elif damage_roll <= 75:
                name += '+2), '
            elif damage_roll <= 90:
                name += '+3), '
            elif damage_roll <= 95:
                name += '+4), '
            elif damage_roll <= 98:
                name += 'double normal damage), '
            elif damage_roll <= 100:
                name += 'double normal damage, +4), '
        elif enchantment == '2':
            char_gain_roll = random.randint(1, 89)
            name += 'Characteristic Gain ('
            if char_gain_roll <= 9:
                name += 'WS +10), '
            elif char_gain_roll <= 18:
                name += 'S +10), '
            elif char_gain_roll <= 27:
                name += 'T +10), '
            elif char_gain_roll <= 36:
                name += 'Agi +10), '
            elif char_gain_roll <= 45:
                name += 'A +1), '
            elif char_gain_roll <= 54:
                name += 'Fel +10), '
            elif char_gain_roll <= 63:
                name += 'Int +10), '
            elif char_gain_roll <= 72:
                name += 'WP +10), '
            elif char_gain_roll <= 75:
                name += 'WS +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 77:
                name += 'S +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 79:
                name += 'T +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 81:
                name += 'Agi +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 83:
                name += 'A +'+str(random.randint(1, 3))+'), '
            elif char_gain_roll <= 85:
                name += 'Fel +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 87:
                name += 'Int +'+str(random.randint(1, 3)*10)+'), '
            elif char_gain_roll <= 89:
                name += 'WP +'+str(random.randint(1, 3)*10)+'), '
        elif enchantment == '3':
            char_drain_roll = random.randint(1, 80)
            name += 'Characteristic Drain ('
            if char_drain_roll <= 15:
                name += 'WS -10), '
            elif char_drain_roll <= 30:
                name += 'S -10), '
            elif char_drain_roll <= 40:
                name += 'T -10), '
            elif char_drain_roll <= 50:
                name += 'Agi -10), '
            elif char_drain_roll <= 60:
                name += 'Fel -10), '
            elif char_drain_roll <= 70:
                name += 'Int -10), '
            elif char_drain_roll <= 80:
                name += 'WP -10), '
        elif enchantment == '4':
            name += 'Bane ('
            bane_roll = random.randint(1, 100)
            if bane_roll <= 5:
                name += 'Goblins and Snotlings'
            elif bane_roll <= 10:
                name += 'Hobgoblins'
            elif bane_roll <= 20:
                name += 'Orcs'
            elif bane_roll <= 25:
                name += 'All Goblinoids'
            elif bane_roll <= 27:
                name += 'Elementals'
            elif bane_roll <= 30:
                name += 'Daemons'
            elif bane_roll <= 35:
                name += 'Undead'
            elif bane_roll <= 45:
                name += 'Non-Daemonic creatures and followers of Chaos'
            elif bane_roll <= 50:
                name += 'Dragons'
            elif bane_roll <= 55:
                name += 'All reptiles'
            elif bane_roll <= 60:
                name += 'Dwarfs, Gnomes and Halflings'
            elif bane_roll <= 65:
                name += 'Elves'
            elif bane_roll <= 70:
                name += 'Fimir'
            elif bane_roll <= 75:
                name += 'Giant Animals'
            elif bane_roll <= 80:
                name += 'Skaven'
            elif bane_roll <= 85:
                name += 'Giants'
            elif bane_roll <= 90:
                name += 'Ogres and Trolls'
            elif bane_roll <= 95:
                name += 'Werecreatures'
            elif bane_roll <= 100:
                name += 'Vampires'
            name += '), '
        elif enchantment == '16':
            name += 'Protection ('
            protection_roll = random.randint(1, 100)
            if protection_roll <= 75:
                name += '+1 AP in all areas'
            elif protection_roll <= 90:
                name += '+2 AP in all areas'
            elif protection_roll <= 95:
                name += '+3 AP in all areas'
            elif protection_roll <= 98:
                name += '1 Attack per round automatically parried'
            elif protection_roll <= 100:
                name += '2 Attacks per round automatically parried'
            name += '), '
        else:
            name += weapon_enchantment_dict[enchantment]+', '
    name = name[:-2]
    name += ')'
    final_object = [object_id, name, description, source, page]
    return final_object
