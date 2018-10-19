#! /usr/bin/python3
import random


def calc_modifier(score):
    return int((score - 10)/2)

class Character:
    ability_score = [15, 14, 13, 12, 10, 8]
    alignments = ["LG", "LN", "LE", "CG", "CN", "CE", "NG", "TN", "NE"]
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

    def __init__(self, name):
        '''
        //////
        //Character Archetype
        //////
        name = ""
        character_class = ""
        race = ""
        alignment = ""
        strength = 0
        dexterity = 0
        constitution = 0
        intelligence = 0
        wisdom = 0
        charisma = 0
        saving_throws = []
        skills = []
        proficiency_bonus = 2
        armor_class = 0
        hit_points = 0
        speed = 0
        proficiencies = {}
        languages = []
        '''


        init_scores = random.sample(self.ability_score,
                                    len(self.ability_score))
        self.name = name
        self.character_class = random.choice(Character.classes) 
        self.race = random.choice(Character.races)
        self.alignment = random.choice(Character.alignments) 
        self.strength = init_scores[0]
        self.strength_modifier = calc_modifier(self.strength)
        self.dexterity = init_scores[1]
        self.dexterity_modifier = calc_modifier(self.dexterity)
        self.constitution = init_scores[2]
        self.constitution_modifier = calc_modifier(self.constitution)
        self.intelligence = init_scores[5]
        self.intelligence_modifier = calc_modifier(self.intelligence)
        self.wisdom = init_scores[3]
        self.wisdom_modifier = calc_modifier(self.wisdom)
        self.charisma = init_scores[4]
        self.charisma_modifier = calc_modifier(self.charisma)
        self.saving_throws = []
        self.skills = []
        self.proficiency_bonus = 2
        self.armor_class = 0
        self.hit_points = 0
        self.speed = 0
        self.proficiencies = {}
        self.languages = []
    
    def whoami(self):
        print("Hi, I'm {}. I am a {} {}".format(self.name,
                                                self.race,
                                                self.character_class))
        print("Alignment:{}".format(self.alignment))
        print("\tStrength:{}".format(self.strength))
        print("\tstrengh_modifier:{}".format(self.strength_modifier))
        print("\tDexterity:{}".format(self.dexterity))
        print("\tdexterity_modifier:{}".format(self.dexterity_modifier))
        print("\tConstitution:{}".format(self.constitution))
        print("\tconstitution_modifier:{}".format(self.constitution_modifier))
        print("\tIntelligence:{}".format(self.intelligence))
        print("\tintelligence_modifier:{}".format(self.intelligence_modifier))
        print("\tWisdom:{}".format(self.wisdom))
        print("\twisdom_modifier:{}".format(self.wisdom_modifier))
        print("\tCharisma:{}".format(self.charisma))
        print("\tcharisma_modifier:{}".format(self.charisma_modifier))
        print("\tsaving_throws:{}".format(self.saving_throws))
        print("\tskills:{}".format(self.skills))
        print("\tproficiency_bonus:{}".format(self.proficiency_bonus))
        print("\tarmor_class:{}".format(self.armor_class))
        print("\thit_points:{}".format(self.hit_points))
        print("\tspeed:{}".format(self.speed))
        print("\tProficiencies: {}".format(self.proficiencies))
        print("\tLanguages: {}".format(self.languages))
        

