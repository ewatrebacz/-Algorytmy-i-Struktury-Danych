import random, time, math 
import matplotlib.pyplot as plt

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2      
        
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)        
        
    def findMin(self):
        return self.heapList[1]

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1    
            
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval           
    
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1    
            
    def size(self):
        return self.currentSize
    
    def isEmpty(self):
        return self.currentSize == 0
    
    def __str__(self):
        txt = "{}".format(self.heapList[1:])
        return txt

def sort(num_list):
    """Sort the list.
    
    @param num_list:(list) list to sort

    @return:(list) sorted list"""
    heap = BinHeap()
    heap.buildHeap(num_list)
    sorted = []
    while heap.size() > 0:
        sorted.append(heap.delMin())
    return sorted

x = []
y = []
y2 = []

for i in range (1,1001):
    t1 = time.time()
    sort([random.randint(-100, 100) for i in range(i)])
    t2 = time.time()
    y.append(t2 - t1)
    x.append(i)
    y2.append((10**(-5.9))*i*math.log(i, 2))
    
plt.scatter(x, y, label='wyniki pomiaru')
plt.plot(x, y2, color='r', label='t(n)')
plt.xlabel('liczba elementów na liście')
plt.ylabel('czas działania funkcji')
plt.legend()
plt.show()