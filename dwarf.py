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
