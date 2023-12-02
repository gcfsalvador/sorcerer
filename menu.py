import os,sys,time,random

typing_speed = 50 #wpm
#Slow Input to be immersive.
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print ('')

def slow_type_EXTRA(t): 
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*7.0/typing_speed)
    print ('')

class Entity(object):
    name = ""
    type = ""
    health = 50
    strength = 7
    defence = 3

#3 Main Classes
class rogue (object):
    health = 75
    strength = 10
    defence = 10
    magic = 1

class sorcerer (object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class warlock (object):
    health = 100
    strength = 5
    defence = 10
    magic = 7

def heroselect():
    print ("Select your Vocation.")
    selection = input("1. Rogue \n2. Warlock \n3. Hunter \n")
    if selection == "1":
        character = rogue
        print ("You have selected the rogue...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = warlock
        print ("You have selected the warlock...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = sorcerer
        print ("You have selected the hunter...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def battlestate():
    enemy = Entity
    print("a wild", enemy, "has appeared!")
    print ("you have 3 options...")
    while enemy.health > 0 :
        choice = input("1. Sword\n2. Magic \n3. RUN!")

        if choice == "1":
            print ("You swing your weapons against the ", enemy)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("It's vigor has lowered. ", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "attacks you leaving", character.health)
                    gameOver(character)

def gameOver(character):
    if character.health < 1:
        print("You have fell into the Abyss, Becoming one of it's victims")
        print("Thanks for playing...")

        exit()


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        os.system('cls')
        setup_game()

    elif option.lower() == ("help"):
        os.system('cls')
        help_menu()

    elif option.lower() == ("credit"):
        os.system('cls')
        credit_menu()

    elif option.lower() == ("quit"):
        sys.exit()

    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid comand")
        option = input("> ")

        if option.lower() == ("play"):
            os.system('cls')
            setup_game()# placeholder until written

        elif option.lower() == ("help"):
            os.system('cls')
            help_menu()

        elif option.lower() == ("credit"):
            os.system('cls')
            credit_menu()

        elif option.lower() == ("quit"):
            sys.exit()

def setup_game():
    slow_type("What is your name?")
    name = input("> ")
    slow_type(f"I see, {name}. A wonderful name, but it can be better.")
    slow_type("What class do you choose?")
    heroselect()
    battlestate()

def help_menu():
    print("There is none. Ask the devs")
    print("play")
    print("credits")
    print("quit")
    title_screen_selections()

def credit_menu():
    print("Gian Cyrus F. Salvador, Fredmar Declas, Doniele Arys Antonio, Claudio Van Likigan")
    print("play")
    print("help")
    print("quit")
    title_screen_selections()

def title_screen():
    print(""" 
 _                             _   _                  __ _                
| |                           | | | |                / _(_)               
| |    _   _ _ __  _   _ ___  | | | | ___ _ __   ___| |_ _  ___ _   _ ___ 
| |   | | | | '_ \| | | / __| | | | |/ _ \ '_ \ / _ \  _| |/ __| | | / __|
| |___| |_| | |_) | |_| \__ \ \ \_/ /  __/ | | |  __/ | | | (__| |_| \__ |
\_____/\__,_| .__/ \__,_|___/  \___/ \___|_| |_|\___|_| |_|\___|\__,_|___/
            | |                                                           
            |_|                                                           """)
    print("                    play")
    print("                    help")
    print("                   credit")
    print("                    quit")
    title_screen_selections()

title_screen()
