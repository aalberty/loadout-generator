import armor
items = armor.Armor.fromCSVFile('destinyArmor.csv')
# Sort by type
types = ["Helmet", "Gauntlets", "Chest Armor", "Leg Armor"]
class_item_types = {
    "Hunter": "Hunter Cloak",
    "Warlock": "Warlock Bond",
    "Titan": "Titan Mark"
}

def loadClassArmor(guardian_class):
    class_item_type = class_item_types[guardian_class]
    class_armor = list(filter(lambda x: x.equipable == guardian_class, items))

    helmets = filter(lambda x: x.type == types[0], class_armor)
    gauntlets = filter(lambda x: x.type == types[1], class_armor)
    chest = filter(lambda x: x.type == types[2], class_armor)
    leg = filter(lambda x: x.type == types[3], class_armor)
    citem = filter(lambda x: x.type == class_item_type, class_armor)
    return {
        "helmets": list(helmets), 
        "gauntlets": list(gauntlets), 
        "chest": list(chest), 
        "leg": list(leg), 
        "citem": list(citem)
        }