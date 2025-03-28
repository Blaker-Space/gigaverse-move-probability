import statManager
import battleManager

def main():
    userStats = statManager.welcomeUserGetStats()
    opponentStats = statManager.getOpponentStats()
    battleManager.battleOpponents(userStats, opponentStats)
    statManager.checkForUpgrades(userStats)
    battleManager.checkForMoreBattles()
    

main()