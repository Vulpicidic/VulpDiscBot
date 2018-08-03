import random

# returns list of usable commands.
def getHelp():
    listOfCommands = ["!help -> Gives a list of commands.","!coin -> Flips a coin and returns either heads or tails.","!roll (amountOfDice) d(sidesOfDice) -> rolls specified amount of rolls with specified amount of sides.\n\t Ex. \"!roll 4 d20\" would roll 4 D20's and return [1,20] for each roll."]
    return convertListToVerticalString(*listOfCommands)

# flips a coin and returns either heads or tails
def getCoinFlip():
    return random.choice(['Heads','Tails'])

# Rolls specified amount of dice with specified number of sides each, returns String with rolls separated by whitespace
# example: !roll 2 D6 -> rolls 2 6-sided dice
def getDiceRoll(*args):
    diceRolls = list()
    if checkDiceRoll(args) == True:
        for i in range(int(args[0])): #for every roll
            diceRolls.append(random.randint(1, int(args[1][1:]))) #append a random number between 1 & amount of sides
    else: return ('Invalid Input')
    return ('Your dice rolls are:' + '\n' + (diceRolls))

def checkDiceRoll(message):
    try:
        numCheck = int(message[0]) + int(message[1][1:])
    except ValueError: return False
    if (((message[1][0]) == 'd') and (int(message[1][1:]) > 0)) and (int(message[0]) > 0):
        return True
    else: return False

def convertListToVerticalString(*message):
    convertedString = ""
    for i in range(len(message)):
        convertedString = (convertedString + "\n" + str(message[i]))
    return convertedString
