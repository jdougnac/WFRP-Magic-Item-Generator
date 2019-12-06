import random
import extras

random_mutation_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                        27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                        51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
                        75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98,
                        99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117,
                        118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
                        137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
                        156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174,
                        174]

khorne_mutation_list = [7, 11, 12, 14, 15, 22, 26, 44, 45, 46, 47, 48, 49, 51, 55, 57, 63, 66, 68, 77, 79, 89, 90, 91,
                        93, 94, 99, 102, 103, 104, 107, 113, 115, 117, 123, 124, 132, 133, 135, 136, 137, 141, 143,
                        150, 156, 162, 164, 166, 169, 170, 172, 173]

nurgle_mutation_list = [1, 8, 10, 11, 14, 16, 17, 18, 23, 27, 29, 30, 37, 41, 48, 44, 45, 46, 47, 49, 56, 58, 59, 60,
                        62, 63, 66, 69, 70, 71, 75, 81, 83, 89, 103, 107, 109, 111, 113, 114, 117, 121, 125, 126, 129,
                        135, 138, 142, 148, 149, 152, 154, 156, 157, 159, 160, 168, 173]

slaanesh_mutation_list = [2, 4, 6, 7, 11, 14, 20, 25, 32, 33, 38, 39, 43, 44, 45, 46, 47, 48, 49, 52, 64, 66, 68, 72,
                          73, 74, 76, 78, 88, 89, 95, 100, 103, 104, 107, 108, 110, 112, 113, 116, 117, 120, 127, 128,
                          129, 135, 139, 143, 145, 148, 149, 151, 153, 156, 158, 163, 164, 171, 172, 173]

tzeentch_mutation_list = [3, 5, 7, 9, 11, 13, 14, 19, 21, 28, 31, 34, 35, 36, 40, 42, 44, 45, 46, 47, 48, 49, 50, 53,
                          54, 61, 65, 66, 67, 72, 73, 80, 82, 83, 84, 85, 87, 86, 89, 92, 96, 97, 98, 101, 104, 105,
                          106, 107, 113, 116, 117, 118, 119, 122, 127, 130, 131, 134, 135, 139, 140, 143, 144, 146,
                          147, 155, 156, 161, 165, 167, 170, 171, 172, 173]

mutation_dict = {

    '1': ['Acid Excretion', "A caustic liquid leaks from the mutant's pores, destroying any armour or clothing. +1d10"
                            " T. Deals extra damage. See manual.", 'TOC', '27'],
    '2': ['Addiction', 'When near the source of addiction, roll WP to avoid sating that desire immediately. Mutant is'
                       ' always considered to be Stinking Drunk.', 'TOC', '27'],
    '3': ['Additional Eye', 'Grows a third eye somewhere. +5 to vision-based Perception rolls.', 'TOC', '27'],
    '4': ['Agile', 'Mutant gains +1d10 Agi.', 'TOC', '30'],
    '5': ['Albino', 'Skin turns stark white, and eyes become blood red. -1d10 T and -5 to Perception checks on bright'
                    ' light.', 'TOC', '30'],
    '6': ['Alluring', 'Blemishes and defects are moved towards non-visible places. +1d10 Fel, +5 to Charm rolls.',
          'TOC', '30'],
    '7': ['Animalistic Legs', "The mutant's legs take the form of a deer's hind legs. +1 Mov.", 'TOC', '30'],
    '8': ['Atrophy', 'One part of the body becomes shriveled and useless. See manual.', 'TOC', '30'],
    '9': ['Beak', "The mutant's mouth becomes a beak. Can be used as a weapon that deals SB -1 Damage.", 'TOC', '30'],
    '10': ['Beast with a Thousand', 'Gain a thousand something, which makes you hideous. -2d10 Fel.', 'TOC', '30'],
    '11': ['Bestial Appearance', "The mutant's head mutates, gaining the appearance of a beast. -2d10 Fel. See manual.",
           'TOC', '31'],
    '12': ['Beweaponed Extremities', "One arm becomes a twisted spur of sharp bone and hardened flesh. Can attack with"
                                     " it as a weapon with Armour Piercing, dealing SB Damage. Can't use two-handed"
                                     " weapons. -1d10 Agi.", 'TOC', '31'],
    '13': ["Bird's Leg", 'Your legs become similar to those of a bird. If the mutant has the Flier talent, the legs'
                         ' count as a Natural Weapon.', 'TOC', '31'],
    '14': ['Bizarre Coloration', 'Part of your skin turns into a different coloration.', 'TOC', '31'],
    '15': ['Blood Lust', 'Gain the Frenzy talent. While frenzied, the face turns into that of a daemon. Once all'
                         ' enemies are killed, roll -10 WP to get out of the trance. If it fails, you attack the'
                         ' nearest creature.', 'TOC', '32'],
    '16': ['Blood Substitution', 'Your blood has been replaced with something else. +1d10 T. See manual.', 'TOC', '32'],
    '17': ['Boils', 'Painful boils erupt in tender and delicate places. -1d10 Agi and -2d10 T.', 'TOC', '32'],
    '18': ['Boneless', 'The bones leave the your body. BS turns 0, all primary characteristics are halved, and Mov'
                       ' turns to 1. Receive +6 Wounds and the Contortionist talent.', 'TOC', '32'],
    '19': ['Breathe Fire', 'Your neck swells enormously. Can spit fire at your enemies, which bypasses armour. See'
                           ' manual.', 'TOC', '32'],
    '20': ['Brightly Patterned Skin', "Small creatures nest in your skin and die, leaving a strange coloration. The "
                                      "colour is of your god's. If you don't follow a god, the GM decides",
           'TOC', '32'],
    '21': ['Burning Body', 'Turn into a pillar of living flame, destroying all your mundane equipment. +1d10 T.', 'TOC',
           '34'],
    '22': ['Centauroid', 'Your legs are replaced by the trunk and legs of some other creature. Mov +2, your legs '
                         'become Natural Weapons. Your hit location table changes, see manual.', 'TOC', '34'],
    '23': ['Chaos Organ', 'You get a disgusting, cancerous cyst. +1d10 T, +2 Wounds, -2d10 Fel. See manual.', 'TOC',
           '35'],
    '24': ['Chaos Spawn', 'You turn into a Chaos Spawn.', 'TOC', '35'],
    '25': ['Chaos Were', 'You turn into your former, mutationless form, until you fail a WP roll. You swap between'
                         ' forms each time you fail a WP check.', 'TOC', '35'],
    '26': ['Claws', 'Your hands turn into hideous claws. Gain Natural Weapon.', 'TOC', '35'],
    '27': ['Cloud of Flies', 'A cloud of flies hovers over you. -10 to melee attacks against you.', 'TOC', '35'],
    '28': ['Cloven Hooves', 'Ýour feet turn into hooves like a goat. No other effect.', 'TOC', '35'],
    '29': ['Corrosive Vomit', 'Your stomach produces extremely acidic juices, like those of a troll. +1d10 T. Once'
                              ' every 1d10 rounds, can vomit at some target. See manual.', 'TOC', '35'],
    '30': ['Cowardice', 'You are overwhelmed by a crippling fear of everything. -20 to all Fear and Terror checks.',
           'TOC', '35'],
    '31': ['Crossbreed', 'Your body warps horribly, turning you into a hybrid with a beast the GM'
                         ' chooses, or the one in parentheses (which is just a suggestion). You also risk turning into'
                         ' a Chaos Spawn. See manual', 'TOC', '35'],
    '32': ['Crown of Flesh', 'You develop fleshy protrustions around your head. No further effect.', 'TOC', '36'],
    '33': ['Crystalline Body', 'Your body turns into solid crystal. +3d10 T, your Wounds are halved.', 'TOC', '36'],
    '34': ['Cyclops', 'You now have one eye, on the center of your forehead. BS is halved.', 'TOC', '36'],
    '35': ['Detachable Limbs', "Your limbs can be detached without risk, but they can't be reattached again. See"
                               " manual.", 'TOC', '36'],
    '36': ['Dimensional Instability', "You become a creature of the realm of Chaos, like a daemon. Any round in which"
                                      " you are damaged in melee and don't deal damage in return, roll WP. If you fail,"
                                      " you're banished to the Realm of Chaos for all eternity.", 'TOC', '36'],
    '37': ['Dripping', 'Your skin leaks a gross yellow fluid. -2d10 Fel.', 'TOC', '36'],
    '38': ['Duplication', 'A new body tears from you, taking with it half your wounds. In most cases, the mutant can'
                          ' control it. See manual.', 'TOC', '36'],
    '39': ['Elastic Limbs', "Your arms become elastic, allowing you to attack at a distance of 1d10*2 yards. If you're"
                            " attacked back,"
                            " those attacks can only hit your arms.", 'TOC', '36'],
    '40': ['Electrical Touch', 'Raw electricity sparks from your skin. +1d10 Agi. See manual.', 'TOC', '36'],
    '41': ['Emaciated Appearance', 'You become thin, almost cadaverous. -1d10 S and T.', 'TOC', '36'],
    '42': ['Enormous Head', "Your head swells to thrice its size. You can't use normal headgear.", 'TOC', '36'],
    '43': ['Evil Eye', 'You can cast a curse on someone within 4 yards. They must make a WP test or suffer a -10 to all'
                       ' characteristics for as long as you live.', 'TOC', '37'],
    '44': ['Extra Joints', 'You gain extra knees, or elbows, or both. See manual.', 'TOC', '37'],
    '45': ['Extra Fingers or Toes', 'You gain extra digits in one or more hands/feet. No further effect.', 'TOC', '37'],
    '46': ['Extra Mouth', 'Another mouth grows in your face. Gain the Ventriloquist talent.', 'TOC', '38'],
    '47': ['Extra Ear', 'Another ear grows in your face. Gain the Acute Hearing talent.', 'TOC', '38'],
    '48': ['Extra Limb', "You gain an extra limb, though it doesn't give any bonuses.", 'TOC', '38'],
    '49': ['Extra Nose', 'You grow another nose on your face. +10 to Perception tests involving smell.', 'TOC', '38'],
    '50': ['Eyestalks', 'One of your eyes extends from the socket on a stalk. You gain +1d10 to Initiative rolls.',
           'TOC', '38'],
    '51': ['Fangs', 'Your teeth grow and sharpen. You may use them as a SB - 2 weapon with the Precise quality.', 'TOC',
           '38'],
    '52': ['Fast', 'You develop uncanny speed. +1 Mov.', 'TOC', '38'],
    '53': ['Fear of Blood', 'Whenever you see blood, you must make a Fear test. ', 'TOC', '38'],
    '54': ['Feathered Hide', 'Your body is covered with feathers. No further effect.', 'TOC', '38'],
    '55': ['Featureless Face', "You lose your eyes, nose, etc., though you can hear, talk, etc. normally. You can't"
                               " eat. Though you don't need food anymore, you still feel hunger.", 'TOC', '38'],
    '56': ['Fits', 'When shocked, you suffer severe seizures. When you fail a Fear or Terror roll, make a WP test or'
                   ' you collapse. Each round you may make another WP test to recover.', 'TOC', '38'],
    '57': ['Flaming Skull Face', 'The skin on your face melts, and the bone then is set on fire. You may attack with'
                                 ' your skull, dealing 1 damage hits ignoring all armour.', 'TOC', '39'],
    '58': ['Foetid Touch', 'Your hands are always grimy and dirty. If you touch any food, it spreads The Galloping'
                           ' Trots.', 'TOC', '39'],
    '59': ['Foul Stench', 'Your body produces a horrible smell, of dirty feet, rancid ham, and vomit. -2d10 Fel. Anyone'
                          ' standing within 2 yards of you gets a -5 to WS.', 'TOC', '39'],
    '60': ['Froglike Eyes', 'Your eyes bulge out from their sockets, like those of a frog, -1d10 Fel.', 'TOC', '39'],
    '61': ['Fur', 'You grow a thin coat of fur. No further effect.', 'TOC', '40'],
    '62': ['Grossly Fat', 'You become horribly fat. Increase weight by 50%. -1d10 S. +1 Wounds.', 'TOC', '40'],
    '63': ['Growth', 'You grow much larger. Double your height, +1d10 S, +1d10 T, -1d10 Agi, +1 Mov, +2 Wounds.', 'TOC',
           '40'],
    '64': ['Head Crest', 'Your head develops a bony crest. No further effect.', 'TOC', '40'],
    '65': ['Headless', 'Your face disappears from your neck and reappears on your chest. -10 to all sight-related'
                       ' rolls. All head hits become body hits. Using normal armour is impossible.', 'TOC', '40'],
    '66': ['Hideous Appearance', 'You become Terrifying.', 'TOC', '40'],
    '67': ['Hopper', 'One of your legs withers and dies, while the other grows strong. Halve your Mov.', 'TOC', '40'],
    '68': ['Horns', 'Horns grow from your forehead, which you can use to make attacks at SB -1 damage.', 'TOC', '40'],
    '69': ['Host of Maggots', 'Maggots infest your whole body. -2d10 T.', 'TOC', '41'],
    '70': ['Hulking Brute', 'You descend into a primitive form, similar to an orc. +1d10 S and T, -2d10 Int.', 'TOC',
           '41'],
    '71': ['Hunchback', "You become grotesquely hunched. You cannot wear body armour unless it's especially crafted for"
                        " you.", 'TOC', '41'],
    '72': ['Hypnotic Gaze', "One of your eyes turns completely white. As a full action, you can target a creature "
                            "within 4 yards. It must roll WP. If it fails, it can't take any action as long as you hold"
                            " your gaze. This roll may be repeated each round.", 'TOC', '41'],
    '73': ['Illusion of Normality', 'All your mutations are hidden from view, until you get into melee combat. ', 'TOC',
           '41'],
    '74': ['Inside Out', "Your body turns inside out. You can't wear normal armour and critical hits against you are at"
                         " +1. -2d10 T.", 'TOC', '41'],
    '75': ['Intelligent Cyst', 'A horrible, intelligent (2d10 + 20 Int) cyst grows inside you. -1d10 T, +4 Wounds.'
                               ' It will try to take control of you. See manual.', 'TOC', '41'],
    '76': ['Invisibility', 'Your body becomes almost translucent. As a half action you can become invisible. Opponents'
                           ' must pass a Perception -20 roll to notice you. Even then, attacks are at -30 and your'
                           ' attacks are at +20. Each round, roll T. If you fail, you suffer 1 wound.', 'TOC', '41'],
    '77': ['Iron Hard Skin', 'Your skin becomes a hard shell of metal scales in a part of your body, which gains 3'
                             ' points of armour incompatible with more armour.', 'TOC', '41'],
    '78': ['Irrational Fear', 'You develop an irrational fear of something. Whenever you encounter it, you must make a'
                              ' Fear check.', 'TOC', '41'],
    '79': ['Irrational Hatred', 'You develop an unreasoning hatred of something. When you see it, you enter into a'
                                ' Frenzy until it is dead or removed from your sight.', 'TOC', '42'],
    '80': ['Large Ears', 'Your ears triple in size. Gain the Acute Hearing talent.', 'TOC', '42'],
    '81': ['Leathery Skin', 'Your skin thickens, becoming hard and leathery. +1d10 T.', 'TOC', '42'],
    '82': ['Levitation', 'You can hover off the ground at will. Gain the Hoverer talent, keeping your Movement for it.',
           'TOC', '42'],
    '83': ['Limb Loss', 'One of your limbs falls off and turns into a disgusting pile of maggots. See CORE 2 p. 134 for'
                        'the effect of lost limbs.', 'TOC', '42'],
    '84': ['Limb Transference', 'A random part of your body moves to another part of your body.', 'TOC', '42'],
    '85': ['Long Legs', 'You legs become unnaturally long. +1 Mov.', 'TOC', '42'],
    '86': ['Long Neck', 'Your neck becomes unnaturally long. Critical hits to the head are at +2.', 'TOC', '43'],
    '87': ['Long Nose', 'Your nose becomes unnaturally long. Gaint the Follow Trail skill. +10 to smell-related'
                        ' Perception tests.', 'TOC', '43'],
    '88': ['Long Spines', 'You become similar to a porcupine. Each round, opponents in melee range must make an Agi'
                          ' check of receive a 1 Damage hit.', 'TOC', '43'],
    '89': ['Madness', 'Gain 1d10/2 Insanity points.', 'TOC', '43'],
    '90': ['Magic Immune', "You can't be affected by any Petty Magic, Lesser Magic or Arcane Lore. If you're a follower"
                           " of Tzeentch, you become a Chaos Spawn.", 'TOC', '43'],
    '91': ['Magic Resistant', "Gain +20 to WP checks to resist magic. Your Magic drops to 0. If you're a follower of"
                              " Tzeentch, you become a Chaos Spawn.", 'TOC', '43'],
    '92': ['Malign Sorcerer', "You gain +1 Mag. You can buy the Dark Lore of the power you follow for 200 xp. If you're"
                              " a follower of Khorne, you're doomed. See manual.", 'TOC', '43'],
    '93': ['Mane of Hair', 'You grow a mane of hair, like a lion. No further effect.', 'TOC', '43'],
    '94': ['Manic Fighter', 'You see anyone you meet as an enemy. Must pass a WP check to avoid entering a murderous'
                            ' frenzy until the triggering creature is chopped to pieces.', 'TOC', '43'],
    '95': ['Manikin', 'A small humanoid protrudes from your head. It takes 25% of the hits to the head, and has 1'
                      ' wound. If it is killed, you are killed too.', 'TOC', '43'],
    '96': ['Massive Intelect', 'Gain +2d10 Int.', 'TOC', '44'],
    '97': ['Mechanoid', 'Some parts of your body are replaced with mechanical ones. You no longer recover Wounds'
                        ' naturally, but you can be healed with an Engineering test. See manual', 'TOC', '44'],
    '98': ['Mer-creature', 'A tail replaces your legs. You gain the Swim skill, and can swim at your full movement'
                           ' speed. In land your Mov. Becomes 1.', 'TOC', '44'],
    '99': ['Metal Body', 'Your body turns to metal. Gain 5 AP in all locations, +3d10 to S and T, and -2d10 to WS and'
                         ' BS. You become immune to fire and cold, but take double damage from electricity.', 'TOC',
           '44'],
    '100': ['Metallic Skin', 'Your skin takes a metallic hue. Gain 2 AP in all locations.', 'TOC', '44'],
    '101': ['Midnight Skin', 'Your skin becomes black as night, and your eyes lose their irises, becoming completely'
                             ' white. +20 to Concealment tests.', 'TOC', '44'],
    '102': ['Mindless', 'Your intelligence drops to 0. You must obey orders given by creatures with Magic 1 or more.',
            'TOC', '44'],
    '103': ['Moronic', 'Your brain shrinks to 1/4 of its normal size. -2d10 Int.', 'TOC', '45'],
    '104': ['Multiple Arms', 'You gain (1d10 + 2)/3 extra arms. +1 Attack, +1d10 T.', 'TOC', '45'],
    '105': ['Multiple Heads', 'You gain 1d10/5 extra heads. Your Attacks must be at least as many as your amount of'
                              ' heads.', 'TOC', '45'],
    '106': ['Multiplication', 'As a full action, you can separate into 1d10 duplicates, dividing your S and Wounds'
                              ' among them. See manual.', 'TOC', '45'],
    '107': ['Overgrown Body Part', 'One body part becomes overgrown, to a greater or lesser extent. See manual.', 'TOC',
            '46'],
    '108': ['Piercing Tongue', 'Your tongue becomes long, sinuous, and sharp. You can make ranged attacks at SB damage'
                               ' with the Precise quality to enemies up to 4 yards away.', 'TOC', '46'],
    '109': ['Pin Head', 'Your head reduces to a fraction of its normal size. -2d10 Int. Must pass an Int test to take'
                        ' any action that requires thought, including swinging a weapon, running away, or moving'
                        ' through a doorway.', 'TOC', '46'],
    '110': ['Pincer Hand', "Your hand becomes a claw similar to a crab's. It becomes a Natural Weapon with the Precise"
                           " quality.", 'TOC', '46'],
    '111': ['Plague Bearer', "You become the carrier of a nasty disease (described on TOC p. 48). It can't kill you,"
                             " but every day check T to"
                             " see if you get affected. Each time you hit an opponent in melee (whether you wound them"
                             " or not), they must check T or contract the disease. If you're a follower of Nurgle,"
                             " ignore the parentheses, you carry Neiglish Rot (CORE 2, p. 136.", 'TOC', '47'],
    '112': ['Pointed Head', 'Your head becomes pointed like a pin. -1d10 Int, you need special armour for the head.',
            'TOC', '47'],
    '113': ['Poisonous Bite', 'Once every 1d10/2 rounds, you can transmit poison through your fangs, dealing SB -2 on a'
                              ' hit, with the Precise quality. If you deal damage, target must pass a T test or gain'
                              ' 1d10/2 wounds ignoring T and armour.', 'TOC', '47'],
    '114': ['Polyps', 'Weird bumps cover your body. They tend to pop and leak a yellow liquid. -1d10 Fel.', 'TOC',
            '47'],
    '115': ['Powerful Legs', 'Your legs become incredibly muscular, increasing how far you can jump. See manual.',
            'TOC', '47'],
    '116': ['Prehensile Tail', 'You grow a prehensile tail, which you can use as a third arm.', 'TOC', '47'],
    '117': ['Pseudo-Daemonhood', 'Your normal form is obliterated, reaplaced instead by a daemonic visage. Gain '
                                 'the Flier and Night Vision talents, as well as the Horns mutation. ', 'TOC', '47'],
    '118': ['Puny', 'Your skeleton shrivels to a quarter of its normal size. Divide your S and T by four.', 'TOC',
            '47'],
    '119': ['Quadruped/ Biped', "If you're a biped, you lose two hands and gain +2 Mov, your BS turns to 0 and you"
                                " can't make melee attacks unless you have extra arms. If you're a quadruped, you gain"
                                " 2 hands and get -2 Mov, you get BS equal to 10 + 1d10. See manual. ", 'TOC', '47'],
    '120': ['Radiant Skin', 'You glow with a strange, purple light. No further effect.', 'TOC', '47'],
    '121': ['Rash', 'You gain some very annoying rash in one part of your body. No further effect.', 'TOC', '49'],
    '122': ['Rearranged Face', 'All your facial features shuffle to a different part of your skull.', 'TOC', '49'],
    '123': ['Regeneration', "Each round, roll T to regain 1 wound. Doesn't work if you're dead.", 'TOC', '49'],
    '124': ['Resilient', 'You are infused with unholy constitution and vitality. +1d10 T.', 'TOC', '49'],
    '125': ['Rotting Flesh', 'Your whole body starts to suppurate and rot, exhuding the stench of death and attracting '
                             'an army of flies. -1d10 T and Fel. See manual.', 'TOC', '49'],
    '126': ['Running Sores', 'Weeping sores cover your body. -2d10 Fel.', 'TOC', '49'],
    '127': ['Scaly Skin', 'A mesh of fine scales sprouts all over your body, granting 1 Armour Point to all locations.',
            'TOC', '49'],
    '128': ['Scorpion Tail', 'sinister-looking tail sprouts from your back. You can attack with it at SB damage. If you'
                             ' deal damage, victim must pass a T -10 roll or die in an amount of rounds equal to their'
                             ' TB.', 'TOC', '49'],
    '129': ['Sensory Loss', 'You lose one sense, together with the organs associated with it. See manual.', 'TOC',
            '49'],
    '130': ['Short Legs', 'Your legs shorten. -1 Mov.', 'TOC', '50'],
    '131': ['Shrink', 'Your body shrinks. Height and weight become half. -1d10 S, -1 Wound and Mov. -1d10 Agi. See'
                      ' manual.', 'TOC', '50'],
    '132': ['Skeleton', 'Your skin falls off, leaving you a skeleton with organs inside. -2d10 WS, BS, and S. -3d10'
                        'Fel. Gain +2d10 Agi. You may no longer take the run action.', 'TOC', '50'],
    '133': ['Skull Face', 'The flesh from your face liquifies and disappears, leaving only your skull. -2d10 Fel.',
            'TOC', '50'],
    '134': ['Snout', 'Your nose twists and transforms into a piggish snout. Gain the Folow Trail skill.', 'TOC', '50'],
    '135': ['Soul Destruction', 'Your soul and personality are destroyed, devoured by Chaos. Your body is possessed by'
                                ' a mortal spirit. See manual.', 'TOC', '50'],
    '136': ['Spiked Tail', 'You grow a tail that ends on a spiked ball. You can attack with it at SB damage, with the'
                           ' Pummeling quality.', 'TOC', '50'],
    '137': ['Spit Acid', 'As a full action, you can make a ranged attack up to 10 yards away, dealing a Damage 5 hit.'
                         ' Can use it again in 1d10 rounds.', 'TOC', '50'],
    '138': ['Spores', "You develop small puffballs, filled with spores like a fungi. When you're hit on melee, they"
                      " explode. Your opponent must pass a T test or lose their next action. Undead and creatures that"
                      " do not breathe are immune to this.", 'TOC', '51'],
    '139': ['Strange Voice', 'Your voice changes. -1d10 Fel.', 'TOC', '51'],
    '140': ['Strange Walk', 'Your gait becomes weird, and a bit silly. -1 Mov.', 'TOC', '51'],
    '141': ['Strong', 'Gain 1d10 S.', 'TOC', '51'],
    '142': ['Suckers', 'Small, quivering suckers appear all over your body. Gain +20 to Scale Sheer Surface tests.',
            'TOC', '51'],
    '143': ['Tail', 'You grow a small tail, gain 1d10 Agi.', 'TOC', '51'],
    '144': ['Telekinesis', 'You gain the ability to move things with your mind. See manual.', 'TOC', '51'],
    '145': ['Telepathy ', 'Gain 1 IP. Making a WP test, you can transmit a short message to a creature within 10 yards.'
                          ' With an opposed WP roll, you can read the surface thoughts of a nearby creature. After, '
                          'roll WP or gain 1 IP.', 'TOC', '51'],
    '146': ['Teleport', 'As a full action, you can make a WP check to teleport. See manual.', 'TOC', '51'],
    '147': ['Temporal Instability', "You are only loosely in this world's time stream. See manual.", 'TOC', '51'],
    '148': ['Tentacle-like Arm', 'One of your arms falls off, being replaced with a tentacle. -30 to tests involving'
                                 ' fine manipulation, but +5 to grappling tests.', 'TOC', '52'],
    '149': ['Tentacle Fingers', 'Your fingers are replaced with tentacles. -10 to tests involving fine manipulation.',
            'TOC', '52'],
    '150': ['Thick Fur', 'A dense fur grows all over your body. Gain 1 AP to all locations.', 'TOC', '52'],
    '151': ['Thorns', 'Small, sharp thorns break through your flesh. Your unarmed attacks deal SB -2 damage. As a full '
                      'action, you can throw one at an opponent within 10 yards, dealing a Damage 1 hit.', 'TOC', '52'],
    '152': ['Trails of Slime', 'Your body mutates into an aberration similar to a slug. -1d10 to all your'
                               ' Characteristics, and your Mov. Is halved. ', 'TOC', '52'],
    '153': ['Trance', 'When confronted with a tough situation, you slip into a weird trance. When you have to make a '
                      'Fear or Terror test, you move 1d10 yards in a random direction. You may act normally on your'
                      ' next turn.', 'TOC', '52'],
    '154': ['Transparent Skin', 'Your skin becomes translucent, revealing your bones and the organs underneath.', 'TOC',
            '52'],
    '155': ['Trunk', 'Your nose grows and elongates until it turns into a trunk like that of an elephant. It works as a'
                     ' third arm.', 'TOC', '52'],
    '156': ['Turnskin', 'You turn into a beastman. Gain the Animalistic Legs and Bestial Appearance mutations. See'
                        ' manual.', 'TOC', '52'],
    '157': ['Unbelievable Tumour', 'An unnaturally huge tumour grows in your body, weighing 1d10 *10 pounds. For every'
                                   ' 20 pounds, you lose 1 Mov. For every 50 pounds, you lose 1d10 Fel.', 'TOC', '53'],
    '158': ['Uncanny Resemblance', 'In an uncanny twist of fate, your facial features transform to resemble an'
                                   ' important person as determined by the GM.', 'TOC', '53'],
    '159': ['Uncontrollable Flatulence', 'When attacked or when you have to make a Fear or Terror test, you release'
                                         ' gases. See manual.', 'TOC', '53'],
    '160': ['Unnatural Appetite', 'You gain nourishment and sustenance from only one source.', 'TOC', '53'],
    '161': ['Upside-Down', "Your arms and legs switch places. -20 WS and BS for the first 1d10/5 weeks. Afterwards, "
                           "they recover. You may only use two-handed weapons if you're seated.", 'TOC', '53'],
    '162': ['Vampire', 'You must drink blood to survive. Every day you go without drinking fresh blood, you suffer a'
                       ' -10 in all your characteristics.', 'TOC', '53'],
    '163': ['Vestigial/Parasitic Twin', "You become two separate identities fused into one mass of You become two"
                                        " separate identities fused into one mass of flesh and bone. The parentheses"
                                        " indicate the place they're joined at. All characteristics are divided, but"
                                        " they share Skills and Talents. Each twin acts independently. -2 Mov., "
                                        "+20 to Perception Tests.", 'TOC', '54'],
    '164': ['Vile', 'You are repellent. You unconsciously act in ways that repels others, doing exactly the right thing'
                    ' to make them hate you. -3d10 Fel, +20 to Intimidate and Torture tests.', 'TOC', '54'],
    '165': ['Walking Head', 'Your body atrophies and withers away to nothing, and your head expands to take its place.'
                            ' All Body hits are now considered to have hit the head.', 'TOC', '54'],
    '166': ['Warp Frenzy', 'You are dangerously unstable. When you take damage or must make a Fear or Terror test, you '
                           'enter an unnatural frenzy. Gain (1d10+2)/3 temporary mutations. If there are no targets,'
                           ' or you pass a -10 WP test when your opponents are dead, you snap out of the frenzy.',
            'TOC', '54'],
    '167': ['Warped Mind', 'Your mind becomes twisted and vile, prone to strange ruminations. -2d10 Int.', 'TOC', '54'],
    '168': ['Warty Skin', 'Every inch of your body is covered in large, quivering warts. Gain 1 AP in all locations.',
            'TOC', '54'],
    '169': ['Weapon Master', 'You gain a deeper understanding of killing. Choose WS or BS. Gain +1d10 in it.', 'TOC',
            '54'],
    '170': ['Were', 'Gain the Frenzy talent. When you enter a frenzy, you transform into a beast-human hybrid. See'
                    ' manual.', 'TOC', '54'],
    '171': ['Wings', 'You grow a pair of wings, giving bonuses according to their size. See manual.', 'TOC', '55'],
    '172': ['Zoological Mutation', 'One or more parts of your body change into the corresponding parts of some animal.'
                                   ' No further effect.', 'TOC', '56'],
    '173': ['Minor Cosmetic Change', 'You undergo a mild transformation, some slight change that seems innocuous enough'
                                     ' on the surface of things, but shows the favour of the Chaos gods.', 'TOC', '56'],
    '174': ['Custom Mutation', 'Invent your own mutation.', 'TOC', '29']


}


# this function picks a random object
# from the list, then takes the information from
# the corresponding dictionary
# entry.


def pick_mutation(list_of_mutations):
    
    final_mutation_list = []
    for item in list_of_mutations:
        item = str(item)
        chosen_object = mutation_dict[item]
        object_id = item
        name = chosen_object[0]
        description = chosen_object[1]
        source = chosen_object[2]
        page = chosen_object[3]
        if object_id == '3':
            name += ' ('
            random_additional_eye_body_part = random.randint(1, 100)
            random_additional_eye_specific_body_part = random.randint(1, 100)
            if random_additional_eye_body_part <= 15:
                if random_additional_eye_specific_body_part <= 15:
                    name += 'Cheek'
                elif random_additional_eye_specific_body_part <= 45:
                    name += 'Forehead'
                elif random_additional_eye_specific_body_part <= 57:
                    name += 'Chin'
                elif random_additional_eye_specific_body_part <= 68:
                    name += 'Nose'
                elif random_additional_eye_specific_body_part <= 79:
                    name += 'Tongue'
                elif random_additional_eye_specific_body_part <= 90:
                    name += 'Scalp'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Neck'

            elif random_additional_eye_body_part <= 35:
                if random_additional_eye_specific_body_part <= 20:
                    name += 'Right Shoulder'
                elif random_additional_eye_specific_body_part <= 40:
                    name += 'Right Forearm'
                elif random_additional_eye_specific_body_part <= 60:
                    name += 'Palm of the Right Hand'
                elif random_additional_eye_specific_body_part <= 80:
                    name += 'Back of the Right Hand'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Finger on the Right Hand'

            elif random_additional_eye_body_part <= 55:
                if random_additional_eye_specific_body_part <= 20:
                    name += 'Left Shoulder'
                elif random_additional_eye_specific_body_part <= 40:
                    name += 'Left Forearm'
                elif random_additional_eye_specific_body_part <= 60:
                    name += 'Palm of the Left Hand'
                elif random_additional_eye_specific_body_part <= 80:
                    name += 'Back of the Left Hand'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Finger on the Left Hand'

            elif random_additional_eye_body_part <= 80:
                if random_additional_eye_specific_body_part <= 20:
                    name += 'Chest'
                elif random_additional_eye_specific_body_part <= 40:
                    name += 'Navel'
                elif random_additional_eye_specific_body_part <= 60:
                    name += 'Abdomen'
                elif random_additional_eye_specific_body_part <= 80:
                    name += 'Back'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Posterior'
            elif random_additional_eye_body_part <= 90:
                if random_additional_eye_specific_body_part <= 20:
                    name += 'Right Thigh'
                elif random_additional_eye_specific_body_part <= 40:
                    name += 'Right Knee'
                elif random_additional_eye_specific_body_part <= 60:
                    name += 'Calf on Right Leg'
                elif random_additional_eye_specific_body_part <= 80:
                    name += 'Right Foot'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Toe of Right Foot'
            elif random_additional_eye_body_part <= 100:
                if random_additional_eye_specific_body_part <= 20:
                    name += 'Left Thigh'
                elif random_additional_eye_specific_body_part <= 40:
                    name += 'Left Knee'
                elif random_additional_eye_specific_body_part <= 60:
                    name += 'Calf on Left Leg'
                elif random_additional_eye_specific_body_part <= 80:
                    name += 'Left Foot'
                elif random_additional_eye_specific_body_part <= 100:
                    name += 'Toe of Left Foot'
            name += ')'
        elif object_id == '8':
            name += ' ('
            atrophy_roll = random.randint(1, 100)
            if atrophy_roll <= 20:
                name += 'Head'
            elif atrophy_roll <= 40:
                name += 'Right Arm'
            elif atrophy_roll <= 60:
                name += 'Left Arm'
            elif atrophy_roll <= 80:
                name += 'Right Leg'
            elif atrophy_roll <= 100:
                name += 'Left Leg'
            name += ')'
        elif object_id == '10':
            name += ' '
            beast_with_thousand_roll = random.randint(1, 100)
            if beast_with_thousand_roll <= 10:
                name += 'Eyes'
            elif beast_with_thousand_roll <= 20:
                name += 'Noses'
            elif beast_with_thousand_roll <= 30:
                name += 'Ears'
            elif beast_with_thousand_roll <= 40:
                name += 'Sores'
            elif beast_with_thousand_roll <= 50:
                name += 'Tongues'
            elif beast_with_thousand_roll <= 60:
                name += 'Nipples'
            elif beast_with_thousand_roll <= 65:
                name += 'Arms'
            elif beast_with_thousand_roll <= 70:
                name += 'Legs'
            elif beast_with_thousand_roll <= 75:
                name += 'Hands'
            elif beast_with_thousand_roll <= 80:
                name += 'Feet'
            elif beast_with_thousand_roll <= 85:
                name += 'Fingers'
            elif beast_with_thousand_roll <= 90:
                name += 'Toes'
            elif beast_with_thousand_roll <= 99:
                name += 'Orifices'
            elif beast_with_thousand_roll <= 100:
                name += 'Faces'
        elif object_id == '11':
            name += ' ('
            bestial_appearance_roll = random.randint(1, 100)
            if bestial_appearance_roll <= 5:
                name += 'Ant'
            elif bestial_appearance_roll <= 10:
                name += 'Ape'
            elif bestial_appearance_roll <= 15:
                name += 'Bat'
            elif bestial_appearance_roll <= 20:
                name += 'Bear'
            elif bestial_appearance_roll <= 25:
                name += 'Boar'
            elif bestial_appearance_roll <= 30:
                name += 'Bull'
            elif bestial_appearance_roll <= 35:
                name += 'Cat'
            elif bestial_appearance_roll <= 37:
                name += 'Dog'
            elif bestial_appearance_roll <= 40:
                name += 'Wolf'
            elif bestial_appearance_roll <= 43:
                name += 'Eagle'
            elif bestial_appearance_roll <= 45:
                name += 'Falcon'
            elif bestial_appearance_roll <= 50:
                name += 'Goat'
            elif bestial_appearance_roll <= 55:
                name += 'Horse'
            elif bestial_appearance_roll <= 57:
                name += 'Lion'
            elif bestial_appearance_roll <= 60:
                name += 'Tiger'
            elif bestial_appearance_roll <= 65:
                name += 'Rabbit'
            elif bestial_appearance_roll <= 70:
                name += 'Ram'
            elif bestial_appearance_roll <= 75:
                name += 'Rat'
            elif bestial_appearance_roll <= 80:
                name += 'Raven'
            elif bestial_appearance_roll <= 85:
                name += 'Snake'
            elif bestial_appearance_roll <= 90:
                name += 'Spider'
            elif bestial_appearance_roll <= 95:
                name += 'Stag'
            elif bestial_appearance_roll <= 100:
                name += 'Weasel'
            name += ')'
        elif object_id == '14':
            name += ' ('
            bizarre_coloration_color_roll = random.randint(1, 100)
            bizarre_coloration_location_roll = random.randint(1, 70)
            if bizarre_coloration_color_roll <= 10:
                name += 'White'
            elif bizarre_coloration_color_roll <= 20:
                name += 'Brown'
            elif bizarre_coloration_color_roll <= 30:
                name += 'Red'
            elif bizarre_coloration_color_roll <= 40:
                name += 'Yellow'
            elif bizarre_coloration_color_roll <= 50:
                name += 'Blue'
            elif bizarre_coloration_color_roll <= 60:
                name += 'Green'
            elif bizarre_coloration_color_roll <= 70:
                name += 'Orange'
            elif bizarre_coloration_color_roll <= 80:
                name += 'Purple'
            elif bizarre_coloration_color_roll <= 90:
                name += 'Grey'
            elif bizarre_coloration_color_roll <= 100:
                name += 'Black'
            name += ' '
            if bizarre_coloration_location_roll <= 10:
                name += 'Head'
            elif bizarre_coloration_location_roll <= 20:
                name += 'Torso'
            elif bizarre_coloration_location_roll <= 30:
                name += 'Left Arm'
            elif bizarre_coloration_location_roll <= 40:
                name += 'Right Arm'
            elif bizarre_coloration_location_roll <= 50:
                name += 'Right Leg'
            elif bizarre_coloration_location_roll <= 60:
                name += 'Left Leg'
            elif bizarre_coloration_location_roll <= 70:
                name += 'from head to toe'
            name += ')'
        elif object_id == '16':
            name += ' ('
            blood_substitution_roll = random.randint(1, 100)
            if blood_substitution_roll <= 5:
                name += 'Acid'
            elif blood_substitution_roll <= 7:
                name += 'Centipedes'
            elif blood_substitution_roll <= 9:
                name += 'Ants'
            elif blood_substitution_roll <= 10:
                name += 'Beetles'
            elif blood_substitution_roll <= 15:
                name += 'Electricity'
            elif blood_substitution_roll <= 20:
                name += 'Excrement'
            elif blood_substitution_roll <= 25:
                name += 'Eyeballs'
            elif blood_substitution_roll <= 30:
                name += 'Fire'
            elif blood_substitution_roll <= 35:
                name += 'Glue'
            elif blood_substitution_roll <= 37:
                name += 'Leeches'
            elif blood_substitution_roll <= 39:
                name += 'Maggots'
            elif blood_substitution_roll <= 40:
                name += 'Worms'
            elif blood_substitution_roll <= 45:
                name += 'Mice'
            elif blood_substitution_roll <= 50:
                name += 'Molten Metal'
            elif blood_substitution_roll <= 55:
                name += 'Mucous'
            elif blood_substitution_roll <= 60:
                name += 'Mud'
            elif blood_substitution_roll <= 65:
                name += 'Protoplasm'
            elif blood_substitution_roll <= 70:
                name += 'Poison'
            elif blood_substitution_roll <= 75:
                name += 'Small Birds'
            elif blood_substitution_roll <= 80:
                name += 'Tar'
            elif blood_substitution_roll <= 85:
                name += 'Vines'
            elif blood_substitution_roll <= 90:
                name += 'Vomit'
            elif blood_substitution_roll <= 95:
                name += 'Wax'
            elif blood_substitution_roll <= 100:
                name += 'Wind'
            name += ')'
        elif object_id == '20':
            name += ' ('
            brightly_patterned_skin_roll = random.randint(1, 93)
            if brightly_patterned_skin_roll <= 10:
                name += 'Single-coloured spots'
            elif brightly_patterned_skin_roll <= 20:
                name += 'Multi-coloured polka dots'
            elif brightly_patterned_skin_roll <= 30:
                name += 'Single or multi-coloured squares'
            elif brightly_patterned_skin_roll <= 40:
                name += 'Dark, Zebra-like stripes'
            elif brightly_patterned_skin_roll <= 50:
                name += 'Multiple, different-coloured diamonds'
            elif brightly_patterned_skin_roll <= 60:
                name += 'Zigzag stripes'
            elif brightly_patterned_skin_roll <= 70:
                name += 'Tiger stripes'
            elif brightly_patterned_skin_roll <= 80:
                name += 'Camouflage Pattern (no bonus to Concealment)'
            elif brightly_patterned_skin_roll <= 90:
                name += 'Body divided in two equal halves, each of a different colour'
            elif brightly_patterned_skin_roll <= 93:
                name += 'Underside or front of the body in one colour, with the back in a contrasting shade'
            name += ')'
        elif object_id == '22':
            name += ' ('
            centauroid_roll = random.randint(1, 95)
            if centauroid_roll <= 5:
                name += 'Ant'
            elif centauroid_roll <= 10:
                name += 'Ass'
            elif centauroid_roll <= 15:
                name += 'Bear'
            elif centauroid_roll <= 20:
                name += 'Beetle'
            elif centauroid_roll <= 25:
                name += 'Boar'
            elif centauroid_roll <= 30:
                name += 'Centipede'
            elif centauroid_roll <= 35:
                name += 'Cow'
            elif centauroid_roll <= 40:
                name += 'Crocodile'
            elif centauroid_roll <= 45:
                name += 'Elephant'
            elif centauroid_roll <= 50:
                name += 'Frog'
            elif centauroid_roll <= 55:
                name += 'Giraffe'
            elif centauroid_roll <= 60:
                name += 'Horse'
            elif centauroid_roll <= 65:
                name += 'Lion'
            elif centauroid_roll <= 70:
                name += 'Lizard'
            elif centauroid_roll <= 75:
                name += 'Rabbit'
            elif centauroid_roll <= 80:
                name += 'Rat'
            elif centauroid_roll <= 85:
                name += 'Snake'
            elif centauroid_roll <= 90:
                name += 'Spider'
            elif centauroid_roll <= 95:
                name += 'Wolf'
            elif centauroid_roll <= 100:
                name += ''
        elif object_id == '31':
            name += ' ('
            crossbreed_roll = random.randint(1, 100)
            crossbreed_creature_roll = random.randint(1, 100)
            if crossbreed_roll == 100:
                name += 'Chaos Spawn'
            else:
                if crossbreed_creature_roll <= 5:
                    name += 'Goblin'
                elif crossbreed_creature_roll <= 10:
                    name += 'Daemon'
                elif crossbreed_creature_roll <= 20:
                    name += 'Orc'
                elif crossbreed_creature_roll <= 25:
                    name += 'Snotling'
                elif crossbreed_creature_roll <= 27:
                    name += 'Elemental'
                elif crossbreed_creature_roll <= 30:
                    name += 'Ogre Rat'
                elif crossbreed_creature_roll <= 35:
                    name += 'Undead'
                elif crossbreed_creature_roll <= 45:
                    name += 'Minotaur'
                elif crossbreed_creature_roll <= 50:
                    name += 'Dragon'
                elif crossbreed_creature_roll <= 55:
                    name += 'Halfling'
                elif crossbreed_creature_roll <= 60:
                    name += 'Dwarf'
                elif crossbreed_creature_roll <= 65:
                    name += 'Elf'
                elif crossbreed_creature_roll <= 70:
                    name += 'Fimir'
                elif crossbreed_creature_roll <= 75:
                    name += 'Giant Animal'
                elif crossbreed_creature_roll <= 80:
                    name += 'Skaven'
                elif crossbreed_creature_roll <= 85:
                    name += 'Giant'
                elif crossbreed_creature_roll <= 90:
                    name += 'Troll'
                elif crossbreed_creature_roll <= 95:
                    name += 'Ogre'
                elif crossbreed_creature_roll <= 100:
                    name += 'Vampire'
                name += ', '
                if crossbreed_roll <= 33:
                    name += 'Mutant Dominant'
                elif crossbreed_roll <= 66:
                    name += 'Compromise'
                elif crossbreed_roll <= 99:
                    name += 'Creature Dominant'
            name += ')'
        elif object_id == '32':
            name += ' ('
            crown_of_flesh_roll = random.randint(1, 10)
            if crown_of_flesh_roll <= 1:
                name += 'Ears'
            elif crown_of_flesh_roll <= 2:
                name += 'Fingers'
            elif crown_of_flesh_roll <= 3:
                name += 'Noses'
            elif crown_of_flesh_roll <= 4:
                name += 'Tongues'
            elif crown_of_flesh_roll <= 5:
                name += 'Eyes'
            elif crown_of_flesh_roll <= 6:
                name += 'Toes'
            elif crown_of_flesh_roll <= 7:
                name += 'Thumbs'
            elif crown_of_flesh_roll <= 8:
                name += 'Boils'
            elif crown_of_flesh_roll <= 9:
                name += 'Tiny Arms'
            elif crown_of_flesh_roll <= 10:
                name += 'Tentacles'
            name += ')'
        elif object_id == '44':
            name += ' ('
            extra_joints_roll = random.randint(1, 100)
            if extra_joints_roll <= 40:
                name += 'Arms'
            elif extra_joints_roll <= 80:
                name += 'Legs'
            elif extra_joints_roll <= 100:
                name += 'Arms and Legs'
            name += ')'
        elif object_id == '45':
            name += ' ('
            extra_fingers_or_toes_roll = random.randint(1, 100)
            if extra_fingers_or_toes_roll <= 20:
                name += 'Left Hand'
            elif extra_fingers_or_toes_roll <= 40:
                name += 'Right Hand'
            elif extra_fingers_or_toes_roll <= 45:
                name += 'Both Hands'
            elif extra_fingers_or_toes_roll <= 65:
                name += 'Left Foot'
            elif extra_fingers_or_toes_roll <= 85:
                name += 'Right Foot'
            elif extra_fingers_or_toes_roll <= 90:
                name += 'Both Feet'
            elif extra_fingers_or_toes_roll <= 95:
                name += 'One hand, one foot'
            elif extra_fingers_or_toes_roll <= 100:
                name += 'Both hands and feet'
            name += ')'
        elif object_id == '48':
            name += ' (Extra '
            extra_limb_limb_roll = random.randint(1, 80)
            extra_limb_location_roll = random.randint(1, 100)
            if extra_limb_limb_roll <= 10:
                name += 'Left Arm'
            elif extra_limb_limb_roll <= 20:
                name += 'Right Arm'
            elif extra_limb_limb_roll <= 30:
                name += 'Left Leg'
            elif extra_limb_limb_roll <= 40:
                name += 'Right Leg'
            elif extra_limb_limb_roll <= 50:
                name += 'Left Hand'
            elif extra_limb_limb_roll <= 60:
                name += 'Right Hand'
            elif extra_limb_limb_roll <= 70:
                name += 'Left Foot'
            elif extra_limb_limb_roll <= 80:
                name += 'Right Foot'
            name += ' on '
            if extra_limb_location_roll <= 10:
                name += 'Head'
            elif extra_limb_location_roll <= 20:
                name += 'Chest'
            elif extra_limb_location_roll <= 30:
                name += 'Back'
            elif extra_limb_location_roll <= 40:
                name += 'Stomach'
            elif extra_limb_location_roll <= 50:
                name += 'Hip'
            elif extra_limb_location_roll <= 60:
                name += 'Groin'
            elif extra_limb_location_roll <= 65:
                name += 'Left Elbow'
            elif extra_limb_location_roll <= 70:
                name += 'Right Elbow'
            elif extra_limb_location_roll <= 75:
                name += 'Left Knee'
            elif extra_limb_location_roll <= 80:
                name += 'Right Knee'
            elif extra_limb_location_roll <= 85:
                name += 'Left Hand'
            elif extra_limb_location_roll <= 90:
                name += 'Right Hand'
            elif extra_limb_location_roll <= 95:
                name += 'Left Foot'
            elif extra_limb_location_roll <= 100:
                name += 'Right Foot'
            name += ')'
        elif object_id == '77':
            name += ' ('
            iron_hard_skin_roll = random.randint(1, 10)
            if iron_hard_skin_roll <= 1:
                name += 'Head'
            elif iron_hard_skin_roll <= 3:
                name += 'Left Arm'
            elif iron_hard_skin_roll <= 5:
                name += 'Right Arm'
            elif iron_hard_skin_roll <= 6:
                name += 'Body'
            elif iron_hard_skin_roll <= 8:
                name += 'Left Leg'
            elif iron_hard_skin_roll <= 10:
                name += 'Right Leg'
            name += ')'
        elif object_id == '78':
            name += ' ('
            irrational_fear_roll = random.randint(1, 100)
            if irrational_fear_roll <= 4:
                name += "GM's choice (for example pies, meatbread, ham, critics)"
            elif irrational_fear_roll <= 8:
                name += 'Humans'
            elif irrational_fear_roll <= 12:
                name += 'Elves'
            elif irrational_fear_roll <= 16:
                name += 'Dwarfs'
            elif irrational_fear_roll <= 20:
                name += 'Anything larger than yourself'
            elif irrational_fear_roll <= 24:
                name += 'Halflings'
            elif irrational_fear_roll <= 28:
                name += 'Wizards'
            elif irrational_fear_roll <= 32:
                name += 'Goblins'
            elif irrational_fear_roll <= 36:
                name += 'Orcs'
            elif irrational_fear_roll <= 40:
                name += 'Winged Creatures'
            elif irrational_fear_roll <= 44:
                name += 'Other Mutants'
            elif irrational_fear_roll <= 48:
                name += 'Items and creatures of a particular colour'
            elif irrational_fear_roll <= 52:
                name += 'Loud noise'
            elif irrational_fear_roll <= 56:
                name += 'Reptiles'
            elif irrational_fear_roll <= 60:
                name += 'Insects'
            elif irrational_fear_roll <= 64:
                name += 'Odd smells'
            elif irrational_fear_roll <= 68:
                name += 'Women'
            elif irrational_fear_roll <= 72:
                name += 'Men'
            elif irrational_fear_roll <= 76:
                name += 'Children'
            elif irrational_fear_roll <= 80:
                name += 'Ham'
            elif irrational_fear_roll <= 84:
                name += 'Blood'
            elif irrational_fear_roll <= 88:
                name += 'Vomit'
            elif irrational_fear_roll <= 92:
                name += 'Salt Water'
            elif irrational_fear_roll <= 96:
                name += 'Rodents'
            elif irrational_fear_roll <= 100:
                name += 'Religious paraphernalia'
            name += ')'
        elif object_id == '79':
            name += ' ('
            irrational_hatred_roll = random.randint(1, 100)
            if irrational_hatred_roll <= 4:
                name += "GM's choice (for example pies, meatbread, ham, critics"
            elif irrational_hatred_roll <= 8:
                name += 'Humans'
            elif irrational_hatred_roll <= 12:
                name += 'Elves'
            elif irrational_hatred_roll <= 16:
                name += 'Dwarfs'
            elif irrational_hatred_roll <= 20:
                name += 'Anything larger than yourself'
            elif irrational_hatred_roll <= 24:
                name += 'Halflings'
            elif irrational_hatred_roll <= 28:
                name += 'Wizards'
            elif irrational_hatred_roll <= 32:
                name += 'Goblins'
            elif irrational_hatred_roll <= 36:
                name += 'Orcs'
            elif irrational_hatred_roll <= 40:
                name += 'Winged Creatures'
            elif irrational_hatred_roll <= 44:
                name += 'Other Mutants'
            elif irrational_hatred_roll <= 48:
                name += 'Items and creatures of a particular colour'
            elif irrational_hatred_roll <= 52:
                name += 'Loud noise'
            elif irrational_hatred_roll <= 56:
                name += 'Reptiles'
            elif irrational_hatred_roll <= 60:
                name += 'Insects'
            elif irrational_hatred_roll <= 64:
                name += 'Odd smells'
            elif irrational_hatred_roll <= 68:
                name += 'Women'
            elif irrational_hatred_roll <= 72:
                name += 'Men'
            elif irrational_hatred_roll <= 76:
                name += 'Children'
            elif irrational_hatred_roll <= 80:
                name += 'Ham'
            elif irrational_hatred_roll <= 84:
                name += 'Blood'
            elif irrational_hatred_roll <= 88:
                name += 'Vomit'
            elif irrational_hatred_roll <= 92:
                name += 'Salt Water'
            elif irrational_hatred_roll <= 96:
                name += 'Rodents'
            elif irrational_hatred_roll <= 100:
                name += 'Religious paraphernalia'
            name += ')'
        elif object_id == '83':
            name += ' ('
            limb_loss_roll = random.randint(1, 100)
            if limb_loss_roll <= 10:
                name += 'Left Hand'
            elif limb_loss_roll <= 20:
                name += 'Right Hand'
            elif limb_loss_roll <= 30:
                name += 'Left Arm and Hand'
            elif limb_loss_roll <= 40:
                name += 'Right Arm and Hand'
            elif limb_loss_roll <= 50:
                name += 'Left Foot'
            elif limb_loss_roll <= 60:
                name += 'Right Foot'
            elif limb_loss_roll <= 70:
                name += 'Left Leg and Foot'
            elif limb_loss_roll <= 80:
                name += 'Right Leg and Foot'
            elif limb_loss_roll <= 90:
                name += 'Both Arms and Hands'
            elif limb_loss_roll <= 100:
                name += 'Both Legs and Feet'
            name += ')'
        elif object_id == '84':
            name += ' ('
            amount_of_transfers = random.randint(1, 5)
            transfers = 0
            while transfers < amount_of_transfers:
                limb_transference_new_location_roll = random.randint(1, 100)
                limb_transference_body_part_roll = random.randint(1, 90)
                if limb_transference_body_part_roll <= 5:
                    name += 'Head goes'
                elif limb_transference_body_part_roll <= 10:
                    name += 'Eyes go'
                elif limb_transference_body_part_roll <= 15:
                    name += 'Nose goes'
                elif limb_transference_body_part_roll <= 20:
                    name += 'Mouth goes'
                elif limb_transference_body_part_roll <= 25:
                    name += 'Ears go'
                elif limb_transference_body_part_roll <= 30:
                    name += 'Right Hand goes'
                elif limb_transference_body_part_roll <= 35:
                    name += 'Left Hand goes'
                elif limb_transference_body_part_roll <= 45:
                    name += 'Right Arm goes'
                elif limb_transference_body_part_roll <= 55:
                    name += 'Left Arm goes'
                elif limb_transference_body_part_roll <= 60:
                    name += 'Right Foot goes'
                elif limb_transference_body_part_roll <= 65:
                    name += 'Left Foot goes'
                elif limb_transference_body_part_roll <= 75:
                    name += 'Right Leg goes'
                elif limb_transference_body_part_roll <= 85:
                    name += 'Left Leg goes'
                elif limb_transference_body_part_roll <= 89:
                    name += 'Internal Organ goes'
                elif limb_transference_body_part_roll <= 90:
                    name += "GM's Choice goes"
                name += ' into the '
                if limb_transference_new_location_roll <= 10:
                    name += 'Head'
                elif limb_transference_new_location_roll <= 20:
                    name += 'Chest'
                elif limb_transference_new_location_roll <= 30:
                    name += 'Back'
                elif limb_transference_new_location_roll <= 40:
                    name += 'Stomach'
                elif limb_transference_new_location_roll <= 50:
                    name += 'Hip'
                elif limb_transference_new_location_roll <= 60:
                    name += 'Groin'
                elif limb_transference_new_location_roll <= 65:
                    name += 'Right Elbow'
                elif limb_transference_new_location_roll <= 70:
                    name += 'Left Elbow'
                elif limb_transference_new_location_roll <= 75:
                    name += 'Right Knee'
                elif limb_transference_new_location_roll <= 80:
                    name += 'Left Knee'
                elif limb_transference_new_location_roll <= 85:
                    name += 'Right Hand'
                elif limb_transference_new_location_roll <= 90:
                    name += 'Left Hand'
                elif limb_transference_new_location_roll <= 95:
                    name += 'Right Foot'
                elif limb_transference_new_location_roll <= 100:
                    name += 'Left Foot'
                name += ', '
                transfers += 1
            name = name[:-2]
            name += ')'
        elif object_id == '97':
            name += ' ('
            full_transformation_roll = random.randint(1, 10)
            second_transformation_roll = random.randint(1, 100)
            if full_transformation_roll <= 6:
                name += 'Full. -30 Move Silently Tests, '
                if second_transformation_roll <= 40:
                    name += 'mechanical legs, +1 Mov.'
                elif second_transformation_roll <= 60:
                    name += 'wheels instead of legs, +3 Mov.'
                elif second_transformation_roll <= 80:
                    hovering_movement = random.randint(1, 10)
                    name += ' Chaos engine legs, gain Hoverer at ' + str(hovering_movement) + ' Mov.'
                elif second_transformation_roll <= 100:
                    track_movement = random.randint(1, 10)
                    name += 'tracks instead of legs, Mov. ' + str(track_movement)
            elif full_transformation_roll <= 10:
                extra_parts = random.randint(1, 4)
                name += 'Partial transformation. ' + str(extra_parts) + ' mechanical parts. See manual'
        elif object_id == '111':
            name += ' ('
            plague_bearer_roll = random.randint(1, 100)
            if plague_bearer_roll <= 16:
                name += 'The Shakes'
            elif plague_bearer_roll <= 32:
                name += 'Eye Rot'
            elif plague_bearer_roll <= 48:
                name += 'Creeping Buboes'
            elif plague_bearer_roll <= 64:
                name += 'Bone Ague'
            elif plague_bearer_roll <= 80:
                name += 'Grey Fever'
            elif plague_bearer_roll <= 96:
                name += 'Green Pox'
            elif plague_bearer_roll <= 100:
                plague_bearer_disease_list = ['Bloody Flux', 'Galloping Trots', 'Green Pox', 'Kruts', 'Neiglish Rot',
                                              'Scurvy Madness', 'Stenchfoot Fever', 'Weevil Cough']
                name += random.choice(plague_bearer_disease_list)+' (see CORE 2 p. 136- 137)'
            name += ')'
        elif object_id == '122':
            name += ' ('
            rearranged_face_roll = random.randint(1, 10)
            if rearranged_face_roll <= 1:
                name += 'Top of the head'
            elif rearranged_face_roll <= 4:
                front_of_the_head_roll = random.randint(1, 10)
                if front_of_the_head_roll <= 3:
                    name += 'Upper part, front of the head'
                elif front_of_the_head_roll <= 6:
                    name += 'Lower part, front of the head'
                elif front_of_the_head_roll <= 9:
                    name += 'Middle part, front of the head'
                elif front_of_the_head_roll <= 10:
                    name += 'Your face rearranges itself back into normal position'
            elif rearranged_face_roll <= 5:
                name += 'Back of the head'
            elif rearranged_face_roll <= 7:
                name += 'Left side of the head'
            elif rearranged_face_roll <= 9:
                name += 'Right side of the head'
            elif rearranged_face_roll <= 10:
                name += 'Neck'
            name += ')'
        elif object_id == '129':
            name += ' ('
            sensory_loss_roll = random.randint(1, 100)
            if sensory_loss_roll <= 20:
                name += 'Hear'
            elif sensory_loss_roll <= 40:
                name += 'See'
            elif sensory_loss_roll <= 60:
                name += 'Smell'
            elif sensory_loss_roll <= 80:
                name += 'Taste'
            elif sensory_loss_roll <= 100:
                name += 'Touch'
            name += ')'
        elif object_id == '139':
            name += ' ('
            strange_voice_roll = random.randint(1, 100)
            if strange_voice_roll <= 10:
                name += 'Belching'
            elif strange_voice_roll <= 20:
                name += 'Growling'
            elif strange_voice_roll <= 30:
                name += 'Hoarse'
            elif strange_voice_roll <= 40:
                name += 'Honking'
            elif strange_voice_roll <= 50:
                name += 'Lilting'
            elif strange_voice_roll <= 60:
                name += 'Shrill'
            elif strange_voice_roll <= 70:
                name += 'Squeaking'
            elif strange_voice_roll <= 80:
                name += 'Ululating'
            elif strange_voice_roll <= 90:
                name += 'Whining'
            elif strange_voice_roll <= 100:
                name += 'Whispery'
            name += ')'
        elif object_id == '156':
            name += ' ('
            turnskin_roll = random.randint(1, 100)
            if turnskin_roll <= 30:
                name += 'Bray'
            elif turnskin_roll <= 60:
                name += 'Ungor'
            elif turnskin_roll <= 100:
                name += 'Gor'
            name += ')'
        elif object_id == '159':
            name += ' ('
            uncontrollable_flatulence_roll = random.randint(1, 10)
            if uncontrollable_flatulence_roll <= 2:
                name += 'Poison'
            elif uncontrollable_flatulence_roll <= 4:
                name += 'Paralysing'
            elif uncontrollable_flatulence_roll <= 6:
                name += 'Oily Mist'
            elif uncontrollable_flatulence_roll <= 8:
                name += 'Noxious'
            elif uncontrollable_flatulence_roll <= 10:
                name += 'Stench of Madness'
            name += ')'
        elif object_id == '160':
            name += ' ('
            unnatural_appetite_roll = random.randint(1, 100)
            if unnatural_appetite_roll <= 5:
                name += 'Blood'
            elif unnatural_appetite_roll <= 10:
                name += 'Children'
            elif unnatural_appetite_roll <= 15:
                name += 'Critics'
            elif unnatural_appetite_roll <= 20:
                name += 'Dirt'
            elif unnatural_appetite_roll <= 25:
                name += 'Dung'
            elif unnatural_appetite_roll <= 30:
                name += 'Eyeballs'
            elif unnatural_appetite_roll <= 35:
                name += 'Grass'
            elif unnatural_appetite_roll <= 40:
                name += 'Hair'
            elif unnatural_appetite_roll <= 45:
                name += 'Maggots'
            elif unnatural_appetite_roll <= 50:
                name += 'Nail Clippings'
            elif unnatural_appetite_roll <= 55:
                name += 'Nails'
            elif unnatural_appetite_roll <= 60:
                name += 'Paints'
            elif unnatural_appetite_roll <= 65:
                name += 'Pets'
            elif unnatural_appetite_roll <= 70:
                name += 'Rats'
            elif unnatural_appetite_roll <= 75:
                name += 'Rotting Meat'
            elif unnatural_appetite_roll <= 80:
                name += 'Spiders'
            elif unnatural_appetite_roll <= 85:
                name += 'Tears'
            elif unnatural_appetite_roll <= 90:
                name += 'Teeth'
            elif unnatural_appetite_roll <= 95:
                name += 'Tongues'
            elif unnatural_appetite_roll <= 100:
                name += 'GM Choice'
            name += ')'
        elif object_id == '163':
            name += ' ('
            vestigial_twin_roll = random.randint(1, 100)
            if vestigial_twin_roll <= 20:
                name += 'Head'
            elif vestigial_twin_roll <= 40:
                name += 'Front to Front'
            elif vestigial_twin_roll <= 60:
                name += 'Back to Back'
            elif vestigial_twin_roll <= 80:
                name += 'Left Side'
            elif vestigial_twin_roll <= 100:
                name += 'Right Side'
            name += ')'
        elif object_id == '171':
            name += ' ('
            wings_roll = random.randint(1, 100)
            if wings_roll <= 50:
                name += 'Small'
            elif wings_roll <= 80:
                name += 'Medium'
            elif wings_roll <= 100:
                name += 'Large'
            name += ')'
        elif object_id == '172':
            name += ' ('
            zoological_mutation_part_roll = random.randint(1, 100)
            if zoological_mutation_part_roll <= 4:
                name += 'Head'
            elif zoological_mutation_part_roll <= 8:
                name += 'Torso'
            elif zoological_mutation_part_roll <= 12:
                name += 'Arms'
            elif zoological_mutation_part_roll <= 16:
                name += 'Legs'
            elif zoological_mutation_part_roll <= 20:
                name += 'Head and Torso'
            elif zoological_mutation_part_roll <= 24:
                name += 'Head, Torso and Arms'
            elif zoological_mutation_part_roll <= 28:
                name += 'Head, Torso and Legs'
            elif zoological_mutation_part_roll <= 32:
                name += 'Torso and Arms'
            elif zoological_mutation_part_roll <= 36:
                name += 'Torso and Legs'
            elif zoological_mutation_part_roll <= 40:
                name += 'Arms and Legs'
            elif zoological_mutation_part_roll <= 44:
                name += 'Face'
            elif zoological_mutation_part_roll <= 48:
                name += 'One Leg'
            elif zoological_mutation_part_roll <= 52:
                name += 'One Foot'
            elif zoological_mutation_part_roll <= 56:
                name += 'One Toe'
            elif zoological_mutation_part_roll <= 60:
                name += 'One Arm'
            elif zoological_mutation_part_roll <= 64:
                name += 'One Hand'
            elif zoological_mutation_part_roll <= 68:
                name += 'One Finger'
            elif zoological_mutation_part_roll <= 72:
                name += 'Mouth'
            elif zoological_mutation_part_roll <= 76:
                name += 'One Eye'
            elif zoological_mutation_part_roll <= 80:
                name += 'Eyes'
            elif zoological_mutation_part_roll <= 84:
                name += 'One Ear'
            elif zoological_mutation_part_roll <= 88:
                name += 'Tail'
            elif zoological_mutation_part_roll <= 92:
                name += 'One Hand and One Foot'
            elif zoological_mutation_part_roll <= 96:
                name += 'One Arm and One Leg'
            elif zoological_mutation_part_roll <= 100:
                name += 'Mouth and Eyes'
            name += ' of '
            zoological_mutation_animal_roll = random.randint(1, 100)
            if zoological_mutation_animal_roll <= 3:
                name += 'an Ant'
            elif zoological_mutation_animal_roll <= 6:
                name += 'an Ape'
            elif zoological_mutation_animal_roll <= 9:
                name += 'a Bat'
            elif zoological_mutation_animal_roll <= 12:
                name += 'a Bear'
            elif zoological_mutation_animal_roll <= 15:
                name += 'a Beetle'
            elif zoological_mutation_animal_roll <= 18:
                name += 'a Bird'
            elif zoological_mutation_animal_roll <= 21:
                name += 'a Boar'
            elif zoological_mutation_animal_roll <= 24:
                name += 'a Bull'
            elif zoological_mutation_animal_roll <= 27:
                name += 'a Cat'
            elif zoological_mutation_animal_roll <= 30:
                name += 'a Deer'
            elif zoological_mutation_animal_roll <= 33:
                name += 'a Wolf'
            elif zoological_mutation_animal_roll <= 36:
                name += 'a Dragon'
            elif zoological_mutation_animal_roll <= 39:
                name += 'a Duck'
            elif zoological_mutation_animal_roll <= 42:
                name += 'an Eagle'
            elif zoological_mutation_animal_roll <= 45:
                name += 'a Frog'
            elif zoological_mutation_animal_roll <= 48:
                name += 'a Horse'
            elif zoological_mutation_animal_roll <= 51:
                name += 'a Lion'
            elif zoological_mutation_animal_roll <= 54:
                name += 'a Lizard'
            elif zoological_mutation_animal_roll <= 57:
                name += 'an Octopus'
            elif zoological_mutation_animal_roll <= 60:
                name += 'an Owl'
            elif zoological_mutation_animal_roll <= 63:
                name += 'a Rabbit'
            elif zoological_mutation_animal_roll <= 66:
                name += 'a Raven'
            elif zoological_mutation_animal_roll <= 69:
                name += 'a Scorpion'
            elif zoological_mutation_animal_roll <= 72:
                name += 'a Goat'
            elif zoological_mutation_animal_roll <= 75:
                name += 'a Snake'
            elif zoological_mutation_animal_roll <= 78:
                name += 'a Spider'
            elif zoological_mutation_animal_roll <= 81:
                name += 'a Squirrel'
            elif zoological_mutation_animal_roll <= 84:
                name += 'a Tiger'
            elif zoological_mutation_animal_roll <= 87:
                name += 'a Toad'
            elif zoological_mutation_animal_roll <= 90:
                name += 'a Warthog'
            elif zoological_mutation_animal_roll <= 93:
                name += 'a Weasel'
            elif zoological_mutation_animal_roll <= 96:
                name += 'a Rat'
            elif zoological_mutation_animal_roll <= 100:
                name += '(GM Choice)'
            name += ')'

        final_object = [object_id, name, description, source, page]
        final_mutation_list.append(final_object)

    return final_mutation_list


def random_mutation(amount):

    mutation_list = []
    for mutation in range(0, amount):
        extra_mutation_chance_roll = random.randint(1, 1000)
        if extra_mutation_chance_roll <= 985:
            pass
        elif extra_mutation_chance_roll <= 990:
            amount += 1
        elif extra_mutation_chance_roll <= 995:
            amount += 2
    while len(mutation_list) < amount:
        character_mutation = random.choice(random_mutation_list)
        if character_mutation not in mutation_list:
            mutation_list.append(character_mutation)
    final_list = pick_mutation(mutation_list)

    return final_list


def random_mutation_khorne(amount):
    mutation_list = []

    for mutation in range(0, amount):
        random_mutation_chance_roll = random.randint(1, 100)
        if random_mutation_chance_roll <= 92:
            pass
        elif random_mutation_chance_roll <= 100:
            random_list = random_mutation(1)
            if len(random_list) != 1:
                amount += len(random_list)-1
            for item in random_list:
                
                item = str(item[0])
                
                mutation_list.append(item)
        while len(mutation_list) < amount:
            character_mutation = random.choice(khorne_mutation_list)
            if character_mutation not in mutation_list:
                mutation_list.append(character_mutation)
    final_list = pick_mutation(mutation_list)
    
    return final_list


def random_mutation_nurgle(amount):
    mutation_list = []

    for mutation in range(0, amount):
        random_mutation_chance_roll = random.randint(1, 100)
        if random_mutation_chance_roll <= 92:
            pass
        elif random_mutation_chance_roll <= 100:
            random_list = random_mutation(1)
            if len(random_list) != 1:
                amount += len(random_list)-1
            for item in random_list:
                
                item = str(item[0])
                
                mutation_list.append(item)
        while len(mutation_list) < amount:
            character_mutation = random.choice(nurgle_mutation_list)
            if character_mutation not in mutation_list:
                mutation_list.append(character_mutation)
    final_list = pick_mutation(mutation_list)
    
    return final_list


def random_mutation_slaanesh(amount):
    mutation_list = []

    for mutation in range(0, amount):
        random_mutation_chance_roll = random.randint(1, 100)
        if random_mutation_chance_roll <= 92:
            pass
        elif random_mutation_chance_roll <= 100:
            random_list = random_mutation(1)
            if len(random_list) != 1:
                amount += len(random_list)-1
            for item in random_list:
                
                item = str(item[0])
                
                mutation_list.append(item)
        while len(mutation_list) < amount:
            character_mutation = random.choice(slaanesh_mutation_list)
            if character_mutation not in mutation_list:
                mutation_list.append(character_mutation)
    final_list = pick_mutation(mutation_list)
    
    return final_list


def random_mutation_tzeentch(amount):
    mutation_list = []

    for mutation in range(0, amount):
        random_mutation_chance_roll = random.randint(1, 100)
        if random_mutation_chance_roll <= 92:
            pass
        elif random_mutation_chance_roll <= 100:
            random_list = random_mutation(1)
            if len(random_list) != 1:
                amount += len(random_list)-1
            for item in random_list:
                
                item = str(item[0])
                
                mutation_list.append(item)
        while len(mutation_list) < amount:
            character_mutation = random.choice(tzeentch_mutation_list)
            if character_mutation not in mutation_list:
                mutation_list.append(character_mutation)
    final_list = pick_mutation(mutation_list)
    
    return final_list
