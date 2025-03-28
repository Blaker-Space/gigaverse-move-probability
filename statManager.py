import os

def welcomeUserGetStats():
    print("Welcome to the Gigaverse Probability Calculator!\n")
    userStats = []
    isCurrentUser = checkForStatFile()
    
    if isCurrentUser:
        userStats = getCurrentUserStats()
    else:
        getNewUserStats()
   
def getNewUserStats():
    print("It looks like this is your first time using my calculator, so let's get started!\n")
    print("Please enter your Gigaverse stats using the following format:\n")
    print("Start with attack first, then defense for each move. Go in the order" \
            "of sword, shield, and then magic. Lastly, enter your starting health" \
            " and starting armor.\n")
    print("Example: 4,0,0,4,2,2,9,5 = 4 attack for sword, 0 defense for sword," \
            "0 attack for shield, 4 defense for shield," \
            "2 attack for magic, 2 defense for magic, 9 starting health, and 5 starting armor\n")
    userStats = updateStats(True);
       
def getCurrentUserStats():

    machineName = os.path.basename(os.path.expanduser("~"))
    filePath = fr"C:\Users\{machineName}\gigaverse-probability-calculator\userStats.txt"

    with open(filePath, 'r') as file:
        statArr = list(map(int, file.read().strip().split(",")))
        
    print((
    f"Your saved stats are:\n"
    f"\tSword attack: {statArr[0]}\n"
    f"\tSword defense: {statArr[1]}\n"
    f"\tShield attack: {statArr[2]}\n"
    f"\tShield defense: {statArr[3]}\n"
    f"\tMagic attack: {statArr[4]}\n"
    f"\tMagic defense: {statArr[5]}\n"
    f"\tStarting Health: {statArr[6]}\n"
    f"\tStarting Armor: {statArr[7]}\n"
    ))

    yesNo = input("Is this still correct? (y/n): ").strip().lower()

    while yesNo not in ['y', 'n']:
        yesNo = input("Please enter 'y' or 'n': ").strip().lower()

    if yesNo == 'n':
        statArr = updateStats(True)
    return statArr
    
def updateStats(isPlayer):
    statArr = []
    statsCorrect = False
    if isPlayer:
        print("Please enter your new stats: ")
    else:
        print("Please enter your opponent's stats: ")
    while statsCorrect != True:
        try:
            userInput = input().strip()
            enteredStats = list(map(int, userInput.split(",")))
            if len(enteredStats) != 8:
                raise ValueError("Please enter exactly 8 numbers separated by commas.")
            print((
                f"You entered:\n"
                f"\tSword attack: {enteredStats[0]}\n"
                f"\tSword defense: {enteredStats[1]}\n"
                f"\tShield attack: {enteredStats[2]}\n"
                f"\tShield defense: {enteredStats[3]}\n"
                f"\tMagic attack: {enteredStats[4]}\n"
                f"\tMagic defense: {enteredStats[5]}\n"
                f"\tStarting Health: {enteredStats[6]}\n"
                f"\tStarting Armor: {enteredStats[7]}\n"
            ))
            confirmation = input("Are these stats correct? (y/n): ").strip().lower()
            while confirmation not in ['y', 'n']:
                confirmation = input("Please enter 'y' or 'n': ").strip().lower()
            if confirmation == 'y':
                statArr = enteredStats
                statsCorrect = True
                break
            else:
                if isPlayer:
                    print("Please re-enter your stats: ")
                else:
                    print("Please re-enter your opponent's stats: ")
            
        except ValueError as e:
            print(f"Invalid input: {e}")

    uploadStats(statArr)
    return statArr

def checkForStatFile():
    # machineName is used for the file path to store user stats
    machineName = os.path.basename(os.path.expanduser("~"))
    #filePath holds the path to the user stats file
    filePath = fr"C:\Users\{machineName}\gigaverse-probability-calculator\userStats.txt"
    
    if not os.path.exists(filePath):
        return False
    else:
        return True
    
def uploadStats(statArr):
    # machineName is used for the file path to store user stats
    machineName = os.path.basename(os.path.expanduser("~"))
    #filePath holds the path to the user stats file
    filePath = fr"C:\Users\{machineName}\gigaverse-probability-calculator\userStats.txt"
    
    with open(filePath, 'w') as file:
        file.write(",".join(map(str, statArr)))

def getOpponentStats():
    opponentStats = []
    print("Please enter your opponent's stats using the same format as before:\n")
    print("Example: 4,0,0,4,2,2,9,5 = 4 attack for sword, 0 defense for sword," \
            "0 attack for shield, 4 defense for shield," \
            "2 attack for magic, 2 defense for magic, 9 starting health, and 5 starting armor\n")
    opponentStats = updateStats(False)
    return opponentStats