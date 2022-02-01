import math 

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

def a_to_b(a, b, state):
    new_state = [0,0]
    if state[0] + state[1] <= b:
                new_state[1] = state [1] + state[0]
                new_state[0] = 0
    if state[0] + state[1] > b:
                new_state[0] = state[0] - (b - state[1])
                new_state[1] = b
    return (new_state[0], new_state[1])

def b_to_a(a, b, state):
    new_state = [0,0]
    if state[0] + state[1] <= a:
                new_state[0] = state[0] + state[1]
                new_state[1] = 0
    if state[0] + state[1] > a:
                new_state[1] = state[1] - (a - state[0])
                new_state[0] = a
    return state

def fill_a(a, state):
    return (a, state[1])

def fill_b(b, state):
    return (state[0], b)

def watter(state, a, b, c, graph:Graph):
    if c // math.gcd(a,b) == c / math.gcd(a,b) and c <= a and c <= b:
        solution_found = False
        if state == (a,b):
            return False
        elif state[0] == c or state[1] == c:
            return True
        elif state == (0,0):
            graph.addVertex(state)
            graph.addEdge((0,0),(a,0))
            solution_found = (solution_found or watter((a,0), a, b, c, graph))
            graph.addEdge((0,0),(0,b))
            solution_found = (solution_found or watter((0,b), a, b, c, graph))
            if solution_found:
                return True
        else:
            if state[0] != a:
                graph.addEdge(state,fill_a(a,state))
                solution_found = (solution_found or watter(fill_a(a,state), a, b, c, graph))
                if solution_found:
                    return True
            if state[1] != b:
                graph.addEdge(state, fill_b(b,state))
                solution_found = (solution_found or watter(fill_b(b,state), a, b, c, graph))
                if solution_found:
                    return True
            graph.addEdge(state, a_to_b(a, b, state))
            solution_found = (solution_found or watter(a_to_b(a, b, state), a, b, c, graph))
            if solution_found:
                return True
            graph.addEdge(state, b_to_a(a, b, state))
            solution_found = (solution_found or watter(b_to_a(a, b, state), a, b, c, graph))
            if solution_found:
                return True
        return solution_found
    else:
        raise ValueError('No solution.')