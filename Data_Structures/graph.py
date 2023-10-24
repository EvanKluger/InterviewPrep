class Graph:

    def __init__(self):

        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        return
    
    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append((vertex2, weight))
        return
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for key in self.adj_list:
                self.adj_list[key] = [(v, w) for v, w in self.adj_list[key] if v != vertex]
        return

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1] = [(v, w) for v, w in self.adj_list[vertex1] if v != vertex2]
        return
        
    def get_neighbors(self, vertex):
        arr = []
        if vertex in self.adj_list:
            for edge in self.adj_list[vertex]:
                 arr.append(edge[0])
        return arr

    def has_vertex(self, vertex):
        return vertex in self.adj_list
    
    def has_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            for edge in self.adj_list[vertex1]:
                if edge[0] == vertex2:
                    return True
        return False
    
    def display(self):
        for key, value in self.adj_list.items():
            print(key, value)
        return