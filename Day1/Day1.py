elfArray = []
calorieArray = []
with open("input.txt") as inputFile:
    lines = inputFile.readlines()
    for l in lines:
        if (l != '\n'):
            calorieArray.append(int(l.strip()))
        else:
            x = sum(calorieArray)
            elfArray.append(x)
            calorieArray.clear()
    print (max(elfArray))

    # Get top 3
    sortedArray = sorted(elfArray, reverse=True)
    sum3 = sortedArray[0] + sortedArray[1] + sortedArray[2]
    print(sum3)