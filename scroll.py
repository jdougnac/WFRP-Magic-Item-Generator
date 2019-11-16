import random
import spell


def pick_scroll():
    extra_spell_chance = random.randint(1, 100)
    if extra_spell_chance <= 95:
        name = 'Scroll: ' + spell.pick_spell()
    elif extra_spell_chance <= 100:
        name = 'Scroll: ' + spell.pick_spell(same_school=random.randint(1, 3)+1)

    final_object = ['0', name, 'A scroll containing one or more spells. They can be cast once by a spellcaster without'
                               ' needing to roll.', 'CORE1', '187']
    return final_object
