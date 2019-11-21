

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def add_vertice(self, start, end):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append(end)
        if end not in self.graph:
            self.graph[end] = []

    # Dijkstra
    def Dijkstra(self, start):

        # aduce urmatorul copil de verificat
        def findNextDistance(distances, visited):
            good = next(iter(distances))
            minDist = distances[good]
            if good in visited: minDist = float("inf")

            for next_connection in distances:
                if next_connection not in visited and distances[next_connection] <= minDist:
                    good = next_connection
                    minDist = distances[good]
            if good not in visited: return good
            return None

        # relaxez distantele
        def relax(child, distances):
            for connection in self.graph[child]:
                if distances[child] + self.graph[child][connection] < distances[connection]:
                    distances[connection] = distances[child] + self.graph[child][connection]

        visited = set()
        distances = {k:float("inf") for k in self.graph}

        distances[start] = 0
        visited.add(start)
        relax(start, distances)
        next_connection = findNextDistance(distances, visited)

        while (next_connection is not None and next_connection != float("inf")):
            visited.add(next_connection)
            relax(next_connection, distances)
            next_connection = findNextDistance(distances, visited)
        return distances


    # BellmanFord
    def BellmanFord(self, start):

        visited = set()
        distances = {k:float("inf") for k in self.graph}
        distances[start] = 0



        for step in range(1, len(distances) + 1):
            relaxed = False
            for vertex in distances.keys():
                for child in self.graph[vertex]:
                    if distances[vertex] + self.graph[vertex][child] < distances[child]:
                        distances[child] = distances[vertex] + self.graph[vertex][child]
                        relaxed = True
            if relaxed is False: break

        return distances

    # Dial Algorithm = Dijkstra Algorithm(optimised)
    def DijkstraOptimised(self, start):
        # Find the maximum weight
        def findMaxWeight():
            maxim = -float("inf")
            for vertex in self.graph:
                for child in self.graph[vertex]:
                    if self.graph[vertex][child] > maxim: maxim = self.graph[vertex][child]
            return maxim

        # Create a new set of empty buckets
        def emptyBuckets():
            buckets = []
            for i in range(findMaxWeight() * len(self.graph)):
                buckets.append(set())
            return buckets

        # Index and values from first empty bucket and values from it
        def firstValidBucket(buckets):
            firstEmptyBucketIndex = None
            firstEmptyBucket = []
            for index, bucket in enumerate(buckets):
                if len(bucket) != 0:
                    firstEmptyBucketIndex = index
                    [firstEmptyBucket.append(vertex) for vertex in bucket]
                    break
            return (firstEmptyBucketIndex, firstEmptyBucket)

        def updateBuckets(vertice, distances):
            buckets = emptyBuckets()
            for child in self.graph[vertice]:
                if distances[child] == float("inf"):
                    prevDistance = distances[vertice]
                    nextDistance = self.graph[vertice][child]
                    totalDistance = prevDistance + nextDistance
                    buckets[totalDistance].add(child)
            return buckets

        def utils(index, buckets, distances):
            if index is None: return
            vertices = buckets[index]
            for vertex in vertices:
                distances[vertex] = index
            for vertex in vertices:
                buckets = updateBuckets(vertex, distances)
                index, newVertices = firstValidBucket(buckets)
                utils(index, buckets, distances)

        buckets = emptyBuckets()
        distances = {k:float("inf") for k in self.graph}
        distances[start] = 0
        buckets[0].add(start)
        index, newVertices = firstValidBucket(buckets)
        utils(index, buckets, distances)

        return distances