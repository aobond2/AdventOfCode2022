import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

prioritiesSum = 0
threeElfArray = []

def part_one():
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        ParseLine(l)
    print (prioritiesSum)

def part_two():
    global threeElfArray
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        if (len(threeElfArray) <= 2):
            threeElfArray.append(l)
            checkThreeInput()
    
    print(prioritiesSum)

def checkThreeInput():
    global prioritiesSum
    global threeElfArray
    if (len(threeElfArray) == 3):
        sameLetters = list(set(threeElfArray[0].strip()) & set(threeElfArray[1].strip()) & set(threeElfArray[2].strip()))
        for l in sameLetters:
            prioritiesSum += (values[l])
        threeElfArray.clear()

def ParseLine(line):
    global prioritiesSum
    line = line.strip()
    firstPart, secondPart = line[:len(line)//2], line[len(line)//2:]
    sameLetters = list(set(firstPart) & set(secondPart))
    for l in sameLetters:
        prioritiesSum += (values[l])

def main() -> None:
    #part_one()
    part_two()

if __name__ == "__main__":
    main()