import character

class Dwarf(character.Character):

    def __init__(self, name, character_class):
        character.Character.__init__(self, name, character_class)
        self.constitution = self.constitution + 2
        self.constitution_modifier = character.calc_modifier(self.constitution)

