import armor, loadout
# Sort by type
types = ["Helmet", "Gauntlets", "Chest Armor", "Leg Armor"]
class_item_types = {
    "hunter": "Hunter Cloak",
    "warlock": "Warlock Bond",
    "titan": "Titan Mark"
}

armor_types = ['helmets', 'gauntlets', 'chest', 'leg', 'citem']

def loadClassArmor(all_armor, guardian_class):
    class_item_type = class_item_types[guardian_class.lower()]
    class_armor = list(filter(lambda x: x.equipable.lower() == guardian_class.lower(), all_armor))

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

def buildLoadouts(armor_sets):
    loadouts = []
    index = 0
    for armor_set in armor_sets:
        loadouts.append(loadout.Loadout('sample_set_' + str(index), armor_set))
        index += 1
    return loadouts

def loopArmor(classArmorList, armor_sets=[]):
    for helmet in classArmorList['helmets']:
        for gauntlet in classArmorList['gauntlets']:
            for chest in classArmorList['chest']:
                for leg in classArmorList['leg']:
                    for citem in classArmorList['citem']:
                        armor_sets.append({
                            'Helmet': helmet,
                            'Gauntlets': gauntlet,
                            'Chest Armor': chest,
                            'Leg Armor': leg,
                            'citem': citem
                        })
    return armor_sets


items = armor.Armor.fromCSVFile('sample.csv')
h = loadClassArmor(items, 'hunter')
armor_sets = loopArmor(h)
loadouts = buildLoadouts(armor_sets)





