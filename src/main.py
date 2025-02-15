class Vertex:
    def __init__(self, id, homeTeam=None, guestTeam=None):
        self.id = id 
        self.homeTeam = homeTeam
        self.guestTeam = guestTeam
        self.neighbors = list[int]()
        self.color = None