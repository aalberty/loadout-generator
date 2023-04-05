import armor
items = armor.Armor.fromCSVFile('sample.csv')
# Sort by type
types = ["Helmet", "Gauntlets", "Chest Armor", "Leg Armor"]
class_item_types = {
    "hunter": "Hunter Cloak",
    "warlock": "Warlock Bond",
    "titan": "Titan Mark"
}

def loadClassArmor(guardian_class):
    class_item_type = class_item_types[guardian_class.lower()]
    class_armor = list(filter(lambda x: x.equipable.lower() == guardian_class.lower(), items))

    helmets = filter(lambda x: x.type == types[0], class_armor)
    gauntlets = filter(lambda x: x.type == types[1], class_armor)
    chest = filter(lambda x: x.type == types[2], class_armor)
    leg = filter(lambda x: x.type == types[3], class_armor)
    citem = filter(lambda x: x.type == class_item_type, class_armor)
    return {
        "className": guardian_class,
        "helmets": list(helmets), 
        "gauntlets": list(gauntlets), 
        "chest": list(chest), 
        "leg": list(leg), 
        "citem": list(citem)
        }



# index == 5 return list as a loadout

# else, add next armor piece based on index
armor_types = ['helmets', 'gauntlets', 'chest', 'leg', 'citem']

def buildLoadouts():
    pass

loadoutObjs = []
def loopArmor(classArmorList):
    for helmet in classArmorList['helmets']:
        for gauntlet in classArmorList['gauntlets']:
            for chest in classArmorList['chest']:
                for leg in classArmorList['leg']:
                    for citem in classArmorList['citem']:
                        loadoutObjs.append({
                            'Helmet': helmet,
                            'Gauntlets': gauntlet,
                            'Chest Armor': chest,
                            'Leg Armor': leg,
                            'citem': citem
                        })


