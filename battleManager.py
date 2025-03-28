import probabilities
import statManager

def battleOpponents(userStats, opponentStats):
    stillAlive = True
    # weight variables (variables that affect the weight of different factors in the game)
    weaponCooldownWeight = 0.7
    # current stats for user including buffs in dungeon
    dungeonStats = userStats
    # while our user's health is greater than 0
    while stillAlive:
        stillAlive, dungeonStats = battleOpponent(dungeonStats, opponentStats)
        
        if stillAlive:
            opponentStats = statManager.getOpponentStats()

def battleOpponent(userStats, opponentStats):
    # while neither the user nor the opponent is dead
    while userStats[6] > 0 and opponentStats[6] > 0:
        probArray = getProbabilities(userStats, opponentStats, weaponCooldownWeight)
        giveProbabilities(probArray)
        userStats = getPlayResults()
    if (userStats[6] < 0):
        return False, userStats
    else:
        userStats = checkForBuffs(userStats)
        return True, userStats

def checkForBuffs(userStats):
    printf("You won! please enter the number corresponding to what you have buffed:\n")
    return userStats