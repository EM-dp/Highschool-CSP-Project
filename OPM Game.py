# -*- coding: utf-8 -*-
import sys
import time
import random

black = "\033[30m"
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
bold = "\033[1m"
underline = "\033[4m"
end = "\033[0m"

Replay = True
Start = False
UseMove = False
Completed = False
Completed2 = False

Super = "Not Active"
SuperUsed = False
ComputerSuperUsed = False

Enemy = ""
ComputerMove = 0
UserMove = ""

# computer base stats
CompDef = 0
CompSpe = 0

# computer attack buffs
CompAtkBuff = 1.0
CompDefBuff = 1.0

# Stages
ClearLevel1 = False
ClearLevel2 = False
ClearLevel3 = False
ClearLevel4 = False
ClearLevel5 = False
ClearLevel6 = False

# Stages (For characterChoice = Garou)
ClearLevel1Garou = False
ClearLevel2Garou = False
ClearLevel3Garou = False
ClearLevel4Garou = False

# Variables to store all character's stats
# Levels
TornadoLvl = 1
BangLvl = 1
GenosLvl = 1
MetalBatLvl = 1
SonicLvl = 1
MumenRiderLvl = 1
GarouLvl = 1

# Exp points
TornadoXp = 0
BangXp = 0
GenosXp = 0
MetalBatXp = 0
SonicXp = 0
MumenRiderXp = 0
GarouXp = 0

# Attack power
TornadoAtk = 300
BangAtk = 250
GenosAtk = 250
MetalBatAtk = 250
SonicAtk = 250
MumenRiderAtk = 150
GarouAtk = 300

# Defense
TornadoDef = 180
BangDef = 230
GenosDef = 200
MetalBatDef = 180
SonicDef = 100
MumenRiderDef = 100
GarouDef = 230

# Speed
TornadoSpe = 200
BangSpe = 230
GenosSpe = 250
MetalBatSpe = 200
SonicSpe = 200
MumenRiderSpe = 150
GarouSpe = 220

# Used to track any stat bonuses
SpeUp = 1.0
AtkUp = 1.0
DefUp = 1.0

# Health point storage variables
UserHp = 100
ComputerHp = 100

# Tornado's moves
Tornado1 = "\nTelekenetic Throw: Attacks with 120% power plus 10% for every time it has been used previously this battle. "
Tornado2 = "\nMeditation: Increases attack by 1.5x for 2 turns."
Tornado3 = "\nTelekinetic Tornado: Attacks with 60% power and deals 120% over two turns after."
Tornado4 = "\nSuper Move (Must be below 50% health and can only be used once)\n Telekinetic Pause: (Priority) Your opponent deals no damage to you during this turn and next turn."

# Bang's moves
Bang1 = "\n" + bold + "Water Stream Encampment:" + end + " (Priority) Reduces damage taken by 50% this turn and counter attacks with 100% power."
Bang2 = "\n" + bold + "Abandonment:" + end + " (Can only be used once per fight) Increases attack and speed by 1.5x for 3 turns."
Bang3 = "\n" + bold + "Fang Interpolation:" + end + " Attacks with 160% power."
Bang4 = "\n" + yellow + bold + "Super Move " + end + "(Must be below 50% health and can only be used once)\n " + bold + "Water Stream Rock Smashing Fist:" + end + " Attacks with 250% power"

# Genos' moves
Genos1 = " "
Genos2 = " "
Genos3 = " "
Genos4 = " "

# Metal Bat's moves
MetalBat1 = " "
MetalBat2 = " "
MetalBat3 = " "
MetalBat4 = " "

# Speed-o'-Sound Sonic's moves
Sonic1 = " "
Sonic2 = " "
Sonic3 = " "
Sonic4 = " "

# Mumen Rider's moves
MumenRider1 = " "
MumenRider2 = " "
MumenRider3 = " "
MumenRider4 = " "

# Garou's moves
Garou1 = " "
Garou2 = " "
Garou3 = " "
Garou4 = " "


# Default "loading screen" for this game in a function.
def loading():
    print ("⠀⠀⠀ ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷\n⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇\n⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇\n⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇\n⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼\n⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀\n⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀")
    a = 0
    for x in range(0, 3):
        a = a + 1
        b = ("Loading" + "." * a)
        sys.stdout.write("\r" + b)
        time.sleep(2)
    sys.stdout.write("\r" + "            " + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


# Calculates combat damage in battle using 3 stats
def combat_damage(attack_pwr, attack_buff, char_atk, defense, defense_buff):
    return int(((char_atk * attack_buff) / (defense * defense_buff)) * (attack_pwr / 10.0))


# Random crit and weak hit simulator (Weak hit x >= 95, Crit x<=5)
def random_crit():
    x = random.randint(1, 100)
    if x <= 5:
        return 2
    elif x >= 95:
        return 3
    else:
        return 1


# Checks after battles, this function will check if the character will level up. (true if lvl up, false if not)
def lvl_up(xp, lvl):
    if lvl == 1:
        if xp >= 100:
            return True
        else:
            return False
    elif lvl == 2:
        if xp >= 200:
            return True
        else:
            return False
    elif lvl == 3:
        if xp >= 300:
            return True
        else:
            return False
    elif lvl == 4:
        if xp >= 400:
            return True
        else:
            return False
    elif lvl == 5:
        if xp >= 500:
            return True
        else:
            return False
    elif lvl == 6:
        if xp >= 600:
            return True
        else:
            return False
    elif lvl == 7:
        if xp >= 700:
            return True
        else:
            return False
    elif lvl == 8:
        if xp >= 800:
            return True
        else:
            return False
    elif lvl == 9:
        if xp >= 900:
            return True
        else:
            return False
    else:
        if xp >= 1000:
            return True
        else:
            return False


# Gives a semi-accurate display of both character's current health totals
def display_hp(user_hp, computer_hp):
    print(Character + ": [" + ("|" * int(user_hp / 10)) + (" " * (10 - (int(user_hp / 10)))) + "]  " + str(user_hp) + "/100 Hp\t\t\t\t" + Enemy + ": [" + ("|" * int(computer_hp / 10)) + (" " * (10 - (int(computer_hp / 10)))) + "]  " + str(computer_hp) + "/100 Hp")


def computer_move_funct():
    return random.randint(1, 3)


# Title and Start screens of the game.
loading()
print("\n\nWelcome to the Hero Association!\n\n")
while not Start:
    time.sleep(2)
    YN = raw_input("Would you like to start (Y/N)? ")
    if YN == "Yes" or YN == "yes" or YN == "y" or YN == "Y" or YN == "YES":
        Start = True
    else:
        print("\nTry inputting YES or Y instead.\n")

# checks to see if they want to replay and only loops if they want to play again.
while Replay:
    ErrorCheck = True
    loading()
    # loops until the player enters a valid input for a character choice.
    while ErrorCheck:
        print"Character List: "
        time.sleep(0.5)
        print("Heroes and Other Characters: 1. Tornado (lvl " + str(TornadoLvl) + ")" + "  2. Bang (lvl " + str(BangLvl) + ")" + "  3. Genos (lvl " + str(GenosLvl) + ")" + "  4. Speed-o'-Sound Sonic (lvl " + str(SonicLvl) + ")" + "  5. Metal Bat (lvl " + str(MetalBatLvl) + ")")
        if Completed:
            time.sleep(0.5)
            print("Unlocked: 6. Garou (lvl " + str(GarouLvl) + ")")
        if Completed2:
            print("Unlocked Special: 7. Mumen Rider (lvl " + str(MumenRiderLvl) + ")")
        time.sleep(1.5)
        # Player chooses what character they want to play as. Garou is unlocked if they have completed the game before.
        if Completed and Completed2:
            CharacterChoice = input("Choose a Character (1-7): ")
        elif Completed:
            CharacterChoice = input("Choose a Character (1-6): ")
        else:
            CharacterChoice = input("Choose a Character (1-5): ")
        # Assigns the character they chose to a string variable for later use and checks for valid character choice.
        ErrorCheck = False
        if CharacterChoice == 1:
            Character = green + "Tornado" + end
        elif CharacterChoice == 2:
            Character = green + "Bang" + end
        elif CharacterChoice == 3:
            Character = green + "Genos" + end
        elif CharacterChoice == 5:
            Character = green + "Metal Bat" + end
        elif CharacterChoice == 4:
            Character = green + "Speed-o'-Sound Sonic" + end
        elif CharacterChoice == 7 and Completed and Completed2:
            Character = green + "Mumen Rider" + end
        elif CharacterChoice == 6 and Completed:
            Character = red + "Garou" + end
        else:
            ErrorCheck = True
            print("Invalid Input. Please try again.")

    # Starts the game with the character Tornado selected
    if CharacterChoice == 1:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(TornadoAtk) + " Defense:" + str(TornadoDef) + " Speed:" + str(TornadoSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        print("Lets start you off with an introduction fight to help you fit in with the other heroes.")
        time.sleep(4)
        print("There is a villain calling himself Crablante who has been going around killing people, your job is to stop him.\n")
        time.sleep(4)
        ComputerHp = 100
        while UserHp > 0 and ComputerHp > 0:
            Enemy = red + "Crablante" + end
            UseMove = False
            if UserHp <= 50:
                Super = "Active"
            elif UserHp > 50:
                Super = "Not Active"
            display_hp(UserHp, ComputerHp)
            if ComputerHp <= 50 and not ComputerSuperUsed:
                ComputerMove = 4
            else:
                ComputerMove = computer_move_funct()
            while not UseMove:
                UserMove = raw_input("\nChoose a move (Enter info1, info2, etc. for info on a speific move):\n1. Telekenetic Throw\t\t2. Meditation\n3. Telekinetic Tornado\t\t4. (Super) Telelkinetic Pause \n")
                if str(UserMove) == "info1" or str(UserMove) == "Info1" or str(UserMove) == "INFO1":
                    print Tornado1
                    time.sleep(5.0)
                elif str(UserMove) == "info2" or str(UserMove) == "Info2" or str(UserMove) == "INFO2":
                    print Tornado2
                    time.sleep(5.0)
                elif str(UserMove) == "info3" or str(UserMove) == "Info3" or str(UserMove) == "INFO3":
                    print Tornado3
                    time.sleep(5.0)
                elif str(UserMove) == "info4" or str(UserMove) == "Info4" or str(UserMove) == "INFO4":
                    print Tornado4
                    time.sleep(5.0)
                elif str(UserMove) == "1":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "2":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "3":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "4" and Super == "Active" and not SuperUsed:
                    print(" ")
                    UseMove = True
                else:
                    print("Invalid Input, please try again.")

    # Starts the game with the character Bang selected
    elif CharacterChoice == 2:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(BangAtk) + " Defense:" + str(BangDef) + " Speed:" + str(BangSpe))
        UserSpe = BangSpe
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        print("Lets start you off with an introduction fight to help you fit in with the other heroes.")
        time.sleep(4)
        print("There is a villain calling himself Crablante who has been going around killing people, your job is to stop him.\n")
        time.sleep(4)
        ComputerHp = 100
        CompAtk = 170
        CompDef = 180
        CompSpe = 150
        CompDefBuff = 1.0
        CompAtk = 1.0
        while UserHp > 0 and ComputerHp > 0:
            Enemy = red + "Crablante" + end
            UseMove = False
            if UserHp <= 50:
                Super = "Active"
            elif UserHp > 50:
                Super = "Not Active"
            if ComputerHp <= 50 and not ComputerSuperUsed:
                ComputerMove = 3
            else:
                ComputerMove = random.randint(1, 2)
            while not UseMove:
                print ("\n\n\n")
                display_hp(UserHp, ComputerHp)
                UserMove = raw_input("\nChoose a move (Enter info1, info2, etc. for info on a specific move):\n1. Water Stream Encampment\t\t2. Abandonment\n3. Fang Interpolation\t\t4. (Super) Water Stream Rock Smashing Fist \n")
                if str(UserMove) == "info1" or str(UserMove) == "Info1" or str(UserMove) == "INFO1":
                    print (Bang1)
                    time.sleep(2.5)
                elif str(UserMove) == "info2" or str(UserMove) == "Info2" or str(UserMove) == "INFO2":
                    print (Bang2)
                    time.sleep(2.5)
                elif str(UserMove) == "info3" or str(UserMove) == "Info3" or str(UserMove) == "INFO3":
                    print (Bang3)
                    time.sleep(2.5)
                elif str(UserMove) == "info4" or str(UserMove) == "Info4" or str(UserMove) == "INFO4":
                    print (Bang4)
                    time.sleep(2.5)
                elif str(UserMove) == "1":
                    UseMove = True
                    if UserSpe >= CompSpe:
                        print("")
                        if ComputerHp > 0:
                            if ComputerMove == 1:
                                print ""
                            elif ComputerMove == 2:
                                print ""
                            elif ComputerMove == 3:
                                print ""
                        else:
                            print ""
                    elif CompSpe > UserSpe:
                        print("")
                elif str(UserMove) == "2":
                    UseMove = True
                    if UserSpe >= CompSpe:
                        print ("")
                elif str(UserMove) == "3":
                    print(" ")
                    UseMove = True
                    if (BangSpe * SpeUp) >= CompSpe:
                        ComputerHp -= combat_damage(160, AtkUp, BangAtk, CompDef, CompDefBuff)
                        print ("Bang used Fang Interpolation. It dealt " + str(combat_damage(160, AtkUp, BangAtk, CompDef, CompDefBuff)) + " damage.")
                        time.sleep(2.5)
                        if ComputerHp > 0:
                            if ComputerMove == 1:
                                UserHp -= combat_damage(120, CompAtkBuff, CompAtkBuff, BangDef, DefUp)
                                print ("Crablante used Crab Chop. It dealt " + str(combat_damage(120, CompAtkBuff, CompAtk, BangDef, DefUp)) + " damage.")
                            elif ComputerMove == 2:
                                CompDefBuff += 0.5
                                print ("Crablante started hardening his shell. His defense rose.")
                            elif ComputerMove == 3:
                                UserHp -= combat_damage(120, CompAtkBuff, CompAtkBuff, BangDef, DefUp)
                                print ("Crablante used The Sea's Guillotine. It dealt " + str(combat_damage(190, CompAtk, CompAtkBuff, BangDef, DefUp)) + " damage.")
                                ComputerSuperUsed = True
                        else:
                            print ("You defeated Crablante!")
                    elif CompSpe > UserSpe:
                        print("")
                elif str(UserMove) == "4" and Super == "Active" and not SuperUsed:
                    print(" ")
                    UseMove = True
                    if (BangSpe * SpeUp) >= CompSpe:
                        ComputerHp -= combat_damage(280, AtkUp, BangAtk, CompDef, CompDefBuff)
                        print (Character + " used Water Stream Rock Smashing Fist. It dealt " + combat_damage(280, AtkUp, BangAtk, CompDef, CompDefBuff) + " damage.")
                        time.sleep(4)
                        if ComputerHp > 0:
                            if ComputerMove == 1:
                                print ""
                            elif ComputerMove == 2:
                                print ""
                            elif ComputerMove == 3:
                                print ""
                        else:
                            print
                    elif CompSpe > UserSpe:
                        print""
                else:
                    print("Invalid Input, please try again.")
                time.sleep(2.5)

    # Starts the game with the character Genos selected
    elif CharacterChoice == 3:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(GenosAtk) + " Defense:" + str(GenosDef) + " Speed:" + str(GenosSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        print("Lets start you off with an introduction fight to help you fit in with the other heroes.")
        time.sleep(4)
        print("There is a villain calling himself Crablante who has been going around killing people, your job is to stop him.\n")
        time.sleep(4)
        ComputerHp = 100
        while UserHp > 0 and ComputerHp > 0:
            Enemy = red + "Crablante" + end
            UseMove = False
            if UserHp <= 50:
                Super = "Active"
            elif UserHp > 50:
                Super = "Not Active"
            if ComputerHp <= 50 and not ComputerSuperUsed:
                ComputerMove = 4
            else:
                ComputerMove = computer_move_funct()
            while not UseMove:
                print "\n\n\n"
                display_hp(UserHp, ComputerHp)
                UserMove = raw_input("\nChoose a move (Enter info1, info2, etc. for info on a speific move):\n1. Water Stream Encampment\t\t2. Abandonment\n3. Fang Interpolation\t\t4. (Super) Water Stream Rock Smashing Fist \n")
                if str(UserMove) == "info1" or str(UserMove) == "Info1" or str(UserMove) == "INFO1":
                    print Genos1
                elif str(UserMove) == "info2" or str(UserMove) == "Info2" or str(UserMove) == "INFO2":
                    print Genos2
                elif str(UserMove) == "info3" or str(UserMove) == "Info3" or str(UserMove) == "INFO3":
                    print Genos3
                elif str(UserMove) == "info4" or str(UserMove) == "Info4" or str(UserMove) == "INFO4":
                    print Genos4
                elif str(UserMove) == "1":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "2":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "3":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "4" and Super == "Active" and not SuperUsed:
                    print(" ")
                    UseMove = True
                else:
                    print("Invalid Input, please try again.")

    # Starts the game with the character Metal Bat selected
    elif CharacterChoice == 5:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(MetalBatAtk) + " Defense:" + str(MetalBatDef) + " Speed:" + str(MetalBatSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        print("Lets start you off with an introduction fight to help you fit in with the other heroes.")
        time.sleep(4)
        print("There is a villain calling himself Crablante who has been going around killing people, your job is to stop him.\n")
        time.sleep(4)
        ComputerHp = 100
        while UserHp > 0 and ComputerHp > 0:
            Enemy = red + "Crablante" + end
            UseMove = False
            if UserHp <= 50:
                Super = "Active"
            elif UserHp > 50:
                Super = "Not Active"
            if ComputerHp <= 50 and not ComputerSuperUsed:
                ComputerMove = 3
            else:
                ComputerMove = 0
            while not UseMove:
                print "\n\n\n"
                display_hp(UserHp, ComputerHp)
                UserMove = raw_input("\nChoose a move (Enter info1, info2, etc. for info on a speific move):\n1. Water Stream Encampment\t\t2. Abandonment\n3. Fang Interpolation\t\t4. (Super) Water Stream Rock Smashing Fist ")
                if str(UserMove) == "info1" or str(UserMove) == "Info1" or str(UserMove) == "INFO1":
                    print MetalBat1
                elif str(UserMove) == "info2" or str(UserMove) == "Info2" or str(UserMove) == "INFO2":
                    print MetalBat2
                elif str(UserMove) == "info3" or str(UserMove) == "Info3" or str(UserMove) == "INFO3":
                    print MetalBat3
                elif str(UserMove) == "info4" or str(UserMove) == "Info4" or str(UserMove) == "INFO4":
                    print MetalBat4
                elif str(UserMove) == "1":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "2":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "3":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "4" and Super == "Active" and not SuperUsed:
                    print(" ")
                    UseMove = True
                else:
                    print("Invalid Input, please try again.")

    # Starts the game with the character Speed-o'-Sound Sonic selected
    elif CharacterChoice == 4:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(SonicAtk) + " Defense:" + str(SonicDef) + " Speed:" + str(SonicSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        print("Lets start you off with an introduction fight to help you fit in with the other heroes.")
        time.sleep(4)
        print("There is a villain calling himself Crablante who has been going around killing people, your job is to stop him.\n")
        time.sleep(4)
        ComputerHp = 100
        while UserHp > 0 or ComputerHp > 0:
            Enemy = red + "Crablante" + end
            UseMove = False
            if UserHp <= 50:
                Super = "Active"
            elif UserHp > 50:
                Super = "Not Active"
            display_hp(UserHp, ComputerHp)
            if ComputerHp <= 50 and not ComputerSuperUsed:
                ComputerMove = 4
            else:
                ComputerMove = computer_move_funct()
            while not UseMove:
                print "\n\n\n"
                display_hp(UserHp, ComputerHp)
                UserMove = raw_input("\nChoose a move (Enter info1, info2, etc. for info on a speific move):\n1. Water Stream Encampment\t\t2. Abandonment\n3. Fang Interpolation\t\t4. (Super) Water Stream Rock Smashing Fist ")
                if str(UserMove) == "info1" or str(UserMove) == "Info1" or str(UserMove) == "INFO1":
                    print Sonic1
                elif str(UserMove) == "info2" or str(UserMove) == "Info2" or str(UserMove) == "INFO2":
                    print Sonic2
                elif str(UserMove) == "info3" or str(UserMove) == "Info3" or str(UserMove) == "INFO3":
                    print Sonic3
                elif str(UserMove) == "info4" or str(UserMove) == "Info4" or str(UserMove) == "INFO4":
                    print Sonic4
                elif str(UserMove) == "1":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "2":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "3":
                    print(" ")
                    UseMove = True
                elif str(UserMove) == "4" and Super == "Active" and not SuperUsed:
                    print(" ")
                    UseMove = True
                else:
                    print("Invalid Input, please try again.")

    # Starts the game with the character Mumen Rider selected
    elif CharacterChoice == 7:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(MumenRiderAtk) + " Defense:" + str(MumenRiderDef) + " Speed:" + str(MumenRiderSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()

    # Starts the game with the character Garou selected
    elif CharacterChoice == 6:
        print("You Chose: " + Character)
        print("Stats- Attack:" + str(GarouAtk) + " Defense:" + str(GarouDef) + " Speed:" + str(GarouSpe))
        time.sleep(8)
        print("\n\n\n\n\n\n\n\n")
        loading()
    print "You Won!"
