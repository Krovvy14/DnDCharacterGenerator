import character
import random

class Dwarf(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.constitution = self.constitution + 2
        self.constitution_modifier = character.calc_modifier(self.constitution)
        self.speed = 25
        self.languages.append("Common")
        self.languages.append("Dwarvish")
        self.proficiencies.update({'Darkvision': "Can see in dim light"+\
                " within 60ft of you as if it were bright light,"+\
                " and in darkness as if it were dim light"})
        self.proficiencies.update({'Dwarven Resilience':"You have "+\
                "advantage on saving throws against poison, "+\
                "and you have resistance against poison damage"})
        self.proficiencies.update({'Dwarven Combat Training':"You have "+\
                "proficiency with the battleaxe, handaxe, "+\
                "throwing hammer, and warhammer"})
        self.proficiencies.update({'Tool Proficiency':"You have " +\
                "proficiency the artisan's tools of "+\
                random.choice(["smith's tools",\
                               "brewer's supplies",\
                               "mason's tools"])})
        self.proficiencies.update({'Stonecunning':"Whenever " +\
                "you make an Intelligence(History) check related "+\
                "to the origin of stonework, you are considered "+\
                "proficient in the History skill and add double your "+\
                "proficiency bonus to the check."})

class HillDwarf(Dwarf):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.wisdom = self.wisdom + 1
        self.wisdom_modifier = character.calc_modifier(self.wisdom)
        self.hit_points = self.hit_points + 1
        self.proficiencies.update({'Dwarven Toughness':"Your hit point "+\
                "maximum increases by 1, and it increases by 1 every "+\
                "time you gain a level"})

class MountainDwarf(Dwarf):
    def __init__(self, name, race):
        super().__init__(name, race)
        self.strength = self.strength + 2
        self.strength_modifier = character.calc_modifier(self.strength)
        self.proficiencies.update({'Dwarven Armor Training': "You have "+\
                "proficiency with light and medium armor"})
