import unittest

class TopologicalSort:

    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.nodes = self.flattenGraph()
        self.topOrder = []

    def flattenGraph(self):
        nodes = set()
        for key, value in self.graph.items():
            nodes.add(key)
            for v in value:
                nodes.add(v)
        return list(nodes)
    
    def hasNeighbors(self, node):
        return True if self.graph.get(node) else False

    '''
    Wrapper function on DFS
    Visit each node
    Skip if the node has been visited
    Apply DFS to return topological order
    '''
    def apply(self):
        for node in self.nodes:
            if node in self.visited:
                continue
            else:
                self.DFS(node)
        return self.topOrder

    # Main func that does the work
    def DFS(self, node):
        neighbors = self.graph.get(node) or []

        # Dive down to each child (neighbor) node
        for n in neighbors:
            if self.hasNeighbors(n):
                self.DFS(n)
            else:
                # No neighbors, then mark visted and left append in topological order
                self.visited.add(n)
                self.topOrder = [n] + self.topOrder
        
        # Backtrack the parent node
        self.visited.add(node)
        self.topOrder = [node] + self.topOrder

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "E": ["F"]
        }
        self.tps = TopologicalSort(self.graph)
        return super().setUp()

    def test_flattenGraph(self):
        self.assertTrue(all(map(lambda node: node in ["A", "B", "C", "D", "E", "F"], self.tps.flattenGraph())))

    def test_DFS(self):
        self.tps.DFS("B")
        self.assertEqual(self.tps.topOrder, ["B", "E", "F", "D"])

    def test_hasNeighbors(self):
        self.assertTrue(self.tps.hasNeighbors("A"))
        self.assertFalse(self.tps.hasNeighbors("C"))

    def test_apply(self):
        self.tps.topOrder = [] # reset the result from test_DFS func
        result = self.tps.apply()
        self.assertEqual(result, ['A', 'C', 'B', 'E', 'F', 'D'])

if __name__ == '__main__':
    unittest.main()
        