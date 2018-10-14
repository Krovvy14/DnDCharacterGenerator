#! /usr/bin/python3
import character
import random
import dwarf

races = ["Dwarf",
         "Elf",
         "Halfling",
         "Human",
         "Dragonborn",
         "Gnome",
         "Half-Elf",
         "Half-Orc",
         "Tiefling"]

classes = ["Barbarian", 
           "Bard",
           "Cleric",
           "Druid",
           "Fighter",
           "Monk",
           "Paladin",
           "Ranger",
           "Rogue",
           "Sorcerer",
           "Warlock",
           "Wizard"]
'''
barbarian_weights = 
bard_weights = 
cleric_weights = 
druid_weights = 
fighter_weights = 
monk_weights = 
paladin_weights = 
ranger_weights = 
rogue_weights = 
sorcerer_weights = 
warlock_weights = 
wizard_weights = 
'''
if __name__ == "__main__":
    character_race = random.choice(races)
    character_class = random.choice(classes)  
    test = character.Character("Kyle", random.choice(classes))
    test.whoami()
    print(test.constitution)


    test2 = character.Character("Kelly", random.choice(classes))
    test2.whoami()

    dwarf = dwarf.Dwarf("Bruenor", random.choices(classes))
    dwarf.whoami()
    dwarf.whoami()
