class Loadout:
    def __init__(self, name):
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
    

    def add_modifier(self, stat, value):
        """
        self - this instance of the Loadout class
        stat - string identifying what stat is being modified
        value - positive or negative integer to be added to the specified stat
        """
        pass

    def __str__(self):
        s = '''
            Name: {name}

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