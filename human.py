import character
import random


languages = ["Dwarvish", "Elvish", "Giant",
             "Gnomish", "Goblin", "Halfling",
             "Orc", "Abyssal", "Celestial",
             "Draconic", "Deep Speech",
             "Infernal", "Primordial",
             "Sylvan", "Undercommon"]

class Human(character.Character):
    def __init__(self, name):
        super().__init__(name)
        self.strength = self.strength + 1
        self.strength_modifier = character.calc_modifier(self.strength)
        self.dexterity = self.dexterity + 1
        self.dexterity_modifier = character.calc_modifier(self.dexterity)
        self.constitution = self.constitution + 1
        self.constitution_modifier = character.calc_modifier(self.constitution)
        self.intelligence = self.intelligence + 1
        self.intelligence_modifier = character.calc_modifier(self.intelligence)
        self.wisdom = self.wisdom + 1
        self.wisdom_modifier = character.calc_modifier(self.wisdom)
        self.charisma = self.charisma + 1
        self.charisma_modifier = character.calc_modifier(self.charisma)
        self.speed = 30
        self.languages.append("Common")
        self.languages.append(random.choice(languages))
