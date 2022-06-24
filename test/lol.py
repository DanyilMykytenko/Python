import sys
import time
import maze
from colorama import init
from colorama import Fore, Back, Style
import os

init()

map = maze.generateMaze(20,20)

def showMap():
    os.system("cls")
    print()
    for row in map:
        for item in row:
            if item == 'c':
                print (Fore.GREEN + item + Fore.WHITE, end="")
            if item == 'w':
                print (Fore.RED + item + Fore.WHITE, end="")
            if item == '*':
                print (Fore.YELLOW + item + Fore.WHITE, end="")
            if item == 'e':
                print ('e', end="")
        print()

def action(x, y):
    if map[y][x] == 'e':
        print("FINISHED!")
        sys.exit(0)
    if map[x][y] == 'c':
        map[x][y] = '*'
        time.sleep(0.3)
        AI(x,y)

def AI(x, y):
    showMap()
    action(x-1, y)
    action(x+1, y)
    action(x, y-1)
    action(x, y+1)

#AI(1,1)

showMap()

print ("Set exit: ")
exitX = int(input("X: "))
exitY = int(input("Y:" ))
map[exitY][exitX] = 'e'

showMap()

print ("Set entrance: ")
entX = int(input("X: "))
entY = int(input("Y:" ))
map[entY][entX] = 'c'

AI(entX,entY)
print ("NO EXIT :(")
