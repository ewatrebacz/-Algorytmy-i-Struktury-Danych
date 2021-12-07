import time
import matplotlib.pyplot as plt
import functools

class QueueBaB(object):
    """
    Klasa implementująca kolejkę za pomocą pythonowej listy tak,
    że początek kolejki jest przechowywany na początku listy.
    """
  
    def __init__(self):
        self.list_of_items = []
    
    def enqueue(self, item):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items += [item]
    
    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        self.list_of_items = self.list_of_items[1:]
  
    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if len(self.list_of_items) == 0:
            return True
        else:
            return False
    
    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.list_of_items)

class QueueBaE(object):
    """
    Klasa implementująca kolejkę za pomocą pythonowej listy tak,
    że początek kolejki jest przechowywany na końcu listy.
    """
  
    def __init__(self):
        self.list_of_items = []
    
    def enqueue(self, item):
        """
        Metoda służąca do dodawania obiektu do kolejki.
        Pobiera jako argument obiekt który ma być dodany.
        Niczego nie zwraca.
        """
        self.list_of_items = [item] + self.list_of_items
    
    def dequeue(self):
        """
        Metoda służąca do ściągania obiektu do kolejki.
        Nie pobiera argumentów.
        Zwraca ściągnięty obiekt.
        """
        self.list_of_items = self.list_of_items[:-1]
  
    def is_empty(self):
        """
        Metoda służąca do sprawdzania, czy kolejka jest pusta.
        Nie pobiera argumentów.
        Zwraca True jeśli kolejka jest pusta lub False gdy nie jest.
        """
        if len(self.list_of_items) == 0:
            return True
        else:
            return False
    
    def size(self):
        """
        Metoda służąca do określania wielkości kolejki.
        Nie pobiera argumentów.
        Zwraca liczbę obiektów w kolejce.
        """
        return len(self.list_of_items)

def compare(n):
    """
    Porównuje czas wykonywania działań na QueueBaB i QueueBaE.
    Zwraca czas wykonywania działań dla QueueBaB i QueueBaE.
    """
    bab = QueueBaB()
    time_1_1 = time.time()
    for i in range(0,3*n):
        bab.enqueue(i)
    for i in range(0,2*n):
        bab.dequeue()
    time_1_2 = time.time()
    time1 = time_1_2 - time_1_1
    bae = QueueBaE()
    time_2_1 = time.time()
    for i in range(0,3*n):
        bae.enqueue(i)
    for i in range(0,2*n):
        bae.dequeue()
    time_2_2 = time.time()
    time2 = time_2_2 - time_2_1
    return time1, time2

x = [10, 15, 20, 50, 100, 500, 800, 1000]
y1 = []
y2 = []
for i in x:
    y1.append(compare(i)[0])
    y2.append(compare(i)[1])

fig, ax = plt.subplots()
plt.plot(x, y1, 'k--', x, y2, 'k:')
plt.legend(('QueueBaB', 'QueueBaE'))
plt.xlabel('number of elements')
plt.ylabel('time [s]')
plt.title('Comparison: QueueBaB vs QueueBaE')
plt.show()
print(y1, y2)
