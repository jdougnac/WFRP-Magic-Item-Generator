import random
import amulet
import spell

ring_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


ring_dict = {

    '1': ['Amulet Ring', 'The ring has exactly the same effect as the magical amulet of the same name.', 'CORE1',
          '187'],
    '2': ['Energy Ring',
          'Works as a Jewel of Energy. Once per day, can add the amount in parentheses to a spellcasting roll, even'
          'after rolling the dice.',
          'CORE1', '185'],
    '3': ['Fortitude Ring', 'Gives the wearer a +10 bonus on all WP and Cl tests.', 'AN', '46'],
    '4': ['Multiple Spell Ring', 'Contains multiple spells, each of which can be cast once a day without rolling, even'
                                 ' by non-spellcasters.', 'CORE1', '187'],
    '5': ['Multiple Warding Ring', "The wearer becomes completely immune to various spells. If a spellcaster, they"
                                   " can't cast any of them while wearing the ring.", 'CORE1', '187'],
    '6': ['Ring of Protection',
          'The wearer takes half damage from all attacks from the designated monsters, and has a +10 bonus to all tests'
          ' against their spells and special abilities.',
          'CORE1', '187'],
    '7': ['Ring of Elvenkind',
          'Gives the wearer Night Vision up to 30 yards, a +5 Initiative bonus, and +10 to Fellowship tests against'
          ' elves.',
          'AN', '46'],
    '8': ['Spell Ring', 'Contains a spell, which can be cast once per day without rolling, even by non spellcasters.',
          'CORE1', '187'],
    '9': ['Striking Ring',
          'Once per day, for a full turn, and one at a time, the wearer may gain the benefits of Strike Mighty Blow,'
          ' Strike to Injure or Strike to Stun. If they already have the talent, the bonuses are not doubled.',
          'AN', '46'],
    '10': ['Ring of Warding', "The wearer becomes completely immune to a single spell. If a spellcaster, they can't "
                              "cast it while wearing the ring.", 'CORE1', '187']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_ring(is_rune=False):
    choice = str(random.choice(ring_list))
    chosen_object = ring_dict[choice]    
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '1':        
        ring = amulet.pick_amulet(is_rune)
        name = 'Ring' + ring[1][6:]
        description = 'This ring works exactly as the Amulet of the same name. ' + ring[2]
        source = ring[3]
        page = ring[4]
    elif object_id == '2':
        bonus = str(random.randint(1, 6))
        name += ' ('+bonus+')'
    elif object_id == '4' or object_id == '5':
        spell_amount = random.randint(1, 3) + 1
        spell_list = []
        while len(spell_list) < spell_amount:
            spell_mult = spell.pick_spell()
            if spell_mult not in spell_list:
                spell_list.append(spell_mult)
        name += ' ('
        for item in spell_list:
            name += item + ', '
        name = name[:-2]
        name += ')'
    elif object_id == '6':
        roll = random.randint(1, 100)
        if roll <= 5:
            name += ',  Goblins and Snotlings'
        elif roll <= 10:
            name += ',  Hobgoblins'
        elif roll <= 20:
            name += ',  Orcs and Half-Orcs'
        elif roll <= 25:
            name += ',  All goblinoids'
        elif roll <= 27:
            name += ',  Elementals'
        elif roll <= 30:
            name += ',  Demons'
        elif roll <= 35:
            name += ',  Undead and Ethereal Creatures'
        elif roll <= 45:
            name += ',  Creatures of Chaos (including Chaos warriors, etc'
        elif roll <= 50:
            name += ',  Dragons, Wyverns, and Jabberwocks'
        elif roll <= 55:
            name += ',  Elves'
        elif roll <= 60:
            name += ',  Dwarves, Gnomes and Halflings'
        elif roll <= 65:
            name += ',  Fimir'
        elif roll <= 70:
            name += ',  Monstrous Animals (Manticores, Griffins, etc)'
        elif roll <= 75:
            name += ',  Skaven'
        elif roll <= 80:
            name += ',  Lizardmen and Troglodytes'
        elif roll <= 85:
            name += ',  Giants'        
        elif roll <= 90:
            name += ',  Ogres and Trolls'
        elif roll <= 95:
            name += ',  Werecreatures'
        elif roll <= 100:
            name += ',  Vampires'
    elif object_id == '8':
        name += ' (' + spell.pick_spell() + ')'
    elif object_id == '10':
        name += ' (' + spell.pick_spell() + ')'
    final_object = [object_id, name, description, source, page]
    return final_object
