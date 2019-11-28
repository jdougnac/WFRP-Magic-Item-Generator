import random
import amulet
import armour
import arrow
import bag
import boot
import bow
import glove
import grimoire
import horn
import jewel_of_power
import potion
import ring
import robe
import scroll
import special
import spell
import wand
import weapon


def pick_random_object(rune=False, chaos=False, object_type=0):
    if object_type == 0:
        object_roll = random.randint(1, 100)
    else:
        object_roll = object_type
    if object_roll <= 11:
        special_roll = random.randint(1, 100)
        if special_roll <= 70:
            item = special.pick_special()
        elif special_roll <= 80:
            item = horn.pick_horn()
        elif special_roll <= 90:
            item = glove.pick_glove()
        elif special_roll <= 100:
            item = bag.pick_bag()
    elif object_roll <= 19:
        item = amulet.pick_amulet()
    elif object_roll <= 32:
        item = armour.pick_armour()
    elif object_roll <= 37:
        item = arrow.pick_arrow()
    elif object_roll <= 42:
        item = boot.pick_boot()
    elif object_roll <= 48:
        item = bow.pick_bow()
    elif object_roll <= 54:
        item = grimoire.pick_grimoire()
    elif object_roll <= 62:
        item = potion.pick_potion()
    elif object_roll <= 71:
        item = ring.pick_ring()
    elif object_roll <= 74:
        item = robe.pick_robe()
    elif object_roll <= 84:
        item = scroll.pick_scroll()
    elif object_roll <= 86:
        item = wand.pick_wand()
    elif object_roll <= 100:
        item = weapon.pick_weapon()
    return item


def return_items(amount, category=0):
    item_list = []
    for item in range(0, amount):
        object = pick_random_object(object_type=category)
        item_list.append(object)
    return item_list


