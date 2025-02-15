import networkx as nx
import matplotlib.pyplot as plt

class Vertex:
    def __init__(self, id, homeTeam=None, guestTeam=None):
        self.id = id 
        self.homeTeam = homeTeam
        self.guestTeam = guestTeam
        self.neighbors = list[int]()
        self.color = None

class Graph:
    def __init__(self):
        self.nodes = list[Vertex]()
        self.nodes_by_order = list[Vertex]()
        self.visual_graph = nx.Graph()
        self.teams = ["DFC", "TFC", "AFC", "LFC", "FFC", "OFC", "CFC"]
        self.total_colors = [
            "red",
            "blue",
            "green",
            "yellow",
            "purple",
            "orange",
            "pink",
            "brown",
            "gray",
            "violet",
            "lightblue",
            "cyan",
            "magenta",
            "maroon", 
        ]
        self.rounds = [list() for _ in range(14)]

    def draw_graph(self):
        colors = [None] * (len(self.nodes) )

        for round in self.rounds:
            for match in round:
                colors[match.id] = self.total_colors[match.color]
        for i  in range(14):
            colors[i] = "white" 

        colors = [color if color is not None else 'gold' for color in colors]

        pos = nx.circular_layout(self.visual_graph)
        nx.draw(self.visual_graph, pos, with_labels=True, node_color=colors[0:], edge_color = "black", node_size = 200, font_size = 12)
        plt.show()

        


    def build(self):
        for i in range(14):
            self.nodes.append(Vertex(id = i))

        id = len(self.nodes)
        for homeTeam in self.teams:
            for guestTeam in self.teams:
                if(homeTeam == guestTeam):
                    continue
                self.nodes.append(Vertex(id, homeTeam, guestTeam))
                id+=1
        self.setRestrictions()

        sorted_by_id = list(self.nodes)

        sorted_by_id = sorted(sorted_by_id, key=lambda x: len(x.neighbors), reverse = True)
        sorted_by_id = [vertex for vertex in sorted_by_id if vertex.id < 14] + [vertex for vertex in sorted_by_id if vertex.id >=14]  

        self.nodes_by_order = sorted_by_id

    def setRestrictions(self):
        for(i) in range(14):
            for j in range(14):
                if(i==j):
                    continue
                self.addRestriction([i], [j])

        for i in range(len(self.nodes)):

            if((self.nodes[i].homeTeam, self.nodes[i].guestTeam) == ("DFC", "CFC")):
                self.addRestriction([i], [0, 13])
            if((self.nodes[i].homeTeam, self.nodes[i].guestTeam) == ("LFC", "FFC")):
                self.addRestriction([i], [6, 12])
            if((self.nodes[i].homeTeam, self.nodes[i].guestTeam) == ("OFC", "LFC")):
                self.addRestriction([i], [9, 10])
            if((self.nodes[i].homeTeam, self.nodes[i].guestTeam) == ("AFC", "FFC")):
                self.addRestriction([i], [11, 12])
            if((self.nodes[i].homeTeam, self.nodes[i].guestTeam) == ("CFC", "TFC")):
                self.addRestriction([i], [1, 2])

            for j in range(i+1, len(self.nodes)):
                if((self.nodes[i].homeTeam, self.nodes[j].homeTeam) == ("TFC", "OFC")):
                    self.addRestriction([i], [j])
                if((self.nodes[i].homeTeam, self.nodes[j].homeTeam) == ("AFC", "FFC")):
                    self.addRestriction([i], [j])

            for j in range(i+1, len(self.nodes)):
                if(
                    self.nodes[i].homeTeam in [self.nodes[j].homeTeam, self.nodes[j].guestTeam] or 
                    self.nodes[i].guestTeam in [self.nodes[j].homeTeam, self.nodes[j].guestTeam]  
                ):
                    self.addRestriction([i], [j])

    def addRestriction(self, _from: list[int], _to: list[int]):
        for i in _from:
            for j in _to:
                self.nodes[i].neighbors.append(j)
                self.nodes[j].neighbors.append(i)
                self.visual_graph.add_edge(i, j)
    
    def canColor(self, vertex: Vertex, color: int):
        for nbr in vertex.neighbors:
            if(self.nodes[nbr].color == color):
                return False
        return True


    def coloring(self, index):
        if (index== len(self.nodes)):
            return True
        
        for color in range(14):
            if (self.canColor(self.nodes_by_order[index], color)):
                self.nodes_by_order[index].color = color 
                if (self.coloring(index+1)):
                    return True
                self.nodes_by_order[index].color = None

        return False 
                


        

    def solve(self):
        self.build()
        self.draw_graph()
        self.coloring(0)

        for (i) in range(14, len(self.nodes)):
            self.rounds[self.nodes[i].color].append(self.nodes[i])


        for (i) in range(14):
            print(f"Round {i+1}   -----    Color: {self.total_colors[i]}")
            for match in self.rounds[i]:
                print(f"{match.homeTeam} x {match.guestTeam}")
            print()
    

        self.draw_graph()

graph = Graph()
graph.solve()
