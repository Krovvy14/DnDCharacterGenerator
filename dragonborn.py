import character
import random


class Dragonborn(character.Character):
    draconic_ancestry = ["Black", "Blue", "Brass", "Bronze",
                         "Copper", "Gold", "Green", "Red",
                         "Silver", "White"]

    def __init__(self, name):
        super().__init__(name)
        self.strength = self.strength + 2
        self.strength_modifier = character.calc_modifier(self.strength)
        self.charisma = self.charisma + 1
        self.charisma_modifier = character.calc_modifier(self.charisma)
        self.speed = 30
        self.proficiencies.update({'Draconic Ancestry': "You have draconic "+\
                "ancestry of " + random.choice(self.draconic_ancestry) +\
                " dragon type"})
        self.proficiencies.update({'Breath Weapon':"You can use "+\
                "your action to exhale destructive energy based on "+\
                "your draconic ancestry"})
        self.proficiencies.update({'Damage Resistence':"You have "+\
                "resistance to the damage type associated "+\
                "with your draconic ancestry"})
        self.languages.append("Common")
        self.languages.append("Draconic")
