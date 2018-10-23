import character
import random

languages = ["Dwarvish", "Giant",
             "Gnomish", "Goblin", "Halfling",
             "Orc", "Abyssal", "Celestial",
             "Draconic", "Deep Speech",
             "Infernal", "Primordial",
             "Sylvan", "Undercommon"]

class Elf(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.dexterity = character.calc_modifier(self.dexterity)
        self.speed = 30
        self.proficiencies.update({'Keen Senses':"You have proficiency "+\
                "in the Perception skill"})
        self.skills.append("Perception")
        self.proficiencies.update({'Fey Ancestry':"You have advantage "+\
                "on saving throws against being charmed, and magic "+\
                "can't put you to sleep"})
        self.proficiencies.update({'Trance':"You gain the benefits of "+\
                "a long rest after 4 hours of meditation"})
        self.languages.append("Common")
        self.languages.append("Elvish")


class HighElf(Elf):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.intelligence = self.intelligence + 1
        self.intelligence_modifier = character.calc_modifier(self.intelligence)
        self.proficiencies.update({'Elf Weapon Training': "You have "+\
                "proficiency in the longsword, shortsword, shortbow "+\
                "and longbow."})
        self.proficiencies.update({'Cantrip': "You know one cantrip "+\
                "from the wizard spell list"})
        self.proficiencies.update({'Extra Language': "You can speak "+\
                "read, and write one extra language of your choice"})
        self.languages.append(random.choice(languages))

class Drow(Elf):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.charisma = self.charisma + 1
        self.charisma_modifier = character.calc_modifier(self.charisma)
        self.proficiencies.update({'Superior Darkvision': "Your darkvision "+\
                "has a radius of 120ft"})
        self.proficiencies.update({'Sunlight Sensitivity': "You have "+\
                "disadvantage on attack rolls and on Wisdom(Perception) "+\
                "that rely on sight when you, the target of the attack "+\
                "or whatever you are trying to perceive is in direct "+\
                "sunlight"})
        self.proficiencies.update({'Drow Magic':"You know the dancing "+\
                "lights cantrip. When you read 3rd level, you can cast "+\
                "the faerie fire spell once per day. When you reach 5th "+\
                "level, you can also cast the darkness spell once per day "+\
                "Charisma is your spellcasting ability for these spells"})
        self.proficiencies.update({'Drow Weapon Training': "You have "+\
                "proficiency with rapier, shortswords, and hand crossbows."})
