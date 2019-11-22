import random
import spell


def pick_grimoire():
    spell_amount = random.randint(1, 4) + random.randint(1, 4)

    name = 'Spell Grimoire: ' + spell.pick_spell(same_school=spell_amount)

    final_object = ['0', name, 'A grimoire containing spells', 'CORE1', '185']
    return final_object

