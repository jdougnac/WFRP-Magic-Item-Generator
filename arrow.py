import random

arrow_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8,
              8, 8, 8, 8, 8, 9, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14,
              14, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 18, 18, 25, 25, 25, 25, 25, 26, 19, 19, 20,
              20, 21, 21, 22, 22, 23, 23, 23, 24, 24]

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
          "It always hits, though it's still necessary to roll in order to determine where it hits.", 'CORE1', '184'],
    '9': ['Arrow of Cursed Bone', 'When wounded, test T or die and become a Zombie.', 'Apo2', '88'],
    '10': ['Arrow of Direful Summonation', 'When they strike an object, a random creature is summoned.', 'Apo2', '88'],
    '11': ['Arrow of Far Flight', 'It reaches double the distance.', 'Apo2', '88'],
    '12': ['Arrow of Fear', 'Upon being hit, the victim must make a Fear or Terror check. See manual.', 'Apo2', '88'],
    '13': ['Arrow of Fire', 'Makes extra damage upon hitting a target: 1d4 if normal target, 2d4 if flammable, triple'
                            ' damage if it hits a water elemental.', 'Apo2', '88'],
    '14': ['Arrow of Ice', 'Upon hitting, deals 1d3 extra damage if the target fails a T test, or triple damage to fire'
                           ' elementals. See manual.', 'Apo2', '88'],
    '15': ['Arrow of Madness', 'Anyone hit by it with an int of 10 or more gains 2d6 insanity points.', 'Apo2', '89'],
    '16': ['Arrow of Might', 'It hits with S 10.', 'Apo2', '89'],
    '17': ['Arrow of Mind Stealing', 'Adds a special effect when it impacts. See manual.', 'Apo2', '89'],
    '18': ['Arrow of Pestilence', 'Causes infected wounds upon hitting a target. See manual.', 'Apo2', '89'],
    '19': ['Arrow of Sleep', "Doesn't cause damage, upon hitting, target must make a WP check or fall asleep. See"
                             " manual.", 'Apo2', '90'],
    '20': ['Arrow of Sluggish Doom', 'Causes an effect upon impact. See manual.', 'Apo2', '90'],
    '21': ['Arrow of Venom', 'If target survives the strike, it must pass a T test or die.', 'Apo2', '90'],
    '22': ['Arrow of the Warp', 'Ignores all non-magical armour.', 'Apo2', '90'],
    '23': ['Arrow of Weakening', 'Causes an effect upon impact. See manual.', 'Apo2', '91'],
    '24': ['Arrow of Wounding', "Causes extra wounds. If the base attack doesn't cause wounds, it doesn't have any "
                                "effect.", 'Apo2', '91'],
    '25': ['Arrow of Piercing', 'Ignores non-magical armour and shields. See manual.', 'Apo2', '90'],
    '26': ['Arrow of Rightful Banishment', 'Forces target of the associated creature type to make an instability check'
           ' at -3.', 'Apo', '90']

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

    elif object_id == '3':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

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

    elif object_id == '6':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

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
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '8':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '9':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '10':
        summon_roll = random.randint(1, 100)
        name += ' ('
        if summon_roll <= 5:
            name += str(random.randint(1, 3)) + ' Bloodletters'
        elif summon_roll <= 10:
            name += str(random.randint(1, 3)) + ' Daemonettes'
        elif summon_roll <= 15:
            name += str(random.randint(1, 3)) + ' Plaguebearers'
        elif summon_roll <= 20:
            name += str(random.randint(1, 3)) + ' Pink Horrors'
        elif summon_roll <= 21:
            name += 'Bloodthirster'
        elif summon_roll <= 22:
            name += 'Keeper of Secrets'
        elif summon_roll <= 23:
            name += 'Great Unclean One'
        elif summon_roll <= 24:
            name += 'Lord of Change'
        elif summon_roll <= 34:
            name += 'Air Elemental, size ', str(random.randint(1, 6)+4)
        elif summon_roll <= 44:
            name += 'Earth Elemental, size ', str(random.randint(1, 6)+4)
        elif summon_roll <= 54:
            name += 'Fire Elemental, size ', str(random.randint(1, 6)+4)
        elif summon_roll <= 64:
            name += 'Water Elemental, size ', str(random.randint(1, 6)+4)
        elif summon_roll <= 74:
            name += str(random.randint(1, 6)) + ' Skeletons'
        elif summon_roll <= 84:
            name += str(random.randint(1, 6)) + ' Zombies'
        elif summon_roll <= 89:
            name += str(random.randint(1, 3)) + ' Mummies'
        elif summon_roll <= 94:
            name += str(random.randint(1, 3)) + ' Ghouls'
        elif summon_roll <= 97:
            name += str(random.randint(1, 3)) + ' Wraiths'
        elif summon_roll <= 99:
            name += str(random.randint(1, 3)) + ' Wights'
        elif summon_roll <= 100:
            name += 'Spectre'
        name += ')'

    elif object_id == '11':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '12':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'
        name += ' ('
        fear_effect_roll = random.randint(1, 100)

        if fear_effect_roll <= 75:
            name += 'Fear, individual'
        elif fear_effect_roll <= 90:
            name += 'Terror, individual'
        elif fear_effect_roll <= 97:
            name += 'Fear, mass'
        elif fear_effect_roll <= 100:
            name += 'Terror, mass'
        name += ')'

    elif object_id == '13':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '14':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '15':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '16':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '17':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'
        name += ' ('
        mind_stealing_roll = random.randint(1, 100)

        if mind_stealing_roll <= 30:
            name += 'WP -10'
        elif mind_stealing_roll <= 60:
            name += 'Int -10'
        elif mind_stealing_roll <= 75:
            name += 'WP -20'
        elif mind_stealing_roll <= 90:
            name += 'Int -20'
        elif mind_stealing_roll <= 95:
            name += 'WP -20, make Stupidity test'
        elif mind_stealing_roll <= 100:
            name += 'Int -20, make Stupidity test'
        name += ')'

    elif object_id == '19':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '20':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'
        name += ' ('
        sluggish_doom_roll = random.randint(1, 100)

        if sluggish_doom_roll <= 15:
            name += 'Mov -1'
        elif sluggish_doom_roll <= 60:
            name += 'Agi -10'
        elif sluggish_doom_roll <= 95:
            name += 'Agi -20'
        elif sluggish_doom_roll <= 100:
            name += 'Agi -20, Mov -1'
        name += ')'

    elif object_id == '21':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '23':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'
        name += ' ('
        weakening_roll = random.randint(1, 100)
        if weakening_roll <= 25:
            name += 'WS -10'
        elif weakening_roll <= 50:
            name += 'S -10'
        elif weakening_roll <= 75:
            name += 'T -10'
        elif weakening_roll <= 83:
            name += 'WS -20'
        elif weakening_roll <= 92:
            name += 'S -20'
        elif weakening_roll <= 100:
            name += 'T -20'
        name += ')'

    elif object_id == '24':
        arrow_amount = random.randint(1, 3)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'
        name += ' ('
        wounding_roll = random.randint(1, 100)
        if wounding_roll <= 50:
            name += '+1'
        elif wounding_roll <= 75:
            name += '+2'
        elif wounding_roll <= 90:
            name += '+3'
        elif wounding_roll <= 95:
            name += '+4'
        elif wounding_roll <= 100:
            name += '*2'
        name += ')'

    elif object_id == '25':
        arrow_amount = random.randint(1, 6)
        if arrow_amount > 1:
            name += ' ('+str(arrow_amount)+')'

    elif object_id == '26':
        name += ' ('
        rightful_banishment_roll = random.randint(1, 100)
        if rightful_banishment_roll <= 20:
            name += 'Undead'
        elif rightful_banishment_roll <= 40:
            name += 'Undead and Ethereal Creatures'
        elif rightful_banishment_roll <= 60:
            name += 'Elementals'
        elif rightful_banishment_roll <= 80:
            name += 'Daemons'
        elif rightful_banishment_roll <= 85:
            name += 'Undead, Ethereal Creatures and Elementals'
        elif rightful_banishment_roll <= 90:
            name += 'Undead, Ethereal Creatures and Daemons'
        elif rightful_banishment_roll <= 95:
            name += 'Elementals and Daemons'
        elif rightful_banishment_roll <= 100:
            name += 'All creatures subject to instability'
        name += ')'
    final_object = [object_id, name, description, source, page]
    return final_object
