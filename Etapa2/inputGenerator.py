import os
import shutil
import math
import random

path = "./in"

# delete the old in
try:
    shutil.rmtree(path)
except OSError:
    print("Can t delate the previous directory")

# create new empty folder
try:
    os.mkdir(path)
except OSError:
    print("Can t create the directory %s" %path)

def generateFileWithComplexity(complexity):
    file_content = ""
    newline = "\n"
    complexity += 1
    vertices = round(math.exp(math.sqrt(complexity)) * math.sqrt(complexity) - complexity // 2) + 2 * round(math.sqrt(math.exp(math.sqrt(complexity)) * math.sqrt(complexity) - complexity // 2))
    completeEdges = vertices * (vertices + 1) // 2
    edges = completeEdges // complexity
    if complexity > 5: edges += round(math.sqrt(vertices * (vertices + 1) // 2))
    startNode = random.randint(1, vertices)

    doNotOverride = []
    for i in range(0, vertices + 1):
        doNotOverride.append(set([i]))

    maximumSolution = random.randint(1, vertices // 2) * vertices
    allowedExtraEdges = maximumSolution + 1
    generatedNumber = 0
    file_content += str(vertices) + " " + str(edges) + " " + str(startNode) + newline

    for i in range(1, vertices + 1):
        previousNode = startNode
        if i != startNode:
            intermediateNodes = random.randint(1, vertices // 2)
            safeNodeDistance = maximumSolution // (intermediateNodes + 1)
            # print("Noduri intermediare" + str(intermediateNodes))
            if intermediateNodes == 1:
                doNotOverride[startNode].add(i)
                file_content += str(startNode) + " " + str(i) + " " + str(safeNodeDistance) + newline
                generatedNumber += 1
            else:
                randomNodes = [startNode]
                for ii in range(1, intermediateNodes):
                    previousNode = randomNodes[-1]
                    nextNode = random.randint(1, vertices)
                    while nextNode != startNode and nextNode != randomNodes[-1] and nextNode != i and nextNode not in doNotOverride[previousNode]:
                        nextNode = random.randint(1, vertices)
                    randomNodes.append(nextNode)
                    previousNode = nextNode
                randomNodes.append(i)
                previousNode = randomNodes[0]
                for i in range(1, len(randomNodes)):
                    nextNode = randomNodes[i]
                    if nextNode not in doNotOverride[previousNode]:
                        file_content += str(previousNode) + " " + str(nextNode) + " " + str(safeNodeDistance) + newline
                        generatedNumber += 1
                        doNotOverride[previousNode].add(nextNode)
                    previousNode = nextNode

    while generatedNumber < edges:
        for i in range(1, vertices + 1, random.randint(1, 4)):
            if generatedNumber == edges: break
            for j in range(vertices,  -1, -1 * random.randint(1, 3)):
                if i != j and i not in doNotOverride[j] and j != 0 and i != 0:
                    doNotOverride[j].add(i)
                    file_content += str(j) + " " + str(i) + " " + str(allowedExtraEdges + random.randint(1, 2 * complexity)) + newline
                    generatedNumber += 1
                    break
                if generatedNumber == edges: break
        if generatedNumber == edges: break
    return file_content



for i in range(0, 11):
    f = open(path + "/" + "generatedInput" + str(i) + ".txt", "w")
    f.write(generateFileWithComplexity(i))
    f.close()



