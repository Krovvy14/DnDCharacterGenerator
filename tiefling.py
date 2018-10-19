import character

class Tiefling(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.intelligence = self.intelligence + 1
        self.intelligence_modifier = character.calc_modifier(self.intelligence)
        self.charisma = self.charisma + 2
        self.charisma_modifier = character.calc_modifier(self.charisma)
        self.speed = 30
        self.proficiencies.update({'Darkvision': "Can see in dim light"+\
                " within 60ft of you as if it were bright light,"+\
                " and in darkness as if it were dim light"})
        self.proficiencies.update({'Hellish Resistance': "You have "+\
                "resistance to fire damage"})
        self.proficiencies.update({'Infernal Legacy': "You know the "+\
                "thaumaturgy cantrip. Once you reach 3rd level "+\
                "you can cast the hellish rebuke spell once per day "+\
                " as a 2nd-level spell. Once you reach 5th level "+\
                ", you can also cast the darkness spell once per day. "+\
                "Charisma is your spellcasting ability for these spells"})
        self.languages.append("Common")
        self.languages.append("Infernal")
