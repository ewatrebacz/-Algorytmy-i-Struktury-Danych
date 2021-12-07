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

class DequeueUsingUL(object):

  def __init__(self):
    self.items = UnorderedList()

  def is_empty(self):
    """
    Metoda sprawdzajacą, czy kolejka jest pusta.
    Nie pobiera argumentów.
    Zwraca True lub False.
    """
    return self.items.is_empty()
    
  def add_left(self, item):
    """
    Metoda dodaje element do kolejki z lewej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    self.items.add(item)
    
  def add_right(self, item):
    """
    Metoda dodaje element do kolejki z prawej strony.
    Pobiera jako argument element, który ma zostać dodany.
    Niczego nie zwraca.
    """
    self.items.append(item)
    
  def remove_left(self):
    """
    Metoda usuwa element z kolejki z lewej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
    if self.is_empty() == True:
        raise IndexError('List is empty.')
    return self.items.pop(0)
    
  def remove_right(self):
    """
    Metoda usuwa element z kolejki z prawej strony.
    Nie pobiera argumentów.
    Zwraca usuwany element.
    W przypadku pustej kolejku rzuca wyjątkiem IndexError
    """
    if self.is_empty() == True:
        raise IndexError('List is empty.')
    return self.items.pop()

  
  def size(self):
    """
    Metoda zwraca liczę elementów na w kolejce.
    Nie pobiera argumentów.
    Zwraca liczbę elementów na w kolejce.
    """
    return self.items.size()
