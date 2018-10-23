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
'''
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
        character_race ='Dwarf' 
        #character_class = random.choice(classes)  
        character_class = 'Barbarian'

        print("character_race: {}".format(character_race))
        if character_race is 'Dwarf':
            sub_races = ["Hill Dwarf", "Mountain Dwarf"]
            sub_race = random.choice(sub_races)
            if sub_race is "Hill Dwarf":
                character = dwarf.HillDwarf("Bruenor", sub_race,
                        character_class)
            else:
                character = dwarf.MountainDwarf("Bruenor", sub_race,
                        character_class)
        '''
        elif character_race is 'Elf':    
            sub_races = ['High Elf', 'Drow']
            sub_race = random.choice(sub_races)
            if sub_race is 'High Elf':
                character = elf.HighElf("Savannah", sub_race)
            else:
                character = elf.Drow("Jakarta", sub_race)
        elif character_race is 'Halfling':
            sub_races = ['Lightfoot', 'Stout']
            sub_race = random.choice(sub_races)
            if sub_race is 'Lightfoot':
                character = halfling.Lightfoot("Mags", sub_race)
            else:
                character = halfling.Stout("Mags", sub_race)
        elif character_race is 'Human':
            character = human.Human("Colin", character_race)
        elif character_race is 'Dragonborn':
            character = dragonborn.Dragonborn("John", character_race)
        elif character_race is 'Gnome':
            sub_races = ['Forest Gnome', 'Rock Gnome']
            sub_race = random.choice(sub_races)
            if sub_race is 'Forest Gnome':
                character = gnome.ForestGnome("Frodo", sub_race)
            else:
                character = gnome.RockGnome("Frodo", sub_race)
        elif character_race is 'Half-Elf':
            character = halfelf.HalfElf("Zachary", character_race)
        elif character_race is 'Half-Orc':
            character = halforc.HalfOrc("Randy", character_race)
        elif character_race is 'Tiefling':
            character = tiefling.Tiefling("Inrissa", character_race)
        '''

        #character.hit_points = character.hit_points + 12 + \
        character.barbarian()        
        character.whoami()
