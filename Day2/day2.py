scoreArray = []

def ParseLine(line):
    line = line.strip()
    handInput = line.split(" ")
    doCalculation(handInput)

def doCalculation(arrayInput):
    Me = (arrayInput[0])
    You = (arrayInput[1])
    # Draw
    if (Me == You):
        draw()
    # Win
    # Lose

def win():
    print ("")

def draw():
    print ("")

def lost():
    print ("")

with open("input.txt") as inputFile:
    lines = inputFile.readlines()
    for l in lines:
        ParseLine(l)