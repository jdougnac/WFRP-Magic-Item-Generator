import random


rune_talisman_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

master_rune_talisman_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

melee_weapon_category_list = ['1', '2', '2', '2', '3', '4', '5', '6', '7', '7', '7', '8', '8', '8', '8', '9', '10',
                              '11',
                              '12', '12', '13', '14', '15', '16', '17', '18', '18', '18', '18', '18', '19', '19', '19',
                              '19', '19', '19', '19', '18', '18', '20', '20', '20', '21', '21', '21', '21', '20']

rune_melee_weapon_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

master_rune_melee_weapon_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

rune_armour_list = [1, 2, 3, 4, 5, 6, 7]

master_rune_armour_list = [1, 2, 3, 4]

armour_category_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

armour_category_dict = {
    '1': 'Mail Coif',
    '2': 'Plate Helmet',
    '3': 'Mail Shirt',
    '4': 'Mail Coat',
    '5': 'Sleeved Mail Shirt',
    '6': 'Sleeved Mail Coat',
    '7': 'Mail Leggings',
    '8': 'Plate Greaves',
    '9': 'Plate Arms',
    '10': 'Breastplate'
}


rune_armour_dict = {
    '1': '*Rune of Slowness',
    '2': '*Curse Rune',
    '3': 'Rune of Fortitude',
    '4': 'Rune of Iron',
    '5': 'Rune of Resistance',
    '6': 'Rune of Shielding',
    '7': 'Rune of Stone'
}

master_rune_armour_dict = {
    '1': '*Master Rune of Misfortune',
    '2': 'Master Rune of Adamant',
    '3': 'Master Rune of Gromril',
    '4': 'Master Rune of Steel'
}

rune_talisman_dict = {
    '1': '*Curse Rune',
    '2': '*Rune of Battle',
    '3': '*Rune of Enemy Detection',
    '4': '*Rune of Healing',
    '5': '*Rune of Immolation',
    '6': '*Rune of Kadrin',
    '7': '*Rune of Light',
    '8': '*Rune of Restoration',
    '9': '*Rune of Signal',
    '10': '*Rune of Silence',
    '11': 'Rune of Fate',
    '12': 'Rune of the Furnace',
    '13': 'Rune of Luck',
    '14': 'Rune of Spellbreaking',
    '15': 'Rune of Spelleating',
    '16': 'Rune of Warding',
    '17': '*Rune of Slowness'
}

master_rune_talisman_dict = {
    '1': 'Master Rune of Dismay',
    '2': '*Master Rune of Vigour',
    '3': '*Master Rune of Vitality',
    '4': 'Master Rune of Balance',
    '5': 'Master Rune of Kingship',
    '6': 'Master Rune of Spellbinding',
    '7': 'Master Rune of Spite',
    '8': '*Master Rune of Misfortune',
    '9': '*Master Rune of Taunting',
    '10': '*Master Rune of Valaya'
}

melee_weapon_category_dict = {
    '1': 'Buckler',
    '2': 'Dagger',
    '3': 'Cavalry Spear',
    '4': 'Flail',
    '5': 'Foil',
    '6': 'Knuckle-duster',
    '7': 'Great Sword',
    '8': 'Great Axe',
    '9': 'Halberd',
    '10': 'Lance',
    '11': 'Main Gauche',
    '12': 'Morning Star',
    '13': 'Quarterstaff',
    '14': 'Rapier',
    '15': 'Shield',
    '16': 'Spear',
    '17': 'Sword-breaker',
    '18': 'Hand Axe',
    '19': 'Long Sword',
    '20': 'One-Handed Hammer',
    '21': 'Great Hammer'
}

rune_melee_weapon_dict = {
    '1': '*Rune of Frenzy',
    '2': '*Rune of Parrying',
    '3': '*Rune of Transformation',
    '4': 'Rune of Cleaving',
    '5': 'Rune of Fire',
    '6': 'Rune of Fury',
    '7': 'Rune of Grudges',
    '8': 'Rune of Might',
    '9': 'Rune of Striking',
    '10': '*Rune of Cutting',
    '11': '*Rune of Illusion',
    '12': '*Curse Rune'
}

master_rune_melee_weapon_dict = {
    '1': '*Master Rune of Slaying',
    '2': 'Master Rune of Alaric the Mad',
    '3': 'Master Rune of Breaking',
    '4': 'Master Rune of Flight',
    '5': 'Master Rune of Skalf Blackhammer',
    '6': 'Master Rune of Snorri Spanglehelm',
    '7': 'Master Rune of Swiftness',
    '8': '*Master Rune of Smiting',
    '9': '*Master Rune of Misfortune'
}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.

def pick_armour():
    category = armour_category_dict[str(random.choice(armour_category_list))]
    object_id = '1'
    name = 'Rune ' + category + ' ('
    description = 'This armour has one or more runes inscribed. For those with a *, check the Rune document.'
    source = 'ROS2'
    page = '211'
    rune_list = []
    rune_list_final = []
    rune_type = rune_chance()
    if type(rune_type) == int:
        while len(rune_list) < rune_type:
            pick = random.choice(rune_armour_list)
            if pick not in rune_list:
                rune_list.append(pick)
        for item in rune_list:
            rune_list_final.append(rune_armour_dict[str(item)])
        if '*Curse Rune' in rune_list_final:
            rune_list_final = curse_rune(rune_list_final)
        for item in rune_list_final:
            name += item + ', '
        name = name[:-2]
        name += ')'
    else:
        master_rune = master_rune_armour_dict[str(random.choice(master_rune_armour_list))]
        name += master_rune + ')'
    final_object = [object_id, name, description, source, page]
    return final_object


def pick_weapon():
    category = melee_weapon_category_dict[random.choice(melee_weapon_category_list)]
    object_id = '1'
    name = 'Rune ' + category + ' ('
    description = 'This weapon has one or more runes inscribed. For those with a *, check the Rune document.'
    source = 'ROS2'
    page = '211'
    rune_list = []
    rune_list_final = []
    rune_type = rune_chance()
    if type(rune_type) == int:
        while len(rune_list) < rune_type:
            pick = random.choice(rune_melee_weapon_list)
            if pick not in rune_list:
                rune_list.append(pick)
        for item in rune_list:
            rune_list_final.append(rune_melee_weapon_dict[str(item)])
        if '*Curse Rune' in rune_list_final:
            rune_list_final = curse_rune(rune_list_final)
        for item in rune_list_final:
            name += item + ', '
        name = name[:-2]
        name += ')'
    else:
        master_rune = master_rune_melee_weapon_dict[str(random.choice(master_rune_melee_weapon_list))]
        if master_rune == '*Master Rune of Slaying':
            slaying_runes_list = ['Chaotic Creatures', 'Dragons', 'Undead']
            name += 'Master Rune of Slaying (' + random.choice(slaying_runes_list) + ')'
        elif master_rune == 'Master Rune of Flight':
            rune_of_flight_weapon_list = ['One-handed Hammer', 'Great Hammer']
            name = random.choice(rune_of_flight_weapon_list) + ' (Master Rune of Flight)'
        else:
            name += master_rune + ')'
    final_object = [object_id, name, description, source, page]
    return final_object


def pick_talisman(category):
    object_id = '1'
    name = 'Rune ' + category + ' ('
    description = 'This ' + category + ' has one or more runes inscribed. For those with a *, check the Rune document.'
    source = 'ROS2'
    page = '211'
    rune_list = []
    rune_list_final = []
    rune_type = rune_chance()
    if type(rune_type) == int:
        while len(rune_list) < rune_type:
            pick = random.choice(rune_talisman_list)
            if pick not in rune_list:
                rune_list.append(pick)
        for item in rune_list:
            rune_list_final.append(rune_talisman_dict[str(item)])
        if '*Curse Rune' in rune_list_final:
            rune_list_final = curse_rune(rune_list_final)
        if '*Rune of Enemy Detection' in rune_list_final:
            rune_list_final = enemy_detection(rune_list_final)
        for item in rune_list_final:
            name += item + ', '
        name = name[:-2]
        name += ')'
    else:
        master_rune = master_rune_talisman_dict[str(random.choice(master_rune_talisman_list))]
        if master_rune == 'Master Rune of Dismay':
            name = 'Rune Horn (Master Rune of Dismay)'
            description = 'This horn has been engraved with the Master Rune of Dismay.'
        elif master_rune == 'Master Rune of Kingship':
            name = 'Crown of the Dwarven Kings'
            description = 'This massive crown has been engraved with the Master Rune of Kingship.'
        elif master_rune == '*Master Rune of Vigour':
            name = 'Rune Sceptre (*Master Rune of Vigour)'
            description = 'This sceptre has been engraved with the Master Rune of Vigour. See the Rune document.'
        else:
            name += master_rune + ')'
    final_object = [object_id, name, description, source, page]
    return final_object


def curse_rune(rune_list):
    characteristic = ['WS', 'BS', 'S', 'T', 'Agi', 'Int', 'WP', 'Fel']
    affected_characteristic = random.choice(characteristic)
    for item in range(0, len(rune_list)):
        if rune_list[item] == '*Curse Rune':
            rune_list[item] = 'Curse Rune (' + affected_characteristic + ' -10)'
    return rune_list


def enemy_detection(rune_list):
    enemy = ['Greenskins', 'Daemons', 'Undead', 'Dragons', 'Dwarfs, Gnomes and Halflings', 'Elves',
             'Giant Animals', 'Skaven', 'Giants', 'Ogres and Trolls', 'Werecreatures']
    affected_enemy = random.choice(enemy)
    for item in range(0, len(rune_list)):
        if rune_list[item] == '*Rune of Enemy Detection':
            rune_list[item] = '*Rune of Enemy Detection (' + affected_enemy + ')'
    return rune_list


def rune_chance():
    chance = random.randint(1, 100)
    if chance <= 40:
        return 1
    elif chance <= 70:
        return 2
    elif chance <= 90:
        return 3
    elif chance <= 100:
        return 'M'
