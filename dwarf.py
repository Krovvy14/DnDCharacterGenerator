import character

class Dwarf(character.Character):

    def __init__(self, name):
        super().__init__(name)
        self.constitution = self.constitution + 2
        self.constitution_modifier = character.calc_modifier(self.constitution)

