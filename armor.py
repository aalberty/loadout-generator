class Armor:
    def __init__(self, name, tier, item_type, equipable, power, power_limit, stats):
        self.name = name
        self.tier = tier
        self.type = item_type
        self.equipable = equipable
        self.power = power
        self.power_limit = power_limit
        self.stats = stats

    def __str__(self):
        return self.name
    
    @classmethod
    def fromCSVFile(cls, filename):
        return loadCSV(filename)

    @classmethod
    def getHunterItems(cls, items):
        return getClassItems(items, 'Hunter')

    @classmethod
    def getWarlockItems(cls, items):
        return getClassItems(items, 'Warlock')

    @classmethod
    def getTitanItems(cls, items):
        return getClassItems(items, 'Titan')  
        

def getClassItems(items, classname):
    filteredItems = []
    for item in items:
        if item.equipable == classname:
            filteredItems.append(item)
    return filteredItems

def loadCSV(filename):
    file = open(filename, 'r')
    cols = file.readline()
    lines = file.readlines()
    items = []
    for line in lines:
        raw_item = line.split(',')
        stats = {
            "mobility": raw_item[24],
            "resilience": raw_item[25],
            "recovery": raw_item[26],
            "discipline": raw_item[27],
            "intellect": raw_item[28],
            "strength": raw_item[29],
            "total": raw_item[30]
        }
        item = Armor(
            name=raw_item[0],
            tier=raw_item[4],
            item_type=raw_item[5],
            equipable=raw_item[7],
            power=raw_item[8],
            power_limit=raw_item[9],
            stats=stats
        )
        items.append(item)
    return items
        
    