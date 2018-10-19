#! /usr/bin/python3
import character
import random
import dwarf
import elf

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
#    character_race = random.choice(races)
#    character_class = random.choice(classes)  
    test = character.Character("Kelly")
    test.whoami()

    dwarf = dwarf.Dwarf("Bruenor")
    dwarf.whoami()

    elf = elf.Elf("Jakarta")
    elf.whoami()
