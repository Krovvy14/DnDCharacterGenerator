import character

class Halfling(character.Character):

    def __init__(self, name):
        super().__init__(name)
        self.dexterity = self.dexterity + 2
        self.dexterity_modifier = character.calc_modifier(self.dexterity)
        self.speed = 25
        self.proficiencies.update({'Lucky':"When you roll a 1 on an attack "+\
                "roll, ability check, or saving throw, you can "+\
                "reroll the die and must use the new roll"})
        self.proficiencies.update({'Brave':"You have advantage on saving "+\
                "throws against being frightened"})
        self.proficiencies.update({'Halfling Nimbleness':"You can move "+\
                "through the space of any creature that is of a size "+\
                "larger than yours"})
        self.languages.append("Common")
        self.languages.append("Halfling")
