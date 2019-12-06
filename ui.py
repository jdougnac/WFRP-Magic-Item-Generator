import launcher
import mutation

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
    if category > 150:
        if category == 666:
            object_list = mutation.random_mutation(amount)
        elif category == 667:
            object_list = mutation.random_mutation_khorne(amount)
        elif category == 668:
            object_list = mutation.random_mutation_nurgle(amount)
        elif category == 669:
            object_list = mutation.random_mutation_slaanesh(amount)
        elif category == 670:
            object_list = mutation.random_mutation_tzeentch(amount)
        object_text.delete('1.0', END)
        print(object_list)
        for item in object_list:
            object_text.insert(END, item)
            object_text.insert(END, '\n')
    else:
        object_list = launcher.return_items(amount, category)
        object_text.delete('1.0', END)
        for item in object_list:
            object_text.insert(END, item)
            object_text.insert(END, '\n')


randomObjectButton = ttk.Button(text='Random Object', command=lambda: insert_text(int(var1.get()), 0))
randomSpecialButton = ttk.Button(text='Special', command=lambda: insert_text(int(var1.get()), 11))
randomAmuletButton = ttk.Button(text='Amulet', command=lambda: insert_text(int(var1.get()), 19))
randomArmourButton = ttk.Button(text='Armour', command=lambda: insert_text(int(var1.get()), 32))
randomBootsButton = ttk.Button(text='Boots', command=lambda: insert_text(int(var1.get()), 42))
randomBowButton = ttk.Button(text='Bow', command=lambda: insert_text(int(var1.get()), 48))
randomGrimoireButton = ttk.Button(text='Grimoire', command=lambda: insert_text(int(var1.get()), 54))
randomPotionButton = ttk.Button(text='Potion', command=lambda: insert_text(int(var1.get()), 62))
randomRingButton = ttk.Button(text='Ring', command=lambda: insert_text(int(var1.get()), 71))
randomRobeButton = ttk.Button(text='Robe', command=lambda: insert_text(int(var1.get()), 74))
randomScrollButton = ttk.Button(text='Scroll', command=lambda: insert_text(int(var1.get()), 84))
randomWandButton = ttk.Button(text='Wand', command=lambda: insert_text(int(var1.get()), 86))
randomWeaponButton = ttk.Button(text='Weapon', command=lambda: insert_text(int(var1.get()), 100))
randomMutationButton = ttk.Button(text='Chaos Mutation', command=lambda: insert_text(int(var1.get()), 666))
randomKhorneMutationButton = ttk.Button(text='Khorne Mutation', command=lambda: insert_text(int(var1.get()), 667))
randomNurgleMutationButton = ttk.Button(text='Nurgle Mutation', command=lambda: insert_text(int(var1.get()), 668))
randomSlaaneshMutationButton = ttk.Button(text='Slaanesh Mutation', command=lambda: insert_text(int(var1.get()), 669))
randomTzeentchMutationButton = ttk.Button(text='Tzeentch Mutation', command=lambda: insert_text(int(var1.get()), 670))

skillOptionDrop = OptionMenu(window, var1, *amount_list)


randomObjectButton.grid(row=0, column=1)
randomSpecialButton.grid(row=0, column=2)
randomAmuletButton.grid(row=0, column=3)
randomArmourButton.grid(row=0, column=4)
randomMutationButton.grid(row=0, column=5)
randomSlaaneshMutationButton.grid(row=0, column=6)
randomBootsButton.grid(row=1, column=1)
randomBowButton.grid(row=1, column=2)
randomGrimoireButton.grid(row=1, column=3)
randomPotionButton.grid(row=1, column=4)
randomKhorneMutationButton.grid(row=1, column=5)
randomTzeentchMutationButton.grid(row=1, column=6)
randomRingButton.grid(row=2, column=1)
randomRobeButton.grid(row=2, column=2)
randomScrollButton.grid(row=2, column=3)
randomWandButton.grid(row=2, column=4)
randomNurgleMutationButton.grid(row=2, column=5)
randomWeaponButton.grid(row=3, column=1)
skillOptionDrop.grid(row=3, column=2)
object_text.grid(row=5, column=0)
window.mainloop()

