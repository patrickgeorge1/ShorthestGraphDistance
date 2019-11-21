class Constant:
    def __init__(self):
        graph1 = {
            1: {2: 2, 3: 4},
            2: {3: 1, 4: 7},
            3: {5: 3},
            4: {6: 1},
            5: {4: 2, 6: 6},
            6: {},
        }
        self.graph = {1: graph1}

    def getGraph(self, x):
        if x in self.graph:
            return self.graph[x]
        return None