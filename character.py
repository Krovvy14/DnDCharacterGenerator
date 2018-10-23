#! /usr/bin/python3
import random


def calc_modifier(score):
    return int((score - 10)/2)

class Character:
    ability_score = [15, 14, 13, 12, 10, 8]
    alignments = ["LG", "LN", "LE", "CG", "CN", "CE", "NG", "TN", "NE"]

    def __init__(self, name, race, character_class):
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
        self.character_class = character_class
        self.race = race
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
        self.class_features = {}
    
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
        print("\tClass Features: {}".format(self.class_features))
        

    def barbarian(self):
        skills = ['Animal Handling', 'Athletics', 'Intimidation',
                  'Nature', 'Perception', 'Survival']

        self.hit_points = self.hit_points + 12 + self.constitution_modifier
        self.skills.append(random.sample(skills, 2))
        self.saving_throws.append('Strength')
        self.saving_throws.append('Constitution')
        self.proficiencies.update({'Light Armor':"Light armor"}) 
        self.proficiencies.update({'Medium Armor':"Medium armor"}) 
        self.proficiencies.update({'Shields':"Shields"}) 
        self.proficiencies.update({'Simple Weapons':"Simple Weapons"}) 
        self.proficiencies.update({'Martial Weapons':"Martial Weapons"}) 
        self.class_features.update({'Rage': "In battle you fight with primal "+\
                            "ferocity. On your turn you can enter a rage as "+\
                            "a bonus action. While raging you gain the "+\
                            "following benefits if you aren't wearing heavy "+\
                            "You have advantage on Str checks and Str saving "+\
                            "throws. When you make a melee weapon attack using "+\
                            "Str, you gain a bonus to the dmg roll. You have "+\
                            "resistance to bludgeoning, piercing, and slashing "+\
                            "damage."})
        self.class_features.update({'Unarmored Defense': "While not wearing any "+\
                            "armor, your AC equals 10+your Dex modifier+your "+\
                            "Con modifier. You can use a shield and still gain "+\
                            "this benefit."})
