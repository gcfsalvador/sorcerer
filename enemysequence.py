import random,math,os
import encounter,menu
#Enemy Encounter
monsternames = ["Goblin", "Slime", "Skeleton", "Walking Corpse", "Muscle Meat", "Transfigurated Human", "Flesh-Eater", "Elemental Residue", "Diabeter",
                "Dead-Knight", "Skull Knight", "Adamin", "Evenin", "Grave-Mix", "Cyclops", "Orc", "Human-Orca", "Creep", "Devil's Minion"]
titlemonsters = ["Type 0", "Type 1", "Type 2", "Type 3", "Type 4", "Type Nexus", "Type Unregistered", "Extincted"]

def generate_monster():
    print(random.choice(titlemonsters), random.choice(monsternames))

enemy_name = generate_monster

#Fight selections
slow_type_EXTRA("THEY HAVE FOUND YOU.")
os.system("cls")
