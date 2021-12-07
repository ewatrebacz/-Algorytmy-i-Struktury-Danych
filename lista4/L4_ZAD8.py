"""
Zaprojektuj i przeprowadź eksperyment porównujący wydajność listy jednokierunkowej i listy wbudowanej w Pythona.
"""
import time 
import matplotlib.pyplot as plt

class Node:
  
  def __init__(self,init_data):
    self.data = init_data
    self.next = None
  
  def get_data(self):
    return self.data

  def get_next(self):
    return self.next
  
  def set_data(self,new_data):
    self.data = new_data
  
  def set_next(self,new_next):
    self.next = new_next
    

class UnorderedList(object):
  
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, item):
    temp = Node(item)
    temp.set_next(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.get_next()
    return count
    
  def search(self,item):
    current = self.head
    found = False
    while current != None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()
    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    
    while not found:
      if current.get_data() == item:
        found = True
      else:
        previous = current
        current = current.get_next()
    
    if previous == None: #jeśli usuwamy pierwszy element
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())

  def remove2(self, item, start=0):
    current = self.head
    previous = None
    found = False
    index = 0
    
    while not found:
      if current.get_data() == item and index >= start:
        found = True
      else:
        previous = current
        current = current.get_next()
        index += 1
    
    if previous == None: #jeśli usuwamy pierwszy element
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())
      
  def append(self, item):
    """
    Metoda dodająca element na koniec listy.
    Przyjmuje jako argument obiekt, który ma zostać dodany.
    Niczego nie zwraca.
    """
    end = False
    current = self.head
    if self.size() == 0:
      self.add(item)
      return
    while end == False:
        if current.get_next() == None:
            end = True
        else:
            current = current.get_next()
    new = Node(item)
    current.set_next(new)

    
  def index(self, item):
    """
    Metoda podaje miejsce na liście, 
    na którym znajduje się określony element - 
    element pod self.head ma indeks 0.
    Przyjmuje jako argument element, 
    którego pozycja ma zostać określona.
    Zwraca pozycję elementu na liście lub None w przypadku, 
    gdy wskazanego elementu na liście nie ma.
    """
    index = 0 
    current = self.head
    if current == None:
      return None
    while current.get_next() != None:
        if current.get_data() == item:
            return index
        else:
            current = current.get_next()
            index += 1
    if current.get_data() == item:
        return index
    else:
        return None
    
  def insert(self, pos, item):
    """
    Metoda umieszcza na wskazanej pozycji zadany element.
    Przyjmuje jako argumenty pozycję, 
    na której ma umiescić element oraz ten element.
    Niczego nie zwraca.
    Rzuca wyjątkiem IndexError w przypadku, 
    gdy nie jest możliwe umieszczenie elementu
    na zadanej pozycji (np. na 5. miejsce w 3-elementowej liście).
    """
    if pos == 0:
        self.add(item)
        return
    index = 0 
    current = self.head
    while index != pos - 1 and current != None:
        index += 1
        current = current.get_next()
    if current == None:
        raise IndexError('Choose different position!')
    new = Node(item)
    new.set_next(current.get_next())
    current.set_next(new)
  
  def pop(self, pos=-1):
    """
    Metoda usuwa z listy element na zadaniej pozycji.
    Przyjmuje jako opcjonalny argument pozycję, 
    z której ma zostać usunięty element.
    Jeśli pozycja nie zostanie podana, 
    metoda usuwa (odłącza) ostatni element z listy. 
    Zwraca wartość usuniętego elementu.
    Rzuca wyjątkiem IndexError w przypadku,
    gdy usunięcie elementu z danej pozycji jest niemożliwe.
    """
    if self.is_empty() == True:
        raise IndexError('There is nothing to remove.')
    if pos == -1:
        if self.size() == 1:
            pop = self.head.get_data()
            self.head = None
            return pop
        index = 0 
        current = self.head
        while index != self.size() -2:
            index += 1
            current = current.get_next()
        pop = current.get_next()
        pop = pop.get_data()
        current.set_next(None)
        return pop
    else:
        index = 0
        current = self.head
        while index != pos and current != None:
            index += 1
            current = current.get_next()
        if current == None:
          raise IndexError('Choose different position.')
        pop = current.get_data()
        self.remove2(pop, pos)
        return pop

def compare2(n):
    """
    Porównuje czas wykonywania działań na liście jednokierunkowej i pythonowej
    w zalezności od n.
    Zwraca czas wykonywania działań dla listy jednokierunkowej i pythonowej.
    """
    unordered_list = UnorderedList()
    time_1_1 = time.time()
    for i in range(0,3*n):
        unordered_list.append(i)
    for i in range(0,2*n):
        unordered_list.pop()
    for i in range(0,n):
        unordered_list.insert(i,'sth')
    time_1_2 = time.time()
    time1 = time_1_2 - time_1_1
    python_list = []
    time_2_1 = time.time()
    for i in range(0,3*n):
        python_list.append(i)
    for i in range(0,2*n):
        python_list.pop()
    for i in range(0,n):
        python_list.insert(i,'sth')
    time_2_2 = time.time()
    time2 = time_2_2 - time_2_1
    return time1, time2

x = [10, 15, 20, 50, 100]
y1 = []
y2 = []
for i in x:
    y1.append(compare2(i)[0])
    y2.append(compare2(i)[1])

fig, ax = plt.subplots()
plt.plot(x, y1, 'k--', x, y2, 'k:')
plt.legend(('unordered list', 'python list'))
plt.xlabel('number of elements')
plt.ylabel('time [s]')
plt.title('Comparison: unordered list vs python list')
plt.show()
print(y1, y2)
