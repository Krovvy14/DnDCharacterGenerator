import character

class Gnome(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.intelligence = self.intelligence + 2
        self.intelligence_modifier = character.calc_modifier(self.intelligence)
        self.speed = 25
        self.proficiencies.update({'Gnome Cunning':"You have "+\
                "advantage on Intelligence, Wisdom, and Charisma "+\
                "saving throws against magic"})
        self.languages.append("Common")
        self.languages.append("Gnomish")
