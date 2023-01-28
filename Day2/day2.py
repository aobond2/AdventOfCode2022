scoreArray = []
scoreFinal = 0
winPoint = 6
drawPoint = 3
losePoint = 0

def ParseLine(line):
    line = line.strip()
    handInput = line.split(" ")
    doCalculation(handInput)

def doCalculation(arrayInput):
    Me = (arrayInput[0])
    You = (arrayInput[1])
    # Rock
    if (Me == "A"):
        actionPoint = 1
        if (You == "X"):
            draw(actionPoint)
        elif (You == "Y"):
            lost(actionPoint)
        elif (You == "Z"):
            win(actionPoint)
    # Paper
    if (Me == "B"):
        actionPoint = 2
        if (You == "X"):
            win(actionPoint)
        elif (You == "Y"):
            draw(actionPoint)
        elif (You == "Z"):
            lost(actionPoint)
    # Scissor
    if (Me == "C"):
        actionPoint = 3
        if (You == "X"):
            lost(actionPoint)
        elif (You == "Y"):
            win(actionPoint)
        elif (You == "Z"):
            draw(actionPoint)

def win(ap):
    global scoreFinal
    score = winPoint + ap
    scoreFinal += score
    print(score)
    scoreArray.append(score)

def draw(ap):
    global scoreFinal
    score = drawPoint + ap
    print(score)
    scoreArray.append(score)
    scoreFinal += score

def lost(ap):
    global scoreFinal
    score = losePoint + ap
    scoreArray.append(score)
    scoreFinal += score

def sumA():
    s = sum(scoreArray)
    print (s)
    print (scoreFinal)

def part_one():
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        ParseLine(l)
    sumA()

def main() -> None:
    part_one()

if __name__ == "__main__":
    main()