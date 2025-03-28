def getProbabilities(userStats,opponentStats,cooldownWeight):
    #static variables
    uSwordAttack = userStats[0]
    uSwordDefense = userStats[1]
    uShieldAttack = userStats[2]
    uShieldDefense = userStats[3]
    uMagicAttack = userStats[4]
    uMagicDefense = userStats[5]
    oSwordAttack = opponentStats[0]
    oSwordDefense = opponentStats[1]
    oShieldAttack = opponentStats[2]
    oShieldDefense = opponentStats[3]
    oMagicAttack = opponentStats[4]
    oMagicDefense = opponentStats[5]
    
    # starting health and armor
    oStartingHealth = opponentStats[6]
    oStartingArmor = opponentStats[7]
    uStartingHealth = userStats[6]
    uStartingArmor = userStats[7]

    # current health and armor

    
    # move cooldowns
    uSwordCooldown = 3
    uShieldCooldown = 3
    uMagicCooldown = 3
    oSwordCooldown = 3
    oShieldCooldown = 3
    oMagicCooldown = 3

    # maximum values
    maxAttack = max(uSwordAttack, oSwordAttack, uShieldAttack, oShieldAttack, uMagicAttack, oMagicAttack)
    maxArmorRepair = max(uSwordDefense, oSwordDefense, uShieldDefense, oShieldDefense, uMagicDefense, oMagicDefense)

    # formula 1: effectiveness of moves
    swordEffectivenessArr = [uSwordAttack, uSwordDefense]
    shieldEffectivenessArr = [uShieldAttack, uShieldDefense]
    magicEffectivenessArr = [uMagicAttack, uMagicDefense]

    swordEffect = getBaseMoveEffectiveness(swordEffectivenessArr, maxAttack, maxArmorRepair)
    shieldEffect = getBaseMoveEffectiveness(shieldEffectivenessArr, maxAttack, maxArmorRepair)
    magicEffect = getBaseMoveEffectiveness(magicEffectivenessArr, maxAttack, maxArmorRepair)

    # formula 2: move cooldowns
    #maximum values

    
    while uStartingHealth > 0 and oStartingHealth > 0:
        calculateSwordProbability(uSwordAttack, uSwordDefense, oSwordAttack, oSwordDefense,
                                  uSwordCooldown, oSwordCooldown, maxAttack, maxArmorRepair)
        calculateShieldProbability(uShieldAttack, oShieldDefense, uShieldCooldown, oShieldCooldown)
        calculateMagicProbability(uMagicAttack, oMagicDefense, uMagicCooldown, oMagicCooldown)

def getBaseMoveEffectiveness(effectivenessArr, maxAttack, maxArmorRepair):
    attack = effectivenessArr[0]
    armorRepair = effectivenessArr[1]

    effect = (attack + armorRepair) / (maxAttack + maxArmorRepair)
    return effect