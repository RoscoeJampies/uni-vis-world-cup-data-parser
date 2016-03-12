# Read file into array of lines
def loadFile (fname):
    f = open(fname, 'r')
    data = [];
    for line in f:
        data.append(line)
    f.close()
    return data

# Split lines on split
def splitLines (line, split):
    line = line.split(split)
    return line

# Categorise line
def catLine(line):
    if (line[0] == "\n" or line[0][0] == "#"):
        return False
    elif (len(line)>4 and line[3] == "|"):
        return False
    elif (line[0][0] == "("):
        True
    else:
        return False

# process line
def processLine(line):
    date = True
    output = []
    output.append("")
    for i, val in enumerate(line):
        if (val != "" and i != 0):
            if (date):
                output[0] = " "+val
    return output


# Run Software
if __name__ == "__main__":
    fileLines = loadFile("world-cup/2010--south-africa/cup.txt")
    print(fileLines)
    for i in range(len(fileLines)):
        fileLines[i] = splitLines(fileLines[i], " ")
    print(fileLines)
    lineCat = []
    for i in range(len(fileLines)):
        lineCat.append(catLine(fileLines[i]))
    for i in range(len(lineCat)):
        if (lineCat[i]):
            print(processLine(fileLines[i]))
