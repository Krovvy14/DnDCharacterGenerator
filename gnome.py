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


class ForestGnome(Gnome):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.dexterity = self.dexterity + 1
        self.dexterity_modifier = character.calc_modifier(self.dexterity)
        self.proficiencies.update({'Natural Illusionist':"You know the "+\
                "minor illusion cantrip. Intelligence is your spellcasting "+\
                "ability for it."})
        self.proficiencies.update({'Speak with Small Beasts':"Through "+\
                "sounds and gestures, you can communicate simple ideas "+\
                "with Small or smaller beasts. Forest gnomes love animals "+\
                "and often keep squirrels, badgers, rabbits, moles, "+\
                "woodpeckers, and other creatures as beloved pets."})


class RockGnome(Gnome):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.constitution = self.constitution + 1
        self.constitution_modifier = character.calc_modifier(self.constitution)
        self.proficiencies.update({"Artificer's Lore":"Whenever you "+\
                "make and Intelligence(History) check related to magic "+\
                "items, you can spend 1 hour and 10gp worth of materials "+\
                "to construct a Tiny clockwork device (AC 5, 1hp). The "+\
                "device ceases to function after 24 hours (unless you "+\
                "spend 1 hour repairing it to keep the device functioning) "+\
                ", or when you reclaim the materials used to create it. "+\
                "You can have up to three such devices active at a time."+\
                "Choose one of the following options: Clockwork Toy, "+\
                "Fire Starter, Music Box"})
