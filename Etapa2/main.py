import os
import shutil
from Graph import Graph as g




# graph = g.Graph(now)
# print(graph.Dijkstra(1))
# print(graph.BellmanFord(1))
# print(graph.DijkstraOptimised(1))

# os.system('python inputGenerator.py')


path = "./out"

# delete the old out
try:
    shutil.rmtree(path)
except OSError:
    print("Can t delate the previous directory")


# create new empty folder
try:
    os.mkdir(path)
except OSError:
    print("Can t create the directory %s" %path)

for i in range(0, 11):
    readFile = "./in/generatedInput" + str(i) + ".txt"
    f = open(readFile, "r")
    vertices, edges, startNode = f.readline().split(" ")
    vertices = int(vertices)
    edges = int(edges)
    startNode = int(startNode)
    graph = {}
    for j in range(1, vertices + 1):
        graph[j] = {}
    for j in range(1, edges + 1):
        start, end, weight = f.readline().split(" ")
        start = int(start)
        end = int(end)
        weight = int(weight)
        graph[start][end] = weight
    f.close()

    def utils(dictionary, start):
        newline = "\n"
        result = ""
        for keys in dictionary:
            result += str(keys) + " " + str(dictionary[keys]) + newline
        return result

    f = open(path + "/DijkstraTest" + str(i) + ".txt", "w")
    f.write(utils(g.Graph(graph).Dijkstra(startNode), startNode))
    f.close()

    f = open(path + "/BellmanFordTest" + str(i) + ".txt", "w")
    f.write(utils(g.Graph(graph).BellmanFord(startNode), startNode))
    f.close()

    f = open(path + "/DijkstraOptimisedTest" + str(i) + ".txt", "w")
    f.write(utils(g.Graph(graph).DijkstraOptimised(startNode), startNode))
    f.close()

