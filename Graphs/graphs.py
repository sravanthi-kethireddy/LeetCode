graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
import copy
class Graph:
    def generateEdges(self, graph):
        self.edges = []
        self.graph = graph
        for (k,v) in self.graph.items():
            self.edges.extend(k+i for i in v if (k+i)[::-1] not in self.edges)
        print(self.edges)
        return self.edges
    
    def findPath(self, graph):
        self.graph = graph
        

obj = Graph()
obj.generateEdges(graph)