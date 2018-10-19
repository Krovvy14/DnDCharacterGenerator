import character
import random


languages = ["Dwarvish", "Giant",
             "Gnomish", "Goblin", "Halfling",
             "Orc", "Abyssal", "Celestial",
             "Draconic", "Deep Speech",
             "Infernal", "Primordial",
             "Sylvan", "Undercommon"]

skills = ["Acrobatics", "Animal Handling", "Arcana",
          "Athletics", "Deception", "History",
          "Insight", "Intimidation", "Investigation",
          "Medicine", "Nature", "Perception",
          "Performance", "Persuasion", "Religion",
          "Sleight of Hand", "Stealth", "Survival"]

class HalfElf(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.charisma = self.charisma + 2
        self.charisma_modifier = character.calc_modifier(self.charisma)


        self.speed = 30
        self.proficiencies.update({'Darkvision': "Can see in dim light"+\
                " within 60ft of you as if it were bright light,"+\
                " and in darkness as if it were dim light"})
        self.proficiencies.update({'Fey Ancestry':"You have advantage "+\
                "on saving throws against being charmed, and magic "+\
                "can't put you to sleep"})
        self.proficiencies.update({'Skill Versatility':"You gain "+\
                "proficiency in two skills of your choice"})
        self.languages.append("Common")
        self.languages.append("Elvish")
        self.languages.append(random.choice(languages))
        # TODO: Make this only return two elments of the list skills
        # not a list of lists. That shit is whack
        self.skills.append(random.sample(skills, 2))
