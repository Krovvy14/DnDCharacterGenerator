#! /usr/bin/python3
import random


ability_score = [15, 14, 13, 12, 10, 8]

def calc_modifier(score):
    return int((score - 10)/2)

class Character:
    def __init__(self, name):
        init_scores = random.sample(ability_score, len(ability_score))

        self.name = name
        self.strength = init_scores[0]
        self.strength_modifier = calc_modifier(self.strength)
        self.dexterity = init_scores[1]
        self.dexterity_modifier = calc_modifier(self.dexterity)
        self.constitution = init_scores[2]
        self.constitution_modifier = calc_modifier(self.constitution)
        self.wisdom = init_scores[3]
        self.wisdom_modifier = calc_modifier(self.wisdom)
        self.charisma = init_scores[4]
        self.charisma_modifier = calc_modifier(self.charisma)
        self.intelligence = init_scores[5]
        self.intelligence_modifier = calc_modifier(self.intelligence)
    
    def whoami(self):
        print("Hi, I'm {}".format(self.name))
        print("\tStrength:{}".format(self.strength))
        print("\tstrengh_modifier:{}".format(self.strength_modifier))
        print("\tDexterity:{}".format(self.dexterity))
        print("\tdexterity_modifier:{}".format(self.dexterity_modifier))
        print("\tConstitution:{}".format(self.constitution))
        print("\tconstitution_modifier:{}".format(self.constitution_modifier))
        print("\tWisdom:{}".format(self.wisdom))
        print("\twisdom_modifier:{}".format(self.wisdom_modifier))
        print("\tCharisma:{}".format(self.charisma))
        print("\tcharisma_modifier:{}".format(self.charisma_modifier))
        print("\tIntelligence:{}".format(self.intelligence))
        print("\tintelligence_modifier:{}".format(self.intelligence_modifier))
