import random

petty_magic = [
    'Petty Magic',
    ['Glowing Light', '3'],
    ['Sounds', '4'],
    ['Drop', '4'],
    ['Marsh Lights', '6'],
    ['Magic Dart', '6'],
    ['Sleep', '6'],
    ['Protection From Rain', '3'],
    ['Magic Flame', '3'],
    ['Gust', '4'],
    ['Ghost Step', '4'],
    ['Ill Fortune', '5'],
    ['Shock', '6']

]

petty_magic_chaos = [
    'Petty Magic (Chaos)',
    ['Befuddle', '4'],
    ['Blessing of the Master', '6'],
    ['Burn', '4'],
    ['Curse', '6'],
    ['Eyes of Clarity', '6'],
    ['Spew ', '3']
]

lesser_magic = [
    'Lesser Magic',
    ['Move', '4'],
    ['Aethyric Armour', '5'],
    ['Blessed Weapon', '6'],
    ['Magic Lock', '7'],
    ['Magic Alarm', '8'],
    ['Silence', '10'],
    ['Skywalk', '11'],
    ['Dispel', '13'],
    ['Bind', '10'],
    ['Climb', '7'],
    ['Hand of the God', '13'],
    ['Side-Step', '11'],
    ['Suppress Mutation', '15'],
    ['Tremor', '8'],
]

lore_beasts = [
    'Lore of Beasts',
    [
        ['The Beast Broken', '7'],
        ['The Beast Made Well', '9'],
        ['Calm the Wild Beast', '5'],
        ['Claws of Fury', '8'],
        ["Cruelty's Desserts", '6'],
        ['Form of the Soaring Raven', '7']
    ],

    [
        ["The Boar's Hide", '14'],
        ['Form of the Ravening Wolf', '15'],
        ['Leatherbane', '15'],
        ["Master's Voice", '13'],
        ['The Ox Stands', '11'],
        ['The Talking Beast', '11'],
    ],

    [
        ['The Beast Unleashed', '19'],
        ['Cowering Beasts', '18'],
        ["Crow's Feast", '17'],
        ['Form of the Puissant Steed', '18'],
        ["The Winter's Long Slumber", '16']
    ],

    [
        ['Form of the Raging Bear', '21'],
        ['Repugnant Transformation', '21'],
        ['Wings of the Falcon', '25'],
    ]
]

lore_death = [
    'Lore of Death',
    [
        ["Death's Messenger", '6'],
        ['Deathsight', '5'],
        ["Grief's End", '5'],
        ['Reaping Scythe', '8'],
        ['Swift Passing', '7'],
        ["Tomb Robber's Curse", '10']
    ],

    [
        ['Acceptance of Fate', '14'],
        ["Death's Release", '14'],
        ['Limbwither ', '11'],
        ['Tide of Years', '11'],
        ['Ward Against Abomination', '12']
    ],

    [
        ["Death's Door", '20'],
        ['Final Words', '18'],
        ['The Icy Grip of Death', '16'],
        ['Knock of the Departed ', '18'],
        ['Steal Life', '16']
    ],

    [
        ['The Animus Imprisoned', '29'],
        ["Life's End", '31'],
        ['Wind of Death', '27'],
        ["Youth's Bane", '23']
    ]

]

lore_fire = [
    'Lore of Fire',
    [
        ['Cauterize', '4'],
        ['Choleric', '6'],
        ['Crown of Fire', '8'],
        ["Fires of U'Zhul", '6'],
        ['Flashcook', '4'],
        ['Taste of Fire ', '9']
    ],

    [
        ['Curtain of Flame', '14'],
        ['Fire Ball', '12'],
        ['Flaming Sword of Rhuin', '14'],
        ['Inextinguishable Flame', '11'],
        ['Shield of Aqshy', '12']
    ],

    [
        ['Consuming Wrath', '16'],
        ['Hearts of Fire', '16'],
        ['Ruin and Destruction', '18']
    ],

    [
        ["Aqshy's Aegis", '24'],
        ['Boiling Blood', '21'],
        ['Breathe Fire', '25'],
        ['Burning Vengeance', '26'],
        ['Conflagration of Doom', '31'],
        ['Fiery Blast', '22']
    ]
]

lore_heavens = [
    'Lore of the Heavens',
    [
        ['Birdspeak', '10'],
        ['First Portent of Amul', '6'],
        ['Lens on the Sky', '8'],
        ['Lightning Bolt', '10'],
        ['Omen', '4'],
        ['Polish, Clean, And Gleam', '4']
    ],

    [
        ['Clear Sky', '12'],
        ["Fortune's Renewal", '13'],
        ['Second Portent of Amul', '12'],
        ['Third Portent of Amul', '14'],
        ['Wind Blast', '14']
    ],

    [
        ['Curse', '16'],
        ['Premonition', '16'],
        ['Project Spirit', '18'],
        ['Wings of Heaven', '18'],
    ],

    [
        ['Fate of Doom', '31'],
        ['Finding Divination', '21'],
        ['Lightning Storm', '25'],
        ['Signs in the Stars', '24'],
        ['Starshine', '22']

    ]

]

lore_life = [
    'Lore of Life',
    [
        ['Curse of Thorns', '6'],
        ['Earth Blood', '9'],
        ['Fat of the Land', '8'],
        ['Ferment', '4'],
        ["Track's Tale Told", '7'],
        ["Tree-Dweller's Step", '8']

    ],

    [
        ['Earth Gate', '14'],
        ['Father of Thorns', '14'],
        ['Leaf Fall', '12'],
        ["River's Whisper", '15'],
        ['Summer Heat', '12'],
        ['Vital Growth', '15'],
        ['The Wilds Undisturbed', '11']

    ],

    [
        ['Spring Bloom', '18'],
        ["Trees' Rustle", '18'],
        ['Wood Shape ', '16']

    ],

    [
        ['Cure Blight', '27'],
        ['Flesh of Clay', '24'],
        ['Geyser', '22'],
        ['Winter Frost', '25']

    ]

]

lore_light = [
    'Lore of Light',
    [
        ['Clarity', '7'],
        ['Cleaning Glow', '5'],
        ['Dazzling Brightness', '5'],
        ['Healing of Hysh', '10'],
        ['Radiant Gaze', '7'],
        ['Radiant Weapon', '9'],
        ['Shimmering Cloak', '8']

    ],

    [
        ['Banish', '13'],
        ['Illuminate the Edifice', '11'],
        ['Light of Purity', '12'],
        ['Radiant Sentinel', '14']

    ],

    [
        ['Eyes of Truth', '20'],
        ['Ill-Bane', '16'],
        ['Inspiration', '16'],
        ['The Power of Truth', '18']

    ],

    [
        ['Blinding Light', '24'],
        ['Boon of Hysh', '27'],
        ['Daemonbane', '26'],
        ["Light's Demand", '21'],
        ['Pillar of Radiance', '28']

    ]

]

lore_metal = [
    'Lore of Metal',
    [
        ['Curse of Rust', '9'],
        ['Fault of Form', '6'],
        ['Guard of Steel', '5'],
        ['Inscription', '7'],
        ['Law of Form', '8'],
        ['Law of Logic', '7'],
        ['Stoke the Forge', '4']

    ],

    [
        ['Armour of Lead', '14'],
        ['Law of Age', '15'],
        ['Rigidity of Body and Mind', '12'],
        ['Secret Rune', '14'],
        ['Silver Arrows of Arha', '13'],
        ['Tale of Metal', '11']

    ],

    [
        ["Fool's Gold", '17'],
        ['Transformation of Metal', '18'],
        ['Trial and Error', '16']

    ],

    [
        ['Breach the Unknown', '22'],
        ['Enchant Item', '21'],
        ['Law of Gold', '26'],
        ['Transmutation of the Unstable Mind', '23']
    ]

]

lore_shadow = [
    'Lore of Shadow',
    [
        ['Bewilder', '8'],
        ['Doppelganger', '7'],
        ['Eye of the Beholder', '6'],
        ['Mindhole', '8'],
        ['Mutable Visage', '7'],
        ['Shadowcloak', '5'],
        ['Take No Heed', '9']

    ],

    [
        ['Burning Shadows', '14'],
        ['Cloak Activity', '12'],
        ['Pall of Darkness', '15'],
        ['Shadow of Death', '15'],
        ['Shadowsteed', '11'],
        ['Throttling', '13']

    ],

    [
        ['Mockery of Death', '18'],
        ['Shroud of Invisibility', '17'],

    ],

    [
        ['Dread Aspect', '21'],
        ['Illusion', '24'],
        ['Shadow Knives', '22'],
        ['Substance of Shadow', '22'],
        ['Universal Confusion', '27']
    ]

]

lore_chaos = [
    'Lore of Chaos',
    [
        ['Boon of Chaos', '9'],
        ['Vision of Torment', '7'],

    ],

    [
        ['Burning Blood', '13'],
        ['Summon Lesser Daemon', '12'],

    ],

    [
        ['Dark Hand of Destruction', '17'],
        ['Lure of Chaos', '16'],
        ['Touch of Chaos', '20'],

    ],

    [
        ['Summon Daemon Pack', '25'],
        ['Veil of Corruption', '24'],
        ['Word of Pain', '27'],

    ]

]

lore_nurgle = [
    'Lore of Nurgle',
    [
        ['Foul Messenger', '8'],
        ['Joyous Aspect', '6'],
        ['Stench of Nurgle', '8']

    ],

    [
        ['Reveal the Inner Beauty', '12']

    ],

    [
        ['Miasma of Pestilence', '18'],
        ["Nurgle's Boon", '16'],
        ['Stream of Corruption', '18']

    ],

    [
        ['From One to Many', '26'],
        ['Plague Wind', '29'],
        ['Sumptuous Pestilence', '25']

    ]

]

lore_slaanesh = [
    'Lore of Slaanesh',
    [
        ['Acquiescence ', '6'],
        ['Cutting Wit', '7']

    ],

    [
        ['Breath of Inspiration', '11'],
        ['Mask of Desire', '14']

    ],

    [
        ['From Pain, Pleasure', '16'],
        ['Pavane of Slaanesh', '18']
    ],

    [
        ['Flesh Puppet', '22'],
        ['Fleshy Curse', '25'],
        ['Golden Torrent', '21'],
        ['Succubus', '28']
    ]

]

lore_tzeentch = [
    'Lore of Tzeentch',
    [
        ['Enrage Beast', '6'],
        ['Flames of Fate', '7'],
        ['Mindfire', '10']
    ],

    [
        ['Pink Fire of Tzeentch', '15'],
        ['Subvert Strength', '11']
    ],

    [
        ['Destroy Magic', '20'],
        ['Slave to Chaos', '18'],
        ['Transformation of Tzeentch', '18'],
        ["Tzeentch's Blessing", '18']
    ],

    [
        ["Tzeentch's Fire Storm", '25'],
        ['Dispel Mortal', '30']

    ]

]

lore_nagash = [
    'Lore of Nagash',
    [
        ['Re-Animate', '8'],
        ['Fountains of Blood', '6']
    ],

    [
        ['Gaze of Nagash', '12'],
        ['Hellish Vigour', '15'],
        ['Ride Through the Night', '11']

    ],

    [
        ['Control Undead', '17']
    ],

    [
        ['Spell of Awakening', '24'],
        ['Withering Wave', '21'],
        ['Blight ', '27'],
        ['Raise the Dead', '22']

    ]

]

chaos_magic_list = [
    petty_magic_chaos, lore_tzeentch, lore_slaanesh, lore_nurgle, lore_chaos
]

magic_list = [
    petty_magic, lore_shadow, lore_beasts,
    lore_death, lore_fire, lore_heavens, lore_life, lore_light, lore_metal, lore_nagash, lesser_magic
]


def pick_spell(same_school=0):
    random_list = random.randint(1, 100)
    if random_list <= 90:
        spell_list = random.choice(magic_list)
    elif random_list <= 95:
        spell_list = random.choice(chaos_magic_list)
    elif random_list <= 100:
        spell_list = lore_nagash
    temp_spell_list = spell_list[1:]
    spell_school = spell_list[0]
    if spell_list == petty_magic or spell_list == petty_magic_chaos or spell_list == lesser_magic:
        chosen_spell = random.choice(temp_spell_list)
    else:
        spell_level_roll = random.randint(1, 100)
        if spell_level_roll <= 55:
            spell_level = 1
        elif spell_level_roll <= 85:
            spell_level = 2
        elif spell_level_roll <= 95:
            spell_level = 3
        elif spell_level_roll <= 100:
            spell_level = 4
        chosen_spell = random.choice(temp_spell_list[spell_level-1])
    spell_final = chosen_spell[0] + ' ('+spell_school+')'
    if same_school != 0:
        same_school_spell_list = []
        while len(same_school_spell_list) < same_school:
            if spell_list == petty_magic or spell_list == petty_magic_chaos or spell_list == lesser_magic:
                chosen_spell = random.choice(temp_spell_list)
            else:
                spell_level_roll = random.randint(1, 100)
                if spell_level_roll <= 55:
                    spell_level = 1
                elif spell_level_roll <= 85:
                    spell_level = 2
                elif spell_level_roll <= 95:
                    spell_level = 3
                elif spell_level_roll <= 100:
                    spell_level = 4
                chosen_spell = random.choice(temp_spell_list[spell_level - 1])
            if chosen_spell[0] not in same_school_spell_list:
                same_school_spell_list.append(chosen_spell[0])
            # a grimoire can have up to 8 spells in it, but there are only six
            # petty magic chaos spells. This elif solves the problem by adding two zeroes
            # which complete the necessary length, which are then removed from the list
            elif spell_list == petty_magic_chaos and len(same_school_spell_list) >= 6:
                same_school_spell_list.append(0)
                same_school_spell_list.append(0)
        while 0 in same_school_spell_list:
            same_school_spell_list.remove(0)
        spell_final = spell_school + ' ('
        for item in same_school_spell_list:
            spell_final += item + ', '
        spell_final = spell_final[:-2]
        spell_final += ')'
    return spell_final
