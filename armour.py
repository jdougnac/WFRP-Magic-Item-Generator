import random
import glove
import boot


armour_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


armour_dict = {
    '1': ['Mail Coif', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN', '48'],
    '2': ['Plate Helmet', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN',
          '48'],
    '3': ['Mail Shirt', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN', '48'],
    '4': ['Mail Coat', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN', '48'],
    '5': ['Sleeved Mail Shirt', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.',
          'AN', '48'],
    '6': ['Sleeved Mail Coat', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.',
          'AN', '48'],
    '7': ['Mail Leggings', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN',
          '48'],
    '8': ['Plate Greaves', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN',
          '48'],
    '9': ['Plate Arms', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN', '48'],
    '10': ['Breastplate', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN',
           '48'],
    '11': ['Shield', 'For an explanation of the powers, go to the corresponding Apocrypha Now section.', 'AN', '48']
}

head_enchantments = ['Berserk', 'Breathe Underwater', 'Flight', 'Flight', 'Hatred', 'Hatred',
                     'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                     'Characteristic Gain', 'Characteristic Gain', 'Invisibility', 'Magic Reflection',
                     'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                     'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                     'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                     'Characteristic Gain', 'Characteristic Gain', 'Protection', 'Protection', 'Protection', 
                     'Protection', 'Protection', 'Protection', 'Protection', 'Protection', 'Protection', 'Regeneration',
                     'Regeneration', 'Wizardry', 'Wizardry', 'Protection', 'Protection', 'Protection', 'Protection',
                     'Protection', 'Protection', 'Corrosion', 'Woodbane']

bracer_enchantments = ['Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                       'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                       'Characteristic Gain', 'Area Protection', 'Area Protection', 'Area Protection',
                       'Area Protection', 'Attack Protection', 'Attack Protection', 'Binding', 'Magical Gloves',
                       'Missile Protection', 'Deflection', 'Deflection', 'Wizardry', 'Corrosion', 'Woodbane']

legging_enchantments = ['Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                        'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain', 'Characteristic Gain',
                        'Area Protection', 'Area Protection', 'Area Protection', 'Area Protection', 'Attack Protection',
                        'Attack Protection', 'Dodging', 'Kicking', 'Leaping', 'Magical Boots', 'Movement', 'Wizardry',
                        'Corrosion', 'Woodbane']

shield_enchantments = ['Charging', 'Invisibility', 'Light', 'Magic Missile Protection', 'Missile Protection',
                       'Missile Reflection', 'Area Protection', 'Spell Absorption', 'Spell Reflection',
                       'Weapon Breaker', 'Corrosion', 'Woodbane']

# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def char_bonus_body(characteristic_list, char_roll):
    if char_roll <= 25:
        characteristic_list[0] += 10
    elif char_roll <= 50:
        characteristic_list[1] += 10
    elif char_roll <= 75:
        characteristic_list[2] += 10
    elif char_roll <= 80:
        characteristic_list[0] += random.randint(1, 3) * 10
    elif char_roll <= 85:
        characteristic_list[1] += random.randint(1, 3) * 10
    elif char_roll <= 90:
        characteristic_list[1] += random.randint(1, 3) * 10


def attack_protection():
    protects_against = 'ERROR ATTACK_PROTECTION FUNCTION'
    attack_protection_roll = random.randint(1, 100)
    if attack_protection_roll <= 5:
        protects_against = 'goblins and Snotlings'
    elif attack_protection_roll <= 10:
        protects_against = 'hobgoblins'
    elif attack_protection_roll <= 20:
        protects_against = 'orcs'
    elif attack_protection_roll <= 25:
        protects_against = 'all Goblinoids'
    elif attack_protection_roll <= 27:
        protects_against = 'elementals'
    elif attack_protection_roll <= 30:
        protects_against = 'daemons (including Daemon Weapons)'
    elif attack_protection_roll <= 35:
        protects_against = 'undead'
    elif attack_protection_roll <= 45:
        protects_against = 'non-Daemonic creatures and followers of Chaos'
    elif attack_protection_roll <= 50:
        protects_against = 'dragons'
    elif attack_protection_roll <= 55:
        protects_against = 'all reptiles'
    elif attack_protection_roll <= 60:
        protects_against = 'dwarfs, Gnomes and Halflings'
    elif attack_protection_roll <= 65:
        protects_against = 'elves'
    elif attack_protection_roll <= 70:
        protects_against = 'fimir'
    elif attack_protection_roll <= 75:
        protects_against = 'giant Animals'
    elif attack_protection_roll <= 80:
        protects_against = 'skaven'
    elif attack_protection_roll <= 85:
        protects_against = 'giants'
    elif attack_protection_roll <= 90:
        protects_against = 'ogres and Trolls'
    elif attack_protection_roll <= 95:
        protects_against = 'werecreatures'
    elif attack_protection_roll <= 100:
        protects_against = 'vampires'
    return protects_against


def area_protection():    
    power = ''
    area_protection_roll = random.randint(1, 100)
    if area_protection_roll <= 15:
        power += 'non-magical blunt hand weapons'
    elif area_protection_roll <= 40:
        power += 'non-magical edged and pointed hand weapons'
    elif area_protection_roll <= 60:
        power += 'non-magical missile weapons'
    elif area_protection_roll <= 80:
        power += 'natural weapons'
    elif area_protection_roll <= 95:
        power += 'non-magical fist weapons'
    elif area_protection_roll <= 100:
        power += 'all non-magical weapons'
    return power
                 

def pick_enchantments(amount_enchantments, enchantment_list):
    object_enchantments = []
    while len(object_enchantments) < amount_enchantments:
        pick = random.choice(enchantment_list)
        if pick not in object_enchantments:
            object_enchantments.append(pick)
    return object_enchantments


def pick_armour(is_rune = False, is_chaos = False):
    choice = str(random.choice(armour_list))
    chosen_object = armour_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]

# this if loop checks the amount of
# extra enchantments the object will have
# (the first enchantment is always an AP bonus)

    # this determines how many enchantments a given item has
    # the number is always one less than shown on AN
    # because there the first enchantment is always
    # a bonus to the AP given by the object
    enchantments = 0
    if object_id == '1' or object_id == '7':
        roll = random.randint(1, 100)
        if roll > 90:
            enchantments = 1
        else:
            enchantments = 0

    elif object_id == '2':
        roll = random.randint(1, 100)
        if 75 < roll < 91:
            enchantments = 1
        elif 90 < roll < 100:
            enchantments = 2
        elif roll == 100:
            enchantments = 3

    elif object_id == '3' or object_id == '4' or object_id == '5' or object_id == '6':
        roll = random.randint(1, 100)
        if 80 < roll < 96:
            enchantments = 1
        elif roll > 96:
            enchantments = 2

    elif object_id == '8' or object_id == '9':
        roll = random.randint(1, 100)
        if 90 < roll < 100:
            enchantments = 1
        elif roll == 100:
            enchantments = 2

    elif object_id == '10':
        roll = random.randint(1, 100)
        if 75 < roll < 91:
            enchantments = 1
        elif 90 < roll < 97:
            enchantments = 2
        elif 96 < roll < 100:
            enchantments = 3            
        elif roll == 100:
            enchantments = 4

    elif object_id == '11':
        roll = random.randint(1, 100)
        if 90 < roll < 97:
            enchantments = 1
        elif roll > 96:
            enchantments = 2

    # this roll determines the
    # amount of enhanced protection
    protection_bonus = random.randint(1, 100)
    if protection_bonus <= 10:
        name += ', +1, '
    elif protection_bonus <= 80:
        name += ', +2, '
    elif protection_bonus <= 95:
        name += ', +3, '
    elif protection_bonus > 95:
        name += ', +4, '        


# this loop will pick the extra enchantments, if there are any
    if object_id == '1' or object_id == '2':
        head_item_enchantments = pick_enchantments(enchantments, head_enchantments)
        for power in head_item_enchantments:
            name += power
            if power == 'Hatred':
                name += ' ('
                hatred_roll = random.randint(1, 100)
                if hatred_roll <= 5:
                    name += 'Goblins and Snotlings'
                elif hatred_roll <= 10:
                    name += 'Hobgoblins'
                elif hatred_roll <= 20:
                    name += 'Orcs'
                elif hatred_roll <= 25:
                    name += 'All Goblinoids'
                elif hatred_roll <= 27:
                    name += 'Elementals'
                elif hatred_roll <= 30:
                    name += 'Daemons'
                elif hatred_roll <= 35:
                    name += 'Undead'
                elif hatred_roll <= 45:
                    name += 'Non-Daemonic creatures and followers of Chaos'
                elif hatred_roll <= 50:
                    name += 'Dragons'
                elif hatred_roll <= 55:
                    name += 'All reptiles'
                elif hatred_roll <= 60:
                    name += 'Dwarfs, Gnomes and Halflings'
                elif hatred_roll <= 65:
                    name += 'Elves'
                elif hatred_roll <= 70:
                    name += 'Fimir'
                elif hatred_roll <= 75:
                    name += 'Giant Animals'
                elif hatred_roll <= 80:
                    name += 'Skaven'
                elif hatred_roll <= 85:
                    name += 'Giants'
                elif hatred_roll <= 90:
                    name += 'Ogres and Trolls'
                elif hatred_roll <= 95:
                    name += 'Werecreatures'
                elif hatred_roll <= 100:
                    name += 'Vampires'
                name += ')'
            elif power == 'Characteristic Gain':
                name += ' ('
                characteristic_gain_roll = random.randint(1, 100)
                if characteristic_gain_roll <= 15:
                    name += '+10 Agi'
                elif characteristic_gain_roll <= 30:
                    name += '+10 Fel'
                elif characteristic_gain_roll <= 45:
                    name += '+10 Int'
                elif characteristic_gain_roll <= 75:
                    name += '+10 WP'
                elif characteristic_gain_roll <= 80:
                    name += '+'+str(random.randint(1, 3)*10)+' Agi'
                elif characteristic_gain_roll <= 85:
                    name += '+'+str(random.randint(1, 3)*10)+' Fel'
                elif characteristic_gain_roll <= 90:
                    name += '+'+str(random.randint(1, 3)*10)+' Int'
                elif characteristic_gain_roll <= 100:
                    name += '+'+str(random.randint(1, 3)*10)+' WP'
                name += ')'
            elif power == 'Protection':
                name += ' ('
                protection_roll = random.randint(1, 100)
                if protection_roll <= 5:
                    name += 'Animosity'
                elif protection_roll <= 55:                    
                    name += 'Area Protection (' + area_protection() + ')'
                elif protection_roll <= 60:
                    name += 'Compulsions'
                elif protection_roll <= 70:
                    name += 'Fear and Terror'
                elif protection_roll <= 75:
                    name += 'Gaze Attacks'
                elif protection_roll <= 80:
                    name += 'Insanity'
                elif protection_roll <= 85:
                    name += 'Instability'
                elif protection_roll <= 90:
                    name += 'Illusions'
                elif protection_roll <= 95:
                    name += 'Stupidity'
                elif protection_roll <= 100:
                    name += 'All psychological effects'
                name += ')'
            elif power == 'Wizardry':
                name += '(PENDING!!!!)'    
            name += ', '

# body has a completely different loop, since its configuration allows for powers to repeat themselves,
# so it is not feasible to just pick them from a list or assign a percentage to them.
# for characteristics gain, the reference to an outside function provides for the fact that,
# on a 91+, the table should be rolled twice
    elif object_id == '3' or object_id == '4' or object_id == '5' or object_id == '6' or object_id == '10':
        # position 0 is for S, 1 is for T, 2 is for Agi
        characteristic_gain = [0, 0, 0]
        body_armor_enchantments = []
        temp = 0
        while temp < enchantments:
            power_roll = random.randint(1, 100)
            # in this case, the power is not added immediately, but instead after all powers have been rolled, in order
            # for all char bonuses to be consolidated and to avoid it saying (agi +30, agi +10) or similar.
            if power_roll <= 45:
                chest_char_bonus_roll = random.randint(1, 100)
                if chest_char_bonus_roll <= 90:
                    char_bonus_body(characteristic_gain, chest_char_bonus_roll)
                elif chest_char_bonus_roll > 90:
                    char_bonus_body(characteristic_gain, random.randint(1, 90))
                    char_bonus_body(characteristic_gain, random.randint(1, 90))
                temp += 1
            elif power_roll <= 95:
                chest_protection_roll = random.randint(1, 100)
                if chest_protection_roll <= 10:
                    body_armor_enchantments.append('Area Protection (' + area_protection() + ')')
                elif chest_protection_roll <= 20:
                    body_armor_enchantments.append('Attack Protection (' + attack_protection() + ')')
                elif chest_protection_roll <= 30:
                    body_armor_enchantments.append('Protection (characteristic draining)')
                elif chest_protection_roll <= 40:
                    body_armor_enchantments.append('Protection (fear and terror, including spells that cause them)')
                elif chest_protection_roll <= 50:
                    body_armor_enchantments.append('Protection (fire)')
                elif chest_protection_roll <= 60:
                    body_armor_enchantments.append('Protection (lightning)')
                elif chest_protection_roll <= 70:
                    chest_magic_protection_roll = random.randint(1, 100)
                    if chest_magic_protection_roll <= 25:
                        body_armor_enchantments.append('Protection (petty magic and level 1 spells)')
                    elif chest_magic_protection_roll <= 50:
                        body_armor_enchantments.append('Protection (petty magic)')
                    elif chest_magic_protection_roll <= 60:
                        body_armor_enchantments.append('Protection (petty magic and up to level 2 spells)')
                    elif chest_magic_protection_roll <= 65:
                        body_armor_enchantments.append('Protection (petty magic and up to level 3 spells)')
                    elif chest_magic_protection_roll <= 75:
                        body_armor_enchantments.append('Protection (all battle magic)')
                    elif chest_magic_protection_roll <= 80:
                        body_armor_enchantments.append('Protection (all daemonic magic)')
                    elif chest_magic_protection_roll <= 85:
                        body_armor_enchantments.append('Protection (all elemental magic)')
                    elif chest_magic_protection_roll <= 90:
                        body_armor_enchantments.append('Protection (all illusion magic)')
                    elif chest_magic_protection_roll <= 95:
                        body_armor_enchantments.append('Protection (all necromantic magic)')
                    elif chest_magic_protection_roll <= 98:
                        body_armor_enchantments.append('Protection (all druidic magic)')
                    elif chest_magic_protection_roll <= 100:
                        body_armor_enchantments.append('Protection (all spells)')
                elif chest_protection_roll <= 80:
                    chest_weapon_protection_roll = random.randint(1, 100)
                    if chest_weapon_protection_roll <= 80:
                        body_armor_enchantments.append('Protection (magical weapons, +10 or less to hit or +1 damage )')
                    elif chest_weapon_protection_roll <= 95:
                        body_armor_enchantments.append('Protection (magical weapons, +20 or less to hit or +1 damage )')
                    elif chest_weapon_protection_roll <= 100:
                        body_armor_enchantments.append('Protection (magical weapons, +30 or less to hit or +1 damage )')
                elif chest_protection_roll <= 85:
                    body_armor_enchantments.append('Protection (all non-magical weapons)')
                elif chest_protection_roll <= 100:
                    body_armor_enchantments.append('Protection (all psychological effects)')
                temp += 1
            elif power_roll <= 100:
                if 'Wizardry' not in body_armor_enchantments:
                    body_armor_enchantments.append('Wizardry')
                    temp += 1
        if characteristic_gain[0] != 0:
            str_bonus = 'Characteristic Gain (S +' + str(characteristic_gain[0]) + ')'
            body_armor_enchantments.append(str_bonus)
        if characteristic_gain[1] != 0:
            t_bonus = 'Characteristic Gain (T +' + str(characteristic_gain[1]) + ')'
            body_armor_enchantments.append(t_bonus)
        if characteristic_gain[2] != 0:
            agi_bonus = 'Characteristic Gain (Agi +' + str(characteristic_gain[2]) + ')'
            body_armor_enchantments.append(agi_bonus)
        # the change to set removes duplicates
        body_armor_enchantments = set(body_armor_enchantments)
        body_armor_enchantments = list(body_armor_enchantments)
        if len(body_armor_enchantments) != 0:
            for enchantment in body_armor_enchantments:
                name += str(enchantment) + ', '

    elif object_id == '9':
        bracer_item_enchantments = pick_enchantments(enchantments, bracer_enchantments)
        for power in bracer_item_enchantments:
            name += power
            if power == 'Characteristic Gain':
                name += ' ('
                characteristic_gain_roll = random.randint(1, 5)
                if characteristic_gain_roll <= 4:
                    name += '+10 Agi'
                elif characteristic_gain_roll == 5:
                    name += '+'+str(random.randint(1, 3)*10)+' Agi'
                name += ')'
            elif power == 'Area Protection':
                name += ' (' + area_protection() + ')'
            elif power == 'Attack Protection':
                name += ' (' + attack_protection() + ')'
            elif power == 'Magical Gloves':
                name += ' (' + glove.pick_glove()[1] + ')'
            name += ', '

    elif object_id == '7' or object_id == '8':
        legging_item_enchantments = pick_enchantments(enchantments, legging_enchantments)
        for power in legging_item_enchantments:
            name += power
            if power == 'Characteristic Gain':
                name += ' ('
                characteristic_gain_roll = random.randint(1, 100)
                if characteristic_gain_roll <= 40:
                    name += '+1 Mov'
                elif characteristic_gain_roll <= 80:
                    name += '+10 Agi'
                elif characteristic_gain_roll <= 90:
                    name += '+'+str(random.randint(1, 3))+' Mov'
                elif characteristic_gain_roll <= 100:
                    name += '+'+str(random.randint(1, 3)*10)+' Agi'
                name += ')'
            elif power == 'Area Protection':
                name += ' (' + area_protection() + ')'
            elif power == 'Attack Protection':
                name += ' (' + attack_protection() + ')'
            elif power == 'Magical Boots':
                name += ' (' + boot.pick_boot()[1] + ')'
            name += ', '

    elif object_id == '11':
        shield_item_enchantments = pick_enchantments(enchantments, shield_enchantments)
        for power in shield_item_enchantments:
            name += power
            if power == 'Area Protection':
                name += ' (' + area_protection() + ')'
            name += ', '

    name = name[:-2]
    final_object = [object_id, name, description, source, page]
    return final_object


print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
print(pick_armour(False, False))
