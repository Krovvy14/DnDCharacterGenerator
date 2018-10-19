import character

class Elf(character.Character):

    def __init__(self, name):
        super().__init__(name)
        self.dexterity = character.calc_modifier(self.dexterity)
        self.speed = 30
        self.proficiencies.update({'Keen Senses':"You have proficiency "+\
                "in the Perception skill"})
        self.skills.append("Perception")
        self.proficiencies.update({'Fey Ancestry':"You have advantage "+\
                "on saving throws against being charmed, and magic "+\
                "can't put you to sleep"})
        self.proficiencies.update({'Trance':"You gain the benefits of "+\
                "a long rest after 4 hours of meditation"})
        self.languages.append("Common")
        self.languages.append("Elvish")
