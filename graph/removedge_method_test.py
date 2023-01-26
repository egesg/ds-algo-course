# test the edge case

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
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D') # adding vertex D here but I am not connecting it with other vertexes
my_graph.print_graph()
# A : []
# B : []
# C : []
# D : []
my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A') 
my_graph.print_graph()
# A : ['B', 'C']
# B : ['A', 'C']
# C : ['B', 'A']
my_graph.remove_edge('A','D') # removing the edge between A and D
my_graph.print_graph()
'''
Exception has occurred: ValueError
list.remove(x): x not in list
'''
