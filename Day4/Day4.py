newStringArray = []
def part_one():
    with open("input.txt") as inputFile:
        lines = inputFile.readlines()
    for l in lines:
        l = (l.strip())
        stringArray = l.split(",")
        getFullRange(stringArray)

def getFullRange(strArray):
    for s in strArray:
        newLine = []
        num = s.split("-")
        splittedRange = range(int(num[0]),int(num[1])+1)
        for sr in splittedRange:
            newLine.append(sr)
        print (newLine)
    
def main() -> None:
    part_one()

if __name__ == "__main__":
    main()