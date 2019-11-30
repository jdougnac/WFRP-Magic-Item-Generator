import random
import extras

special_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

special_dict = {
    '1': ['Dagger of Halflings',
          'For a non-halfling, it works as a magical dagger. For a halfling, it counts as a sword, and gives +10 to'
          ' WS.', 'AN', '47'],
    '2': ['Harness of Fearlessness',
          'When fitted to a horse (not any other rideable creature) it becomes immune to Fear, though not Terror.',
          'AN', '47'],
    '3': ['Lantern of Days', 'Its oil burns very slowly: 1 pint will fuel it for 1d4 days.', 'AN', '47'],
    '4': ['Lens of Detection', 'Allows the user to see illusions for what they truly are. See manual.', 'AN', '47'],
    '5': ['Lyre of Melody', 'It gives +20 to music and busk tests.', 'AN', '47'],
    '6': ['Purse of Teeth',
          'If someone other than the owner tries to take money from it, they take damage. See manual.', 'AN', '47'],
    '7': ['Ring of Comprehension',
          'Allows the wearer to read and write their own language. 50% of them also give knowledge on how to read and'
          ' write 1d3 additional languages.',
          'AN', '47'],
    '8': ['Sand of Flinging',
          'When thrown at a location, all creatures within a four yard radius are blinded, making missile fire and'
          ' spellcasting impossible.', 'AN', '47'],
    '9': ['All-Seeing Mirror',
          'These come in pairs, each seeing the reflection on the other through unlimited distances by land, or up to'
          ' 500 miles of sea.', 'CORE1', '183'],
    '10': ['Enchanted Rope', 'A magical rope that obeys the commands of its owner. See manual.', 'CORE1', '185'],
    '11': ['Golden Death Mask', 'Gives a bonus of +10 to Command and Intimidate, as well as +10 WP.', 'LLL', '93'],
    '12': ['Blades of Honourable Demise', 'Gives a +20 to WS. Parrying. If it wounds, the victim loses an additional'
                                          ' wound each round until they pass a T -10 test,', 'LLL', '94'],
    '13': ['Dagger of Bound Souls', 'If it inflicts at least 1 wound, target suffers 5 more wounds, deals extra wounds,'
                                    ' pierces magical protection. See manual.', 'LLL', '96'],
    '14': ['Gauntlet of Hraklonesh', "S +10, T +10, can't be removed. Each week, make a T -10 check or gain a mutation."
                                     " See manual.", 'LLL', '96'],
    '15': ['Black Diamond Tiara ', 'Zombies controlled by its wearer gain +1 APoint to all locations. ', 'BOTD', '35'],
    '16': ['Blood Opal Brooch ',
           'The wearer gains a +20% bonus to Will Power Tests made to resist spells and effects. ', 'BOTD', '35'],
    '17': ['Gown of Tears ', 'Attacks against its wearer gain no benefit from Ulric’s Fury. ', 'BOTD', '35'],
    '18': ['Amulet of the Horned One ',
           'So long as the character wears it, they regain 1 Wound each hour. The user must continually wear the Amulet'
           ' for an hour to gain its effects. ',
           'COHR', '82'],
    '19': ['Blade of Corruption ',
           'If the wielder inflicts a Wound with it, opponent must make a –10 Toughness Test. On a failed test, it'
           ' takes an additional Damage 3 hit by poison. If used by a non-Skaven, it slowly poisons its wielder. See'
           ' manual.',
           'COHR', '83'],
    '20': ['Cloak of Shadows ',
           'Any creatures attacking the wearer with ranged weapons or magic missiles must pass a –10% WP Test. On a'
           ' failed test, they must select a different target.',
           'COHR', '83'],
    '21': ['Dwarf-Slayer ',
           'Powers: This hand weapon inflicts SB+3 Damage vs. Dwarfs, and Critical Hits against dwarves have +3 Value.'
           ' If used by a non-Skaven, it devours the mind of the wielder. See manual.',
           'COHR', '83'],
    '22': ['Fellblade',
           'It is a sword with Impact that inflicts SB+1 Damage. Skavens wielding it have +20 S. Each round they wield'
           ' it, they must pass a –20 T roll or take a Damage 3 hit that ignores armour and Toughness. For non-Skaven'
           ' the check is at -30 and the hit has Damage 5.',
           'COHR', '83'],
    '23': ['The Foul Pendant',
           'Curls of green foul-smelling smoke rise from it, granting the wearer 2 Armour Points to all locations. The'
           ' protection granted from this device overlaps with any armour worn.',
           'COHR', '83'],
    '24': ['Staff of the Horned One ',
           ' Its wielder may cast an additional Lesser Magic Spell of their choosing. Once selected, the wielder cannot'
           ' change it. If the item changes owners, the new possessor selects a new Lesser Magic Spell.',
           'COHR', '83'],
    '25': ['Algrund’s Orrery ',
           'It gives a +20% to Academic Knowledge (Astronomy) Tests, except rolls to determine its function. It can'
           ' create darkness in an area of ten square miles. This effect lasts for one hour and can be used once per'
           ' day.',
           'NDM', '122'],
    '26': ['Asp Bow ',
           'Arrows fired from it deal Damage 4 and function as if poisoned. If they cause at least 1 Wound, the target'
           ' must make a T roll or lose 2 more Wounds. On a BS result of 96–00, the arrow bites the wielder on the'
           ' hand, dealing normal damage. Vampires are immune to the poison.',
           'NDM', '122'],
    '27': ['Blood Chalice',
           'Its bearer may use it as a full-round action. It has two effects: drinking from it restores 1d10 Wounds to'
           ' the drinker, and using it to coat a weapon causes flames to leap up along it, granting a +2 bonus to'
           ' damage.',
           'NDM', '122'],
    '28': ['Carstein Ring',
           'If Vampires of the Von Carstein bloodline wear this ring, they gain 3 Armour Points on all locations and,'
           ' at the start of each round, regenerate 1d10 Wounds. If the wearer is killed, he returns to un-life at dusk'
           ' completely healed.',
           'NDM', '123'],
    '29': ['The Dagger of Jet ',
           'Anyone wounded by it loses 10 S or T, at the wielder’s choosing. Neither may be reduced to 0. If the victim'
           ' survives, 1% of each characteristic regenerates each hour.',
           'NDM', '123'],
    '30': ['Lady Zmada’s Portrait ',
           'A Vampire may step through the empty frame of this portrait during the day and shelter there until dusk.'
           ' During that time, the Vampire appears as an unmoving portrait of itself. If the painting is destroyed, the'
           ' Vampire is slain.',
           'NDM', '123'],
    '31': ['Necrotic Powder ',
           'It magically ages anything it touches. Only practitioners of necromancy are immune to this effect. Usually'
           ' the necromancer blows a handful of the substance at a target (BS Test), which inflicts 2d10 Wounds. ',
           'NDM', '123'],
    '32': ['Vampire’s Bane ',
           'This is a silver greatsword with a skull device on the pommel. The bearer’s Strength Bonus is doubled when'
           ' using Vampire’s Bane against Vampires.',
           'NDM', '123'],
    '33': ['The Wailing Blade ',
           'As it moves through the air, the blade wails for the blood of men. This forces anyone within 6 yards (3'
           ' squares) to re-roll all successful Fear and Terror Tests. Once drawn in battle, the wielder must make a '
           '–20 WP roll to sheath it whilst living combatants remain.',
           'NDM', '123'],
    '34': ['The Gloves of Jarfreit ', 'The wearer gets +10 to WS and S.', 'SOA', '42'],
    '35': ['The Amulet of Say-K’thar ',
           'The wearer gets +1 to cast all arcane spells. In addition, the amulet may be consumed to guarantee the'
           ' successful casting of a single spell, even if it would normally be impossible for the caster. ',
           'SOA', '42'],
    '36': ['The Crown of Pashtilar ',
           ' No servant of Chaos (including Daemons, Mutants, and cultists) will make the first attack against the'
           ' bearer. In addition, they are inclined to listen to what she says and give it serious consideration. This'
           ' does not grant the wearer any extra powers of persuasion, but it does grant a hearing.',
           'SOA', '42'],
    '37': ['The Cards of Master Wilhelm (Two of Swords) ',
           'The bearer can make one person refuse to acknowledge a single fact. See Manual.', 'SOA', '59'],
    '38': ['The Cards of Master Wilhelm (Five of Wands)',
           'The bearer may take a +10% bonus to any Opposed Skill Test. Every time she does so, she will later take a'
           ' –5% penalty on an unopposed Skill Test, as circumstances conspire to undermine her attempt. The max bonus'
           ' on a test is +10%, but the GM may apply any number of penalties, up to the number owed, to the same Skill'
           ' Test.',
           'SOA', '59'],
    '39': ['Rod of Separation ',
           'Separates an essence from a possessed object and forcibly returns it to the Realm of Chaos.', 'FON', '79'],
    '40': ['Donnacanto',
           'When the wielder charges, it sings, allowing allies within earshot to re-roll previously failed Fear Tests.'
           ' This re-roll—and all subsequent Fear Tests—are made at +10 as long as it can be heard. The spear continues'
           ' singing until combat ends.',
           'TT', '175'],
    '41': ['Chalice of Shared Secrets', 'Can deliver messages to servants of Nurgle. See manual.', 'TT', '221'],
    '42': ['The Foetid Wind ',
           'Living creatures that lose 1 Wound from it must pass a T roll or die in TB rounds. In addition, the wielder'
           ' gains +10 to WS, S, and a +1 A against Elves. ',
           'TT', '221'],
    '43': ['Gangrenous Tooth',
           ' When installed inside the user’s mouth, it burrows into the owner’s brain, sending tendrils of power'
           ' through the being. Any damage dealt by its wielder does not heal naturally until another character'
           ' successfully passes a Heal Test to clean out the injury.',
           'TT', '221'],
    '44': ['Black Skull of the Caliph',
           'When mounted on a pole, it grants a +10% bonus to Fear and Terror Tests to all allies within 8 yards (4'
           ' squares).',
           'ROS2', '204'],
    '45': ['Charm of Hotek',
           'It grants the wearer immunity to fire and +1 Armour Point to all locations. Also, they take –20 to WP rolls'
           ' to resist Chaos effects and gain an additional mutation beyond any other mutations they gain.',
           'ROS2', '204'],
    '46': ['Dazh’s Flint',
           'When touched to a flammable object, such as tinder, cloth, hair (though not flesh), or paper, it '
           'automatically catches flame.',
           'ROS2', '204'],
    '47': ['Doomfire Ring',
           'Once per day, by passing a WP roll, the wielder can fire ball as if he had Magic. A character with the Lore'
           ' of Fire may use the Doomfire Ring a number of additional times per day equal to his Magic.',
           'ROS2', '205'],
    '48': ['Elf Charm',
           'It may be used as an additional ingredient for casting spells from the Lore of Life, doubling the modifier'
           ' for all other ingredients used.',
           'ROS2', '205'],
    '49': ['Fauschlag Ring', 'The wearer gains +10 WS.', 'ROS2', '205'],
    '50': ['Griffon Claw', 'The wearer gains +10 WS.', 'ROS2', '205'],
    '51': ['Helstrum’s Staff', 'Gives +20 Fel for Public Speaking or preaching to a crowd.', 'ROS2', '205'],
    '52': ['Maid’s Charm', 'When worn by a female, she cannot conceive a child.', 'ROS2', '205'],
    '53': ['Orb of Ghrond', 'Grants visions in exchange of madness, Dark Elves are immune. See manual.', 'ROS2', '206'],
    '54': ['Power Stone', 'Allows the user to roll 2 extra Magic Dice when casting spell. Are consumed upon use.',
           'ROS2', '206'],
    '55': ["Scrivener's Candle",
           "When reading by its light, the reader gains +20 Int. It can burn for a total of 24 hours.", 'ROS2', '207'],
    '56': ['Scroll of the Fifth Lore',
           'Appears to be whatever the reader expects to see. Thus, if handed to a literate guard with the explanation'
           ' that the scroll is in fact a writ of passage, a license, or some other document, the guard would see it as'
           ' such.',
           'ROS2', '207'],
    '57': ['Silver Seal',
           'All attacks against the wearer are at –10. It also grants the wearer +20 to WP checksto resist hostile'
           ' spells.',
           'ROS2', '207'],
    '58': ['Skull Charm', 'Grants +5 WS.', 'ROS2', '207'],
    '59': ['Skull Charm', 'Grants +10 to Fear checks.', 'ROS2', '207'],
    '60': ['Skull Charm', 'Grants +5 to WS and BS.', 'ROS2', '207'],
    '61': ['Skull Charm', 'Grants +10 to WS, BS, and Fear tests. It also speaks.', 'ROS2', '207'],
    '62': ['Talisman of Ulrics', 'The wearer of this Talisman regains 1 Wound at the start of their turn each round.',
           'ROS2', '207'],
    '63': ['The Black Amulet', '50% chance of rebounding damage. See manual.', 'ROS1', '160'],
    '64': ['Golden Eye of Tzeentch', 'All enemies in melee with the wearer must pass WP each round or stay immobile.'
                                     ' See manual.', 'ROS1', '160'],
    '65': ['Blood Drinker',
           'Broadsword. Each time it deals damage, it drains 10 S. If it reaches 0, the target dies. S is recovered at'
           ' a pace of 10 per day.',
           'ROS1', '161'],
    '66': ['Book of Ashur',
           'Allows a wizard to cast any spell, as long is it is within one level of his magic level (see the Notes'
           ' document for the conversion). After that, WP roll or gains 1d6 IP and ventures into the Realms of Chaos.'
           ' See manual.',
           'ROS1', '161'],
    '67': ['Bottle Tower of Grimnyth the Great',
           'Allows users to teleport to the tower that exists inside the bottle. See manual.', 'ROS1', '161'],
    '68': ['Chalice of Sorcery',
           'Once per round, a wizard may cast a spell without rolling dice. Then, roll 1d6. On a 6, loses 1d6 wounds.'
           ' See manual.',
           'ROS1', '162'],
    '69': ['Crown of Sorcery',
           'Allows the user to cast necromancy spells without rolling dice. Then, make WP roll. If failed, they are'
           ' prone for a round. If the roll is 96 or more, they journey to the Lands of the Dead. See manual.',
           'ROS1', '162'],
    '70': ["Daemon's Cradle",
           'It can contain a single demon inside. If one comes within 6 squares from it, they must roll WP -50. If they'
           ' fail, they are trapped in it.',
           'ROS1', '162'],
    '71': ['Gilded Armour',
           'Gives +1 AP on all locations. Attackers on melee must pass a S roll in order to attack the wearer.', 'ROS1',
           '162'],
    '72': ["Erik's Sword of Confusion", 'Damage is -3 against everything except dairy products.', 'ROS1', '162'],
    '73': ['Runefang', 'Ignores all armour, including magical, as well as T. Deals double damage against undead.',
           'ROS1', '162'],
    '74': ['Spear of Seeking',
           'If the full name of a foe within 150 yards is spoken, and the spear is thrown, it impacts without rolling'
           ' BS. If the name is wrong, the spear attacks the user instead.',
           'ROS1', '164'],
    '75': ['Tomb-Blade of Arkhan',
           'Anyone killed by it must roll WP, or their soul goes into the blade. Can only be used safely by a'
           ' necromancer, vampire, or liche. See manual.',
           'ROS1', '164']

}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_special():
    choice = str(random.choice(special_list))
    chosen_object = special_dict[choice]
    object_id = choice
    name = chosen_object[0]
    description = chosen_object[1]
    source = chosen_object[2]
    page = chosen_object[3]
    if object_id == '7':
        roll = random.randint(1, 2)
        if roll == 1:
            name += ': '
            extra_languages = random.randint(1, 3)
            language_list = random.sample(extras.languages, k=extra_languages)
            for item in language_list:
                name += item + ', '
            name = name[:-2]
        elif roll == 2:
            name += ': no extra languages'

    elif object_id == '8':
        roll = str(random.randint(1, 4))
        if roll == '1':
            name += ': ' + roll + ' use'
        else:
            name += ': ' + roll + ' uses'

    elif object_id == '10':
        name += ' ('
        roll = str(random.randint(1, 6) + 2)
        owner = random.randint(1, 2)
        name += roll + ' feet, '
        if owner == 1:
            name += 'no current owner)'
        elif owner == 2:
            name += 'its owner still lives)'

    final_object = [object_id, name, description, source, page]
    return final_object
