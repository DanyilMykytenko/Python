from random import randint
from pynput import keyboard
import os

mapSizeX = 10
mapSizeY = 10
playerPosX = 4
playerPosY = 4

map = []
pMap = []

def log(message):
    print ("[INFO]: " + str(message))

def getItem(id):
    match(id):
        case 1: return "s"
        case 2: return "t"
        case 15: return "*"
        case _: return "."

def initLevel():
    level = []
    for X in range(0, mapSizeX):
        level.append(getItem(randint(0, 10)))
    return level

def initPlayerLevel():
    level = []
    for X in range(0, mapSizeX):
        level.append(getItem(15))
    return level

def initMap():
    log ("Initializing map started (X: " + str(mapSizeX) + ", Y:" + str(mapSizeY))
    for Y in range(0, mapSizeY):
        log ("Preparing level " + str(Y) + "...")
        map.append(initLevel())
        pMap.append(initPlayerLevel())
    log ("Map generation done!")
    updatePlayerMap()
    pMap[playerPosY][playerPosX] = '@'

def showMap():
    os.system('cls')
    print()
    for row in pMap:
        for item in row:
            print (item, end="")
        print()

def checkPossibleMove(x, y):
    try:
        return (True if map[playerPosY + y][playerPosX + x] == '.' else False)
    except IndexError:
        return False

def playerMove(offsetX, offsetY):
    global playerPosX
    global playerPosY
    if checkPossibleMove(offsetX, offsetY):
        pMap[playerPosY][playerPosX] = '.'
        playerPosY = playerPosY + offsetY
        playerPosX = playerPosX + offsetX
        updatePlayerMap()
        pMap[playerPosY][playerPosX] = '@'

def updatePlayerMap():
    global playerPosX
    global playerPosY
    try:
        for x in range (-1, 2):
            for y in range (-1, 2):
                pMap[playerPosY+y][playerPosX+x] = map[playerPosY+y][playerPosX+x]
    except IndexError:
        return False

def processMovement(x, y):
    playerMove(x, y)
    showMap()

def user_input(key):
    try:
        match(key.char):
            case "w": processMovement(0, -1)
            case "s": processMovement(0, 1)
            case "a": processMovement(-1, 0)
            case "d": processMovement(1, 0)
            case "q": return False
    except AttributeError:
        log ("Unsupported keys")

initMap()
showMap()

with keyboard.Listener(
        on_release=user_input) as listener:
    listener.join()
