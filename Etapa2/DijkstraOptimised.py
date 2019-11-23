from Graph import Graph as g
import sys


path = sys.argv[1]
f = open(path, "r")
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


print(utils(g.Graph(graph).DijkstraOptimised(startNode), startNode))
