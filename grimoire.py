import random
import spell
import chaos


def pick_grimoire():
    chaos_grimoire_chance = random.randint(1, 100)
    if chaos_grimoire_chance > 95:
        return chaos.pick_chaos_grimoire()
    spell_amount = random.randint(1, 4) + random.randint(1, 4)

    name = 'Spell Grimoire: ' + spell.pick_spell(same_school=spell_amount)

    final_object = ['0', name, 'A grimoire containing spells', 'CORE1', '185']
    return final_object
