import character


class HalfOrc(character.Character):

    def __init__(self, name, race):
        super().__init__(name, race)
        self.strength = self.strength + 2
        self.strength_modifier = character.calc_modifier(self.strength)
        self.constitution = self.constitution + 1
        self.constitution_modifier = character.calc_modifier(self.constitution)
        self.speed = 30

        self.proficiencies.update({'Darkvision': "Can see in dim light"+\
                " within 60ft of you as if it were bright light,"+\
                " and in darkness as if it were dim light"})
        self.proficiencies.update({'Menacing': "You gain "+\
                "proficiency in Intimidation skill"})
        self.skills.append("Intimidation")
        self.proficiencies.update({'Relentless Endurance': "When you "+\
                "are reduced to 0 hit points but not killed outright" +\
                ",you can drop to 1HP instead. You can't use this "+\
                "feature again until you finish a long rest"})
        self.proficiencies.update({'Savage Attacks':"When you score "+\
                "a critical hit with a melee weapon attack, you can "+\
                "roll one of the weapon's damage dice one additional "+\
                "time and add it to the extra damage of the critical "+\
                "hit."})
        self.languages.append("Common")
        self.languages.append("Orcish")
