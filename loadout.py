class Loadout:
    def __init__(self, name, armor_set=False):
        self.armor = {}
        self.armor['helmet'] = armor_set['Helmet'] or False
        self.armor['gauntlet'] = armor_set['Gauntlets'] or False
        self.armor['chest_armor'] = armor_set['Chest Armor'] or False
        self.armor['leg_armor'] = armor_set['Leg Armor'] or False
        self.armor['class_item'] = armor_set['citem'] or False
        self.name = name
        self.stats = {
            'mobility': {
                'value': 0,
                'tier': 0
            },
            'resilience': {
                'value': 0,
                'tier': 0
            },
            'recovery': {
                'value': 0,
                'tier': 0
            },
            'discipline': {
                'value': 0,
                'tier': 0
            },
            'intellect': {
                'value': 0,
                'tier': 0
            },
            'strength': {
                'value': 0,
                'tier': 0
            },
            'total': 0
        }
    

    def add_modifiers(self, mods):
        """
        mods - comes in form {'<stat_name>': <mod_value>, '<stat_name>': <mod_value>...}
        """
        for stat in mods:
            self.add_modifier(stat, mods[stat])


    def add_modifier(self, stat, value):
        """
        self - this instance of the Loadout class
        stat - string identifying what stat is being modified
        value - positive or negative integer to be added to the specified stat
        """

        self.stats[stat]['value']+=value

    def __str__(self):
        s = '''Name: {name}

Mobility: {mobility}
Resilience: {resilience}
Recovery: {recovery}

Discipline: {discipline}
Intellect: {intellect}
Strength: {strength}

Total: {total}
'''.format(
    name=self.name,
    mobility=str(self.stats['mobility']['value']),
    resilience=str(self.stats['resilience']['value']),
    recovery=str(self.stats['recovery']['value']),
    discipline=str(self.stats['discipline']['value']),
    intellect=str(self.stats['intellect']['value']),
    strength=str(self.stats['strength']['value']),
    total=str(self.stats['total']),
)
        return s

    @classmethod
    def calculateLoadoutTiers(cls, loadout):
        pass

    @classmethod
    def calculateStatTier(cls, stat_value):
        tier = 0
        # If stat_value <= 9, tier=0
        # If 10 <= stat_tier <= 19, tier=1
        #.
        #.
        #.
        # If 100 <= stat_tier, tier=10

        #DONT DO THIS
        if stat_value >= 20 and stat_value <=29:
            tier = 2
        elif stat_value >= 30 and stat_value <=39:
            tier = 3
        #END DONT DO THIS
        return tier