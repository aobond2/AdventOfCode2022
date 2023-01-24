elfArray = []
calorieArray = []
with open("input.txt") as inputFile:
    lines = inputFile.readlines()
    for l in lines:
        if (l != '\n'):
            calorieArray.append(int(l.strip()))
            continue
        else:
            x = sum(calorieArray)
            elfArray.append(x)
            calorieArray.clear()
    print (max(elfArray))