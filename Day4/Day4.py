def part_one():
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        l = (l.strip())
        stringArray = l.split(",")
        getFullRange(stringArray)
        print (stringArray)

def getFullRange(strArray):
    for s in range(len(strArray)):
        fullRange = []
        num = strArray[s].split("-")
        splittedRange = range(int(num[0]),int(num[1])+1)
        for a in range(len(splittedRange)):
            fullRange.append(splittedRange[a])
        strArray[s] = fullRange
    
def main() -> None:
    part_one()

if __name__ == "__main__":
    main()