import random

chaos_weapon_property_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                              25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
                              47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
                              69, 70, 71, 72, 73, 74, 75, 76, 77, 78]

khorne_weapon_property_list = [2, 3, 4, 6, 12, 13, 16, 17, 22, 28, 29, 34, 40, 41, 44, 45, 59, 60, 64, 69, 75, 77, 78]
nurgle_weapon_property_list = [3, 10, 11, 15, 17, 18, 21, 30, 34, 39, 46, 51, 52, 56, 58, 63, 65, 66, 74, 76]
slaanesh_weapon_property_list = [3, 8, 9, 10, 14, 17, 19, 21, 27, 31, 32, 33, 34, 36, 37, 39, 47, 49, 50, 55, 61, 62,
                                 68, 71]
tzeentch_weapon_property_list = [1, 3, 5, 7, 10, 11, 17, 20, 21, 23, 24, 25, 26, 34, 35, 37, 38, 42, 43, 48, 53, 54,
                                 57, 67, 70, 72]
special_chaos_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

grimoire_chaos_list = [1, 2, 3, 4, 5, 6]

potion_chaos_list = [1, 2, 3, 4, 5]

weapon_chaos_list = [1, 2, 3, 4, 5]

chaos_gods_list = ['Khorne', 'Nurgle', 'Slaanesh', 'Tzeentch']

weapon_type_list = ['Dagger', 'Cavalry Spear', 'Flail', 'Foil', 'Knuckle-duster', 'Great Sword', 'Great Axe',
                    'Halberd', 'Lance', 'Main Gauche', 'Morning Star ', 'Quarterstaff', 'Rapier', 'Spear',
                    'Sword-breaker', 'Hand Axe', 'Long Sword', 'Great Sword', 'Great Sword', 'Great Sword',
                    'Main Gauche',
                    'Foil', 'Foil', 'Long Sword', 'Long Sword', 'Long Sword', 'Long Sword', 'Long Sword']

chaos_weapon_property_dict = {
    '1': 'Animated',
    '2': 'Banishment',
    '3': 'Bewitched',
    '4': 'Blood Drinker',
    '5': 'Breathe',
    '6': 'Chainsword',
    '7': 'Chill Blast',
    '8': 'Command',
    '9': 'Cool',
    '10': 'Coward',
    '11': 'Creature',
    '12': 'Deathdealer',
    '13': 'Deathlust',
    '14': 'Deflection',
    '15': 'Degeneration',
    '16': 'Disenchantment',
    '17': 'Enchanted',
    '18': 'Enfeeble',
    '19': 'Entrancing',
    '20': 'Fade',
    '21': 'Fear',
    '22': 'Ferocity',
    '23': 'Fiery Blast',
    '24': 'Flame',
    '25': 'Flight',
    '26': 'Freeze',
    '27': 'Glittering',
    '28': 'Hacking',
    '29': 'Hate',
    '30': 'Howling',
    '31': 'Hurling',
    '32': 'Illusion',
    '33': 'Immunity',
    '34': 'Impunity',
    '35': 'Intelligence',
    '36': 'Lashing',
    '37': 'Leadership',
    '38': 'Levitation',
    '39': 'Maddening',
    '40': 'Magic Absorption',
    '41': 'Magic Destroyer',
    '42': 'Magic Force',
    '43': 'Magic Reflection',
    '44': 'Might',
    '45': 'Mighty Strike',
    '46': 'Mind Eater',
    '47': 'Morbid',
    '48': 'Mutating',
    '49': 'Parry',
    '50': 'Piercing',
    '51': 'Plague',
    '52': 'Poisonous',
    '53': 'Protection',
    '54': 'Random',
    '55': 'Relic',
    '56': 'Resilience',
    '57': 'Riposte',
    '58': 'Sanctity',
    '59': 'Savage',
    '60': 'Screaming',
    '61': 'Shrieking',
    '62': 'Singing',
    '63': 'Slacken',
    '64': 'Slaying',
    '65': 'Sleep',
    '66': 'Slime',
    '67': 'Spell',
    '68': 'Stealing',
    '69': 'Strength',
    '70': 'Summoning',
    '71': 'Swiftness',
    '72': 'Tooth of Tzeentch',
    '73': 'Warp',
    '74': 'Weakening',
    '75': 'Will',
    '76': 'Wounding',
    '77': 'Vampire',
    '78': 'Vicious'
}

weapon_chaos_dict = {
    '1': ['The Axes of Khorgor', 'Wielder gains +1 A and +20 WS. If not a beastman, must pass T -10 or gain the'
                                 ' Turnskin mutation.', 'TOC', '178'],
    '2': ['The Black Maul', 'Wielder gains +20 S and the Frenzy talent. If not a beastman or follower of Khorne, must'
                            ' roll WP at the beginning of each combat or enter a murderous frenzy until there is no'
                            ' one alive within 20 yards.', 'TOC', '180'],
    '3': ['Death Head of Nurgle', 'Can be thrown to spread the Neiglish Rot. See manual', 'TOC', '181'],
    '4': ['Great Fang', 'Ignores all AP on a hit. User must test T each week or gain a mutation.', 'TOC', '181'],
    '5': ['Rending Sword', 'If it deals at least 1 wound, automatically deals 3 more wounds that ignore T and armour.'
                           ' If not fed daily, it runs off to feed by itself. See manual.', 'TOC', '182']

}

potion_chaos_dict = {
    '1': ['Allure', 'Consuming it causes vivid, pleasant dreams that may or not be prophetic, with the risk of'
                    ' attracting something from the Realm of Chaos. See manual.', 'TOC', '88'],
    '2': ['Cordial of Tzeentch', 'Randomly affects all Characteristics of the consumer, for 1d10 hours. See manual.',
          'TOC', '89'],
    '3': ['Plaguesooth Balm', 'It frees the victim of a disease from their suffering. They must roll WP -20 or become'
                              ' addicted to Plaguesooth Balm, and may gain a mutation. See manual.', 'TOC', '89'],
    '4': ['Warpstone', 'It is a powerful ingredient when casting spells, but extremely corrupting. Its precise effects'
                       ' depend of their form. See manual.', 'TOC', '89'],
    '5': ['Bloodstone', 'Can be crushed to ask for the help of Khorne when fighting a spellcaster. See manual.',
          'TOC', '180'],


}

special_chaos_dict = {
    '1': ['A Grim Feast', 'Viewer must pass WP -10 or enter a frenzy for 1d10 hours or until he kills his immediate'
                          ' family.'
                          ' See manual.', 'TOC', '80'],
    '2': ['The Blessed Ones', 'Viewer must pass WP or gain 1 IP. If they drop blood on the painting, two demons try to'
                              ' kidnap them. See manual.', 'TOC', '81'],
    '3': ['The Eye of Morkar', "Can be used as an ingredient for any spell, giving a bonus equal to the Magic of the"
                               " caster. If Tzeentch's Curse happens, roll twice and keep the worst result.", 'TOC',
          '87'],
    '4': ['The Helm of Iron and Blood', 'Varios effects, attracts those with high WS. See manual.', 'TOC', '87'],
    '5': ['The Jade Idol', 'All spells around it are considered as if using Dhar (see CORE 2 p. 97). Can be used'
                           ' as an ingredient for rituals. See manual.', 'TOC', '88'],
    '6': ['Beguiling Gem', "Bearer gains +20 to Fel tests. Opponents trying to attack the bearer must pass WP -10 or be"
                           " unable to attack that round. If the user doesn't have the Mark of Slaanesh, each time they"
                           " touch the gem must pass WP -10 or gain 1d10 IP.", 'TOC', '179'],
    '7': ['Bindings of Slaanesh', 'If used by someone with the Mark of Slaanesh, they gain 1 IP. When they take damage,'
                                  ' S, T and Fel gain +1d10 for 1 hour. It is impossible to withdraw from combat with'
                                  ' the bearer. If not, the straps cause 2 wounds per week and cannot be taken off. See'
                                  ' manual.', 'TOC', '179'],
    '8': ['Collar of Khorne', 'When worn, +30 to rolls for resisting spells. Casters targeting the wearer must pass a'
                              ' WP roll or the spell fails. If worn by someone other than the intended user, they gain'
                              ' a mutation and must roll WP -10 or become a Chaos Spawn.', 'TOC', '181'],
    '9': ['Crown of Everlasting Conquest', "The wearer gains the benefit of the Regeneration mutation. If the wearer"
                                           "doesn't have at least one Gift or Reward of Chaos, they gain a random"
                                           " mutation.", 'TOC', '181'],
    '10': ['The Dark Heart', 'The wearer gains Mov. +3. Each week, they gain 1 IP. If they gain a disorder, it will be'
                             ' Blasphemous Rage', 'TOC', '181'],
    '11': ['Fur of Sharrgu', "Gives 4 AP to all locations, only against ranged attacks (including magic). Can't be"
                             " combined with other armour. If the user isn't a Beastman, they gain a mutation, take -20"
                             " to resist mutations, and become a Chaos Spawn after 4 mutations.", 'TOC', '181'],
    '12': ['Helm of Many Eyes', 'Wearer gains +2d10 to Initiative rolls. When in combat, they are affected by Bewilder '
                                '(CORE 2, p. 158) unless they pass WP -10,', 'TOC', '182'],
    '13': ['Pendant of Slaanesh', 'Whenever the wearer takes damage, they gain +1 Attack for 1 round. If the wearer is'
                                  ' not a servant of Slaanesh, instead they get -1 Attack for 1 round.', 'TOC', '182']

}

grimoire_chaos_dict = {
    '1': ['The Celestine Book of Divination', 'If read completely, Chaos Warrior becomes a Career Exit for this'
                                              ' character.'
                                              ' See manual.', 'TOC', '82'],
    '2': ['Catalogue of Flesh', 'Characters can check for Daemonology as if they had the skill, or check at +20 if they'
                                ' have it. Holds the True Names of 66 daemons. Each hour, a daemon might free itself.'
                                ' See'
                                ' manual.', 'TOC', '83'],
    '3': ['Codex of Unspeakable Damnation', 'Contains heaps of useful rituals and spells of Chaos. Every three days'
                                            ' spent'
                                            ' studying it, roll T +10 or gain a mutation. See manual.', 'TOC', '84'],
    '4': ['Liber Malefic', 'Effects change depending whether it is an edited or full copy. See manual.', 'TOC', '85'],
    '5': ['The Tome of Corruption', 'Gives a +10 to Daemonology, Magic, Magical Sense, Speak Arcane Language Daemonic'
                                    ' and'
                                    ' Speak Dark Tongue. Each time it is read, roll WP or gain 1 IP. See manual.',
          'TOC',
          '86'],
    '6': ['Book of Secrets', 'Allows the user to cast from the Lore of Death, Fire or Shadow and gives +1 Mag. Has side'
                             ' effects, see manual.', 'TOC', '180'],


}

# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def random_creature_type():
    random_creature_roll = random.randint(1, 100)
    if random_creature_roll <= 5:
        random_creature = 'Animals'
    elif random_creature_roll <= 15:
        random_creature = 'Beastmen and Minotaurs'
    elif random_creature_roll <= 17:
        random_creature = 'Birds including Great Eagles'
    elif random_creature_roll <= 27:
        random_creature = 'Chaos Spawn'
    elif random_creature_roll <= 28:
        random_creature = 'Lesser Daemons'
    elif random_creature_roll <= 29:
        random_creature = 'Dragon Ogres'
    elif random_creature_roll <= 34:
        random_creature = 'Dwarfs'
    elif random_creature_roll <= 39:
        random_creature = 'Elves'
    elif random_creature_roll <= 40:
        random_creature = 'Fenbeasts'
    elif random_creature_roll <= 43:
        random_creature = 'Ghouls'
    elif random_creature_roll <= 44:
        random_creature = 'Giants'
    elif random_creature_roll <= 49:
        random_creature = 'Goblins'
    elif random_creature_roll <= 50:
        random_creature = 'Griffons, Hipogriffs, and Pegasi'
    elif random_creature_roll <= 54:
        random_creature = 'Halflings'
    elif random_creature_roll <= 69:
        random_creature = 'Humans'
    elif random_creature_roll <= 70:
        random_creature = 'Lizardmen'
    elif random_creature_roll <= 71:
        random_creature = 'Manticores'
    elif random_creature_roll <= 81:
        random_creature = 'Mutants'
    elif random_creature_roll <= 82:
        random_creature = 'Ogres'
    elif random_creature_roll <= 84:
        random_creature = 'Orcs'
    elif random_creature_roll <= 85:
        random_creature = 'Plants, including Treemen and Dryads'
    elif random_creature_roll <= 87:
        random_creature = 'Skaven'
    elif random_creature_roll <= 90:
        random_creature = 'Spellcasters'
    elif random_creature_roll <= 92:
        random_creature = 'Spiders'
    elif random_creature_roll <= 94:
        random_creature = 'Squigs'
    elif random_creature_roll <= 95:
        random_creature = 'Trolls'
    elif random_creature_roll <= 96:
        random_creature = 'Unicorns'
    elif random_creature_roll <= 97:
        random_creature = 'Vampires and Werecreatures'
    elif random_creature_roll <= 98:
        random_creature = 'Wights and Wraiths'
    elif random_creature_roll <= 99:
        random_creature = 'Witch Hunters and Priests'
    elif random_creature_roll <= 100:
        random_creature = 'Wyverns'
    return random_creature


def pick_weapon_chaos():

    chaos_god = random.choice(chaos_gods_list)
    if chaos_god == 'Khorne':
        chaos_powers_list = khorne_weapon_property_list
    elif chaos_god == 'Nurgle':
        chaos_powers_list = nurgle_weapon_property_list
    elif chaos_god == 'Slaanesh':
        chaos_powers_list = slaanesh_weapon_property_list
    elif chaos_god == 'Tzeentch':
        chaos_powers_list = tzeentch_weapon_property_list
    special_weapon_chaos_roll = random.randint(1, 100)
    weapon_type = random.choice(weapon_type_list)
    if special_weapon_chaos_roll > 95:
        choice = str(random.choice(weapon_chaos_list))
        chosen_object = weapon_chaos_dict[choice]
    else:
        daemon_weapon_chance_roll = random.randint(1, 100)
        if daemon_weapon_chance_roll > 95:
            choice = '0'
            chosen_object = ['Daemon Weapon (', 'This weapon is possessed by a Daemon or Daemon Prince. See manual.',
                             'TOC', '191']
            chosen_object[0] += weapon_type + ', ' + chaos_god + ', '
            bound_daemon_roll = random.randint(1, 100)
            if bound_daemon_roll <= 40:
                chosen_object[0] += 'Lesser Daemon'
            elif bound_daemon_roll <= 66:
                chosen_object[0] += 'Greater Daemon'
            elif bound_daemon_roll <= 90:
                chosen_object[0] += 'Daemon Prince'
            elif bound_daemon_roll <= 100:
                chosen_object[0] += 'Random Daemon (see TOC p. 236)'
            chosen_object[0] += ')'

        else:
            choice = '1'
            chosen_object = ['Chaos Weapon (', 'This weapon serves a Chaos God and has special Chaotic properties. See'
                                               ' manual.',
                             'TOC', '183']
            chosen_object[0] += weapon_type + ', '
            chosen_object[0] += chaos_god + '; '
            amount_properties_roll = random.randint(1, 100)
            if amount_properties_roll <= 50:
                amount_properties = 1
            elif amount_properties_roll <= 75:
                amount_properties = 2
            elif amount_properties_roll <= 85:
                amount_properties = 3
            elif amount_properties_roll <= 95:
                amount_properties = 4
            elif amount_properties_roll <= 100:
                amount_properties = 5
            object_enchantments = []
            while len(object_enchantments) < amount_properties:
                roll_chance_chaos = random.randint(1, 100)
                if roll_chance_chaos > 75:
                    pick = random.choice(chaos_weapon_property_list)
                else:
                    pick = random.choice(chaos_powers_list)
                if pick not in object_enchantments:
                    object_enchantments.append(pick)
                    if pick == 10 or pick == 21:
                        amount_properties += 1
            for enchantment in object_enchantments:
                if enchantment == 11:
                    creature_roll = random.randint(1, 100)
                    chosen_object[0] += 'Creature ('
                    if creature_roll <= 10:
                        chosen_object[0] += 'Basilisk'
                    elif creature_roll <= 25:
                        chosen_object[0] += 'Dragon'
                    elif creature_roll <= 40:
                        chosen_object[0] += 'Minotaur'
                    elif creature_roll <= 55:
                        chosen_object[0] += 'Skeleton'
                    elif creature_roll <= 70:
                        chosen_object[0] += 'Spider'
                    elif creature_roll <= 85:
                        chosen_object[0] += 'Troll'
                    elif creature_roll <= 100:
                        chosen_object[0] += 'Wraith'
                    chosen_object[0] += '), '
                elif enchantment == 12:
                    chosen_object[0] += 'Deathdealer ('
                    chosen_object[0] += random_creature_type()
                    chosen_object[0] += '), '
                elif enchantment == 21:
                    chosen_object[0] += 'Fear ('
                    chosen_object[0] += random_creature_type()
                    chosen_object[0] += '), '
                elif enchantment == 29:
                    chosen_object[0] += 'Hate ('
                    chosen_object[0] += random_creature_type()
                    chosen_object[0] += '), '
                elif enchantment == 51:
                    chosen_object[0] += 'Plague ('
                    if chaos_god == 'Nurgle':
                        chosen_object[0] += 'Neiglish Rot'
                    else:
                        plague_roll = random.randint(1, 100)
                        if plague_roll <= 16:
                            chosen_object[0] += 'The Shakes'
                        elif plague_roll <= 32:
                            chosen_object[0] += 'Eye Rot'
                        elif plague_roll <= 48:
                            chosen_object[0] += 'Creeping Buboes'
                        elif plague_roll <= 64:
                            chosen_object[0] += 'Bone Ague'
                        elif plague_roll <= 80:
                            chosen_object[0] += 'Grey Fever'
                        elif plague_roll <= 96:
                            chosen_object[0] += 'Ochre Pox'
                        elif plague_roll <= 100:
                            chosen_object[0] += 'GM Choice (see CORE 2 pp. 136-137'
                    chosen_object[0] += '), '

                else:
                    chosen_object[0] += chaos_weapon_property_dict[str(enchantment)] + ', '
            chosen_object[0] = chosen_object[0][:-2]
            chosen_object[0] += ')'

    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    return final_object


def pick_potion_chaos():
    choice = str(random.choice(potion_chaos_list))
    chosen_object = potion_chaos_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '4':
        roll = random.randint(1, 90)
        if roll <= 30:
            name += ' (dust)'
        elif roll <= 60:
            name += ' (token)'
        elif roll <= 90:
            name += ' (unrefined)'
    final_object = [object_id, name, description, source, page]
    return final_object


def pick_chaos_grimoire():
    choice = str(random.choice(grimoire_chaos_list))
    chosen_object = grimoire_chaos_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '4':
        roll = random.randint(1, 100)
        if roll <= 75:
            name += ' (edited)'
        elif roll <= 100:
            name += ' (full)'
    final_object = [object_id, name, description, source, page]
    return final_object


def pick_chaos_special():
    choice = str(random.choice(special_chaos_list))
    chosen_object = special_chaos_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    final_object = [object_id, name, description, source, page]
    return final_object
