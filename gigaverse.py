import os

def main():
    userStats = welcomeUserGetStats();
    #get stats for current opponent
    #get highest probability play(userStats, opponentStats)
    #output probabilities of each play


def welcomeUserGetStats():
    print("Welcome to the Gigaverse Probability Calculator!")
    isCurrentUser = checkForStatFile()
    if isCurrentUser:
        getCurrentUserStats()
    else:
        getNewUserStats()
    getOpponentStats()




    if os.path.exists(filePath):
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
        ))
        yesNo = input("Is this still correct? (y/n): ").strip().lower()
        while yesNo not in ['y', 'n']:
            yesNo = input("Please enter 'y' or 'n': ").strip().lower()
        if yesNo == 'n':
            statArr = getStats("current")
            return statArr
        elif yesNo == 'y':
            return statArr
        
    else:
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        statArr = getStats("new")
        with open(filePath, 'w') as file:
            file.write(",".join(map(str, statArr)))
        print(f"Stats saved to file: {filePath}")
        return statArr
        

def getCurrentUserStats(playerType):
    yesNo = 'n'
    user_stats = []

    while yesNo == 'n':
        promptForStats(playerType)

        user_stats = input("Please enter your stats: ").strip()
        print((
            f"You entered:\n"
            f"\tSword attack: {user_stats[0]}\n"
            f"\tSword defense: {user_stats[1]}\n"
            f"\tShield attack: {user_stats[2]}\n"
            f"\tShield defense: {user_stats[3]}\n"
            f"\tMagic attack: {user_stats[4]}\n"
            f"\tMagic defense: {user_stats[5]}\n"
        ))
        yesNo = input("Is this correct? (y/n): ").strip().lower()
        while yesNo not in ['y', 'n']:
            yesNo = input("Please enter 'y' or 'n': ").strip().lower()
    return user_stats.split(",")
    
    
def promptForStats(playerType):

    if playerType == 'new':
        print("Please enter your Gigaverse stats using the following format:\n")
        print("Start with attack first, then defense for each move. Go in the order" \
            "of sword, shield, and then magic.")
        print("Example: 4,0,0,4,2,2 = 4 attack for sword, 0 defense for sword," \
            "0 attack for shield, 4 defense for shield," \
            "2 attack for magic, and 2 defense for magic.\n")
        
    # if this is a current player, give abbreviated format
    elif playerType == 'current':
        print("Please enter your updated Gigaverse stats (sword atk, sword def, shield atk, etc.).\n")
    
    # if not new or current, give error message
    else:
        print("Error: playerType not recognized. Please contact support.")
        return None

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
main()