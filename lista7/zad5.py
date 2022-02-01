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
        self.order = None    
        self.visited = None
        self.end = False       

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

    def find_cycle(self, vertex):
        if vertex.end == True:
            return
        if vertex.visited == True:
            raise ValueError('This graph cannot be topologically sorted.')
        vertex.visited = True
        for aVertex in vertex.getConnections():
            self.find_cycle(aVertex)
        vertex.end = True

    def dfs(self):
        for aVertex in self:
            aVertex.visited = False 
            aVertex.end = False
        for aVertex in self:
            self.find_cycle(aVertex)
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
        list_to_order = []
        for aVertex in self:
            list_to_order.append(aVertex.fin)
        list_to_order.sort()
        for i in range(0, len(list_to_order)):
            for aVertex in self:
                if aVertex.fin == list_to_order[i]:
                    aVertex.order = i + 1

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

def traverse2(y):
    """Find shortest way to the vertex.

@param y:(Vertex) Vertex 

@return list_of_moves:(list) shortest way to y"""
    list_of_moves  = []
    x = y
    while (x.getPred()):
        list_of_moves.append(x.getId())
        x = x.getPred()
    list_of_moves.append(x.getId())
    return list_of_moves

def every_shortest_way(graph:Graph, vertex):
    """Find shortest way to every vertex in graph from chosen vertex.
    
@param graph:(Graph) graph to check

@param vertex:(Vertex) chosen vertex

@return:(dict) Dictionary where the key is a vertex and the value is the shortest way to it"""
    result = {}
    graph.bfs(vertex)
    for aVertex in graph:
        if aVertex == vertex:
            continue
        else:
            shortest_way_backwards = traverse2(aVertex)
            shortest_way = []
            for i in range(len(shortest_way_backwards)):
                shortest_way.insert(0, shortest_way_backwards[i])
            result[aVertex.getId()] = shortest_way
    return result