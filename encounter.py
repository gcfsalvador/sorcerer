import random,sys,time,os

#Step Counter
player_steps = 0

#Dialogues
dialogue1 = ["I want to escape.", "When will this end?", "I want to give up.", "Please let all end.", "I don't want to continue this anymore",
            "I want to see my family again", "I don't want to die.", "I have a knife and it is not for my enemies."]
dialogue2 = ["Is a grave better than being tortured?", "What time of the day is it?", "I want to sleep.", "My bones are still intact. But my brain is not",
             "Will I ever see the light of day again?", "Maybe an eternal sleep will benefit me more."]
dialogue3 = ["Why did it not attack me?", "I'm a coward...", "Thank you God.", "I survived..?"]
dialogue_check_failed = ["Nothing seems to be of mind", "Your mental state slightly decreases", "Your mind is empty.", "Your mental state slightly increases"]

def player_move():
    print("Type w,a,s,d")
    if input.lower == ["w","a","s","d"]:
        player_steps += 1
    else:
        print("Are you retarded? Try again.")
        player_move()

if player_steps == 4:
    encounter = random.randint(0, 100)
    if encounter <= 50:
        slow_type(random.choice(dialogue1))

    else:
        slow_type(random.choice(dialogue_check_failed))

if player_steps == 5:
    encounter = random.randint(0, 100)
    if encounter <= 50:
        slow_type_EXTRA("An enemy found you.")
        os.system("cls")
        player_steps == 0 #Reset to 0

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Higher enemy encounter
if player_steps == 6:
    encounter = random.randint(0, 80)
    if encounter <= 40:
        slow_type_EXTRA("An enemy has found you.")
        player_steps == 0 #Reset again

    else: 
        slow_type(random.choice(dialogue1))
        slow_type_EXTRA("You slowly become weary")

#Safe reset.
if player_steps == 7:
    encounter <= random.randint(0, 50)
    if encounter <= random.randint <= 25:
        print("An enemy found you.")
        player_steps == 0 #reset

    else:
        slow_type(random.choice(dialogue2))
        slow_type(random.choice(dialogue3))
        player_steps == 0 #safe reset.