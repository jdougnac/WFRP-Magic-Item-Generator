import random
import spell

potion_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
               '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36',
               '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53',
               '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
               '71', '72']

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
    '8': ['Cursed Potion: ', 'Gives a damaging effect. See the word document.', 'CORE1', '187'],
    '9': ['Potion of Answering',
          'Anyone who drinks this potion must tell the truth when asked a question until its effects wear off.', 'ROS1',
          '164'],
    '10': ['Potion of Attention', 'Gives a +30 to all perception-related rolls while its effects last.', 'ROS1', '164'],
    '11': ['Potion of Beauty',
           'While its effects last, the user cannot be recognized. They gain +10 Fel, or +20 against members of their'
           ' own race.',
           'ROS1', '164'],
    '12': ['Potion of Bravery', 'Gives a +30 to WP while its effects last.', 'ROS1', '164'],
    '13': ['Potion of Chaos', 'Gives 1d3 IP. Also, it causes 1d3 temporary Chaos Mutations. See manual.', 'ROS1',
           '165'],
    '14': ['Potion of Charm', 'Gives +10 Fel while its effects last.', 'ROS1', '165'],
    '15': ['Potion of Charisma',
           'Gives +30 Fel while its effects last. Anyone seeing the user must pass a WP roll or try to monopolize their'
           ' attention.',
           'ROS1', '165'],
    '16': ['Potion of Cleverness', 'Gives +20 Int while its effects last.', 'ROS1', '165'],
    '17': ['Potion of Concealment', 'Gives the Concealment skill while its effects last.', 'ROS1', '165'],
    '18': ['Potion of Cowardice',
           'Subjects the user to fear and gives it a -20 to WP. While the effects last, the user must make a Fear check'
           ' each time the circumstances change.',
           'ROS1', '165'],
    '19': ['Potion of Dancing', 'Makes the user dance until the effect wears off.', 'ROS1', '165'],
    '20': ['Potion of Dissent', 'The user suffers animosity against the first person they see after drinking it.',
           'ROS1', '165'],
    '21': ['Potion of Drunkenness',
           'The user becomes heavily drunk, falling asleep after 1d6 *10 minutes. They only wake up after 3d6 hours.'
           ' When they do, they have -10 to Agi, Int, WP, and Fel for 1d6 hours.',
           'ROS1', '165'],
    '22': ['Potion of Dullness',
           'The user is affected by stupidity, and their Int is halved until the effect wears off.', 'ROS1', '166'],
    '23': ['Potion of Eagle-Eyes', 'The user can see in detail within up to three miles while the effects last.',
           'ROS1', '166'],
    '24': ['Potion of Empathy',
           'The user can sense the emotions of any member of their race with whom they make eye contact.', 'ROS1',
           '166'],
    '25': ['Potion of Fire-Breathing',
           'Allows the user to breathe fire like a dragon, one time. It uses the cone template, dealing one impact of '
           'Strength 8.',
           'ROS1', '166'],
    '26': ['Potion of Fire-Walking', 'Makes the user immune to normal (not magical) fire until the effect wears off.',
           'ROS1', '166'],
    '27': ['Potion of Floating',
           'The user floats to 10 feet above ground. It can only move at half speed unless there is wind. ', 'ROS1',
           '166'],
    '28': ['Potion of Friendliness', 'Double the Fel of the user, to a maximum of 99.', 'ROS1', '166'],
    '29': ['Potion of Fortitude', 'Gives the user a +10 to WP while its effects last.', 'ROS1', '166'],
    '30': ['Potion of Frustration', 'Gives the user a -30 to all perception-related tests while its effects last.',
           'ROS1', '166'],
    '31': ['Potion of Glowing', 'The user starts glowing, giving light like that of a lantern.', 'ROS1', '166'],
    '32': ['Potion of Growth',
           "The user grows to twice their size over 1d3 minutes, increading their S by 50%. Their gear doesn't grow"
           " with them.",
           'ROS1', '167'],
    '33': ['Potion of Happiness',
           'Gives a -20 to Int and WP, as well as a +30 to Fel. Must make a WP roll to avoid agreeing to anything that'
           ' is suggested to them.',
           'ROS1', '167'],
    '34': ['Potion of Hearing', 'Grants the talent Acute Hearing while its effects last.', 'ROS1', '167'],
    '35': ['Potion of Immunity', 'Gives immunity to disease and poison for 3d6 hours.', 'ROS1', '167'],
    '36': ['Potion of Invulnerability', 'The user becomes invulnerable to non-magical weapons while the effects last.',
           'ROS1', '167'],
    '37': ['Potion of Leadership',
           'Gives +20 Fel to the user, making them seem like a legendary hero, akin to Magnus or Sigmar. The effects'
           ' last for 3d6 rounds.',
           'ROS1', '167'],
    '38': ['Potion of Lesser Healing', 'The user recovers 1d6 wounds.', 'ROS1', '167'],
    '39': ['Potion of Life',
           'Makes the user immune to physical and special damage from Undead, but not from their spells, while the'
           ' effect lasts.',
           'ROS1', '167'],
    '40': ['Potion of Loathsomeness',
           'The user becomes unrecognizable, and gets a -40 to Fel. The effects last for 1d3 hours.', 'ROS1', '167'],
    '41': ['Potion of Luck', 'The user gains the talent luck until the next sunrise or sunset, whichever comes first.',
           'ROS1', '168'],
    '42': ['Potion of Loyalty',
           'The user becomes loyal to any person speaking to them while they drink it. The effect lasts for 3d6 days.'
           ' It gives the "leader" a +25 to tests related to loyalty against the user.',
           'ROS1', '168'],
    '43': ['Potion of Melting', 'Causes the user to become a formless blob. See manual.', 'ROS1', '168'],
    '44': ['Potion of Noise',
           'Makes the user extremely noisy: all words are heard as if shouted, and all sounds they make are amplified.',
           'ROS1', '168'],
    '45': ['Potion of Owl-Eyes', 'Grants the talent Night Vision while the effect lasts.', 'ROS1', '168'],
    '46': ['Potion of Shape-Changing',
           'The user can change into a non-fantastic, non-giant creature while the effects last. The creature is'
           ' determined at potion creation. See manual.',
           'ROS1', '168'],
    '47': ['Potion of Shrinking',
           'The user is reduced to a quarter of their size over 1d3 minutes, getting -20 S while the effect lasts.',
           'ROS1', '168'],
    '48': ['Potion of Skill',
           'The user gets a +40 to all building or crafting rolls, as well as +20 to Agi while the effect lasts.',
           'ROS1', '168'],
    '49': ['Potion of Spell Casting',
           'Allows the user to cast the spell associated with it once, without rolling the dice.', 'ROS1', '168'],
    '50': ['Potion of Spider Arms',
           'The arms of the user becomes three times as long, allowing them to make melee attacks at three times the'
           ' normal distance, even over the heads of other party members.',
           'ROS1', '169'],
    '51': ['Potion of Spider-Walking',
           'If not carrying anything in their hands, the user can move up walls or across ceilings like a spider.',
           'ROS1', '169'],
    '52': ['Potion of Spite',
           'The user becomes subject to hatred of the first thing they see after drinking the potion, or the creatures'
           ' between parentheses.',
           'ROS1', '169'],
    '53': ['Potion of Stone',
           'Turns the user to stone while the effects last. Their T becomes 100 and they are immune to most spells'
           ' (GM discretion).',
           'ROS1', '169'],
    '54': ['Potion of Stone-Walking',
           'The user turns into a moving block of stone. Their S and Wounds are doubled, and their T is set to 80 while'
           ' the effects last.',
           'ROS1', '169'],
    '55': ['Potion of Terror',
           'The WP of the user is halved, and it is subject to Terror towards the first thing they see after drinking'
           ' the potion, while the effects last.',
           'ROS1', '169'],
    '56': ['Potion of Toughness', 'Gives the user +20 T while the effect lasts.', 'ROS1', '169'],
    '57': ['Potion of Water-Breath',
           'Allows the user to breathe, move, fight, speak, and cast spells normally while underwater, for 12 hours.',
           'ROS1', '169'],
    '58': ["Boar's Musk",
           'Gives the user a -20 to Fel, and everyone within 4 yards gets a -5 to WS and BS due to the foul smell.'
           ' Lasts for 1d10 hours. Lag 2 hours.',
           'ROS2', '198'],
    '59': ['Channelpath Potion', 'The user gets +15 to Channeling rolls for 1d10 minutes.', 'ROS2', '198'],
    '60': ["Debauch's Friend",
           'Makes the user immune to the negative effects of alcohol, though retaining its enjoyment, for 1d10 hours.',
           'ROS2', '198'],
    '61': ['Draught of Lizard Limbs',
           'Regrows a lost limb. 50% chance for it to be the wrong one (for example, a leg where an arm should go).'
           ' Lag 24 hours.',
           'ROS2', '198'],
    '62': ['Draught of Power', 'If the user is a spellcaster, increases its Magic by 1 for 2 rounds. Lag 1 round.',
           'ROS2', '199'],
    '63': ["God's Spit",
           'When applied to the thumbs, the user unarmed attacks count as if they were using gauntlets, and gain +5 T'
           ' and Agi for 1d10 minutes. Lag 1 round.',
           'ROS2', '199'],
    '64': ['Hair Tonic',
           'When applied to an area, it grows hair profusely. If drank, hair grows on the mouth, giving -20 Fel. Lag 15'
           ' minutes.',
           'ROS2', '199'],
    '65': ['Lucidity Tonic',
           'Gives a +20 to Int and WP for 3d10 hours. During this time it is impossible to fall asleep. Once it passes,'
           ' the user falls exhausted, sleeping for 3d10 hours. Lag 1 hour.',
           'ROS2', '199'],
    '66': ['Nectar of Beauty',
           "Moves scars and blemishes in the face to other parts of the body. +10 to Fel rolls against those affected"
           " by the user's gender for 3d10 hours. While the effect lasts, bright lights become annoying, giving a -5 to"
           " all primary characteristics. Lag 1 hour.",
           'ROS2', '199'],
    '67': ['Potency Draught', 'Increases S and T by 15 for 1d10 hours. Lag 1d10/2 rounds.', 'ROS2', '199'],
    '68': ['Potion of Comeliness',
           'Gives a +20 to Fel for 2d10 hours. When the effect ends, roll T -10 or get Int lowered by 5. Additionally,'
           ' each week roll WP -20 to resist gaining and taking another dose. This effect ends if three rolls in a row'
           ' are passed.',
           'ROS2', '200'],
    '69': ['Potion of Pain Denied',
           'Makes the user immune to pain. They are immune to torture, and gain +20 T for 1d10 hours. Lag 1d10/2'
           ' rounds.',
           'ROS2', '200'],
    '70': ['Potion of Perceptive Clarity',
           'For 1d10/2 hours, the user gains the Acute Hearing and Excellent Vision talents. Lag 1 round.', 'ROS2',
           '200'],
    '71': ['Potion of Teeth',
           'When applied to a broken or missing tooth, regenerates it. If applied to other areas, teeth grow in it. Lag'
           ' 1 hour.',
           'ROS2', '200'],
    '72': ['Slimming Liquor',
           'Burns the fat of the target, though it does nothing for their skin. The stink gives a -10 Fel for 1d10'
           ' hours. Lag 8 hours.',
           'ROS2', '200'],

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

    elif object_id == '46':
        shape_change_list = ['Bat', 'Bear', 'Cat', 'Small Dog', 'Large Dog', 'Eagle', 'Frog', 'Horse', 'Lizard',
                             'Monkey', 'Rat', 'Raven', 'Robin', 'Snake', 'Weasel', 'Squirrel', 'Wolf']
        shape = random.choice(shape_change_list)
        name += ' (' + shape + ')'

    elif object_id == '49':
        spell_cast = spell.pick_spell()
        name += ' (' + spell_cast + ')'

    elif object_id == '52':
        spite_roll = random.randint(1, 100)
        if spite_roll <= 15:
            name += ' (first creature they see)'
        else:
            specific_spite_roll = random.randint(1, 100)
            name += ' ('
            if specific_spite_roll <= 5:
                name += 'Halflings'
            elif specific_spite_roll <= 10:
                name += 'Wild Animals'
            elif specific_spite_roll <= 20:
                name += 'Orcs'
            elif specific_spite_roll <= 25:
                name += 'Humans'
            elif specific_spite_roll <= 27:
                name += 'Undead'
            elif specific_spite_roll <= 35:
                name += 'Greenskins'
            elif specific_spite_roll <= 45:
                name += 'Chaos Followers'
            elif specific_spite_roll <= 50:
                name += 'Dragons'
            elif specific_spite_roll <= 55:
                name += 'Trolls'
            elif specific_spite_roll <= 60:
                name += 'Dwarfs'
            elif specific_spite_roll <= 65:
                name += 'Elfs'
            elif specific_spite_roll <= 70:
                name += 'Daemons'
            elif specific_spite_roll <= 75:
                name += 'Lizardmen'
            elif specific_spite_roll <= 80:
                name += 'Skavens'
            elif specific_spite_roll <= 85:
                name += 'Giants'
            elif specific_spite_roll <= 90:
                name += 'Ogres'
            elif specific_spite_roll <= 95:
                name += 'Lycanthropes'
            elif specific_spite_roll <= 100:
                name += 'Vampires'
            name += ')'

    final_object = [object_id, name, description, source, page]
    return final_object

