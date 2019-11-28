import launcher

from tkinter import *
from tkinter import ttk

window = Tk()

window.geometry("1700x700")
window.title("WFRP Magic Item Generator")
object_text = Text(height=100, width=130, wrap=WORD)

var1 = StringVar()
var1.set(1)
amount_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def insert_text(amount, category):
    object_list = launcher.return_items(amount, category)
    object_text.delete('1.0', END)
    for item in object_list:
        object_text.insert(END, item)
        object_text.insert(END, '\n')


randomObjectButton = ttk.Button(text='Generate Random Object', command=lambda: insert_text(int(var1.get()), 0))
randomSpecialButton = ttk.Button(text='Generate Random Special', command=lambda: insert_text(int(var1.get()), 11))
randomAmuletButton = ttk.Button(text='Generate Random Amulet', command=lambda: insert_text(int(var1.get()), 19))
randomArmourButton = ttk.Button(text='Generate Random Armour', command=lambda: insert_text(int(var1.get()), 32))
randomBootsButton = ttk.Button(text='Generate Random Boots', command=lambda: insert_text(int(var1.get()), 42))
randomBowButton = ttk.Button(text='Generate Random Bow', command=lambda: insert_text(int(var1.get()), 48))
randomGrimoireButton = ttk.Button(text='Generate Random Grimoire', command=lambda: insert_text(int(var1.get()), 54))
randomPotionButton = ttk.Button(text='Generate Random Potion', command=lambda: insert_text(int(var1.get()), 62))
randomRingButton = ttk.Button(text='Generate Random Ring', command=lambda: insert_text(int(var1.get()), 71))
randomRobeButton = ttk.Button(text='Generate Random Robe', command=lambda: insert_text(int(var1.get()), 74))
randomScrollButton = ttk.Button(text='Generate Random Scroll', command=lambda: insert_text(int(var1.get()), 84))
randomWandButton = ttk.Button(text='Generate Random Wand', command=lambda: insert_text(int(var1.get()), 86))
randomWeaponButton = ttk.Button(text='Generate Random Weapon', command=lambda: insert_text(int(var1.get()), 100))

skillOptionDrop = OptionMenu(window, var1, *amount_list)


randomObjectButton.grid(row=0, column=1)
randomSpecialButton.grid(row=0, column=2)
randomAmuletButton.grid(row=0, column=3)
randomArmourButton.grid(row=0, column=4)
randomBootsButton.grid(row=1, column=1)
randomBowButton.grid(row=1, column=2)
randomGrimoireButton.grid(row=1, column=3)
randomPotionButton.grid(row=1, column=4)
randomRingButton.grid(row=2, column=1)
randomRobeButton.grid(row=2, column=2)
randomScrollButton.grid(row=2, column=3)
randomWandButton.grid(row=2, column=4)
randomWeaponButton.grid(row=3, column=1)
skillOptionDrop.grid(row=3, column=2)
object_text.grid(row=5, column=0)
window.mainloop()

