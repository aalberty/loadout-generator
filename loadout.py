class Loadout:

    def __init__(self, name, armor_set=False):
        self.name = name
        self.armor = {}
        self.stats = self.__stat_factory()

        if armor_set is not False:
            self.armor['helmet'] = armor_set['Helmet']
            self.armor['gauntlet'] = armor_set['Gauntlets']
            self.armor['chest_armor'] = armor_set['Chest Armor']
            self.armor['leg_armor'] = armor_set['Leg Armor']
            self.armor['class_item'] = armor_set['citem']
            self.__set_stats_from_armor(self.armor)
            return


    def add_modifiers(self, mods):
        """
        mods - comes in form {'<stat_name>': <mod_value>, '<stat_name>': <mod_value>...}
        """
        for stat in mods:
            self.add_modifier(stat, mods[stat])
            return


    def add_modifier(self, stat, value):
        """
        self - this instance of the Loadout class
        stat - string identifying what stat is being modified
        value - positive or negative integer to be added to the specified stat
        """

        self.stats[stat]['value']+=value
        return

    # INTERNAL
    def __set_stats_from_armor(self, armor):
        if type(armor) == type({}):
            armor = list(armor.values())
        
        for item in armor:
            armor_stats = item.stats.items()
            for s,v in armor_stats:
                if s == 'total':
                    pass
                else:
                    val = int(v)
                    self.stats[s]['value'] = self.stats[s]['value'] + val
                    #self.stats[s]['tier'] = __calculateStatTier(self.stats[stat]['value'])
        return

    # INTERNAL
    def __stat_factory(self):
        return {
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
                }
            }

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
    def calculate_stat_tier(cls, stat_value):
        """
        stat_value - integer value of a specific stat
        returns the tier (0-10) of the given stat_value
        """
        return __calculate_stat_tier(stat_value)

    
    def __calculate_stat_tier(self, stat_value):
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

