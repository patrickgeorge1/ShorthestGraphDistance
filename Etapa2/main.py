from Graph import Graph as g


now = {
    1: {2: 2, 3: 4},
    2: {3: 1, 4: 7},
    3: {5: 3, 1: 2},
    4: {6: 1},
    5: {4: 2, 6: 6},
    6: {},
}


graph = g.Graph(now)
print(graph.Dijkstra(1))
print(graph.BellmanFord(1))
print(graph.DijkstraOptimised(1))