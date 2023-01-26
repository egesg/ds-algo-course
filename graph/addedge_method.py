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
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): # if v1 and v2 both exist, then I can create the edge between two
            self.adj_list[v1].append(v2) # append method
            self.adj_list[v2].append(v1)
            return True
        return False # if either of them does not exist -> return False

my_graph = Graph()
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.print_graph()
# 1 : []
# 2 : []
my_graph.add_edge(1,2)
my_graph.print_graph()
# 1 : [2]
# 2 : [1]


'''
{
    1:[],
    2:[]
}


# to connect these 2 vertices
{
    1:[2],
    2:[1]
}
'''

