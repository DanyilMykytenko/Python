from random import randint
import os

mapSizeX = 30
mapSizeY = 10

map = []

def getItem(id):
    match(id):
        case 1: return "s"
        case 2: return "t"
        case _: return "."

def log(message):
    print ("[INFO]: " + str(message))

def initLevel():
    level = []
    for X in range(0, mapSizeX):
        level.append(getItem(randint(0, 10)))
    return level

def initMap():
    log ("Initializing map started (X: " + str(mapSizeX) + ", Y:" + str(mapSizeY))
    for Y in range(0, mapSizeY):
        log ("Preparing level " + str(Y) + "...")
        map.append(initLevel())
    log ("Map generation done!")

def showMap():
    os.system('cls')
    print()
    for row in map:
        for item in row:
            print (item, end="")
        print()

initMap()
showMap()
