class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'       
        self.pred = None           
        self.disc = 0             
        self.fin = 0               

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id   

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def dot(self):
        string = 'digraph G {'
        for i in self:
            for j in i.getConnections():
                next_element = f'"{i.getId()}" -> "{j.getId()}"'
                if next_element not in string:
                    string += next_element 
        return string + '}'     

    def bfs(self, start):
        start.setDistance(0)                            
        start.setPred(None)                             
        vertQueue = Queue()
        vertQueue.enqueue(start)                        
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()           
            for nbr in currentVert.getConnections():    
                if (nbr.getColor() == 'white'):         
                    nbr.setColor('gray')                             
                    nbr.setDistance(currentVert.getDistance() + 1)   
                    nbr.setPred(currentVert)                         
                    vertQueue.enqueue(nbr)                           
            currentVert.setColor('black')   

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

def is_valid_move(number_missionaries, number_cannnibals):
        return (0 <= number_missionaries <= 3) and (0 <= number_cannnibals <= 3)

def number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
        number_missionaries_right = 3 - number_missionaries
        number_cannnibals_right = 3 - number_cannnibals
        return (number_missionaries > 0 and number_cannnibals > number_missionaries) \
               or (number_missionaries_right > 0 and number_cannnibals_right > number_missionaries_right)

def solve(graph:Graph, number_missionaries, number_cannnibals, side):
        graph.getVertex((number_missionaries, number_cannnibals, side)).setColor('black')

        if (number_missionaries, number_cannnibals, side) == (0, 0, 0):   
            return True
        elif number_of_cannibals_exceeds(number_missionaries, number_cannnibals):
            return False

        solution_found = False
        operation = -1 if side == 1 else 1
        
        can_be_expanded = False

        for x, y in [(1, 0), (0, 1), (1, 1), (0, 2), (2, 0)]:
            next_m, next_c, next_s = number_missionaries + operation * x, number_cannnibals + operation * y, int(not side)
            if graph.getVertex((next_m, next_c, next_s)) is None:
                if is_valid_move(next_m, next_c):
                    can_be_expanded = True
                    graph.addEdge((number_missionaries, number_cannnibals, side), (next_m, next_c, next_s))
                    solution_found = (solution_found or solve(graph, next_m, next_c, next_s))
                    if solution_found:
                        return True
        return solution_found