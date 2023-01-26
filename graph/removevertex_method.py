class Graph:
    def __init__(self) -> None:
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    
    def remove_vertex(self,vertex):
        # before removing vertex, I have to remove all the edges (inefficent)
        if vertex in self.adj_list.keys(): # "vertex" I want to remove
            for other_vertex in self.adj_list[vertex]: # "other_vertex" is that may have an edge with the "vertex" that I want to remove from the graph
                self.adj_list[other_vertex].remove(vertex) # remove "vertex" from the list of edges of the "other_vertex"
            del self.adj_list[vertex] # once I am done with looping through the list of edges, I can delete the vertex itself
            return True
        return False # if the vertex is not in the adj_list.keys() -> return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.print_graph()
# A : []
# B : []
# C : []
# D : []
my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D') 
my_graph.print_graph()
# A : ['B', 'C', 'D']
# B : ['A', 'D']
# C : ['A', 'D']
# D : ['A', 'B', 'C']
my_graph.remove_vertex('D')
my_graph.print_graph()
# A : ['B', 'C']
# B : ['A']
# C : ['A']

