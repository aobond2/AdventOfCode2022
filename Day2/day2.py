def ParseLine(line):
    line = line.strip()
    handInput = line.split(" ")
    print(handInput)
with open("input.txt") as inputFile:
    lines = inputFile.readlines()
    for l in lines:
        ParseLine(l)