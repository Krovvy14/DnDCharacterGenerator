#! /usr/bin/python3
import character
import random
import dwarf
import elf
import halfling
import human
import dragonborn
import gnome
import halfelf
import halforc
import tiefling


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

races = ["Dwarf",
         "Elf",
         "Halfling",
         "Human",
         "Dragonborn",
         "Gnome",
         "Half-Elf",
         "Half-Orc",
         "Tiefling"]

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
    character = None 
    for race in races:
        #character_race = race
        character_race = "Dwarf"
    #    character_class = random.choice(classes)  

        print("character_race: {}".format(character_race))
        if character_race is 'Dwarf':
            sub_races = ["Hill Dwarf", "Mountain Dwarf"]
            sub_race = random.choice(sub_races)
            if sub_race is "Hill Dwarf":
                character = dwarf.HillDwarf("Bruenor", sub_race)
            else:
                character = dwarf.MountainDwarf("Bruenor", sub_race)
        '''
        elif character_race is 'Elf':    
            character = elf.Elf("Jakarta", character_race)
        elif character_race is 'Halfling':
            character = halfling.Halfling("Mags", character_race)
        elif character_race is 'Human':
            character = human.Human("Colin", character_race)
        elif character_race is 'Dragonborn':
            character = dragonborn.Dragonborn("John", character_race)
        elif character_race is 'Gnome':
            character = gnome.Gnome("Frodo", character_race)
        elif character_race is 'Half-Elf':
            character = halfelf.HalfElf("Zachary", character_race)
        elif character_race is 'Half-Orc':
            character = halforc.HalfOrc("Randy", character_race)
        elif character_race is 'Tiefling':
            character = tiefling.Tiefling("Inrissa", character_race)
        '''
        character.whoami()
