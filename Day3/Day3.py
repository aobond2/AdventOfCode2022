import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index + 27

prioritiesSum = 0

def part_one():
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        ParseLine(l)
    print (prioritiesSum)

def ParseLine(line):
    global prioritiesSum
    line = line.strip()
    firstPart, secondPart = line[:len(line)//2], line[len(line)//2:]
    # print (firstPart, secondPart)
    sameLetters = list(set(firstPart) & set(secondPart))
    for l in sameLetters:
        prioritiesSum += (values[l])

def main() -> None:
    part_one()

if __name__ == "__main__":
    main()