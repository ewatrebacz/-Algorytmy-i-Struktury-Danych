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
        first = self.list_of_items[0]
        self.list_of_items = self.list_of_items[1:]
        return first
  
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

class Stack:
    """
    Klasa implementująca stos za pomocą pythonowej listy tak,
    że szczyt stosu jest przechowywany na początku listy.
    """
    def __init__(self):
        self.stack = []

    def add(self, item):
        """
        Dodaje element na stos.
        Jako argument przyjmuje obiekt, który chcemy dodać
        Nic nie zwraca.
        """
        self.stack = [item] + self.stack

    def remove(self):
        """
        Usuwa element ze stosu.
        Nie przujmuje argumentów.
        Zwraca usunięty element.
        """
        pick = self.stack[0]
        self.stack = self.stack[1:]
        return pick

    def is_empty(self):
        """
        Sprawdza czy stos jest pusty.
        Nie przyjmuje argumentów.
        Zwraca True gdy stose jest pusty lub False gdy stos nie jest pusty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Sprawdza rozmiar stosu.
        Nie przyjmuje argumentów.
        Zwraca liczbę elementów znajdujących się na stosie.
        """
        return len(self.stack)

'''Przypuśćmy, ze w firmie X jest zatrudnionych 20 pracowników. 8 pracuje tam od początku istnienia firmy (3 lata), 4 od 1.5 roku i 8 pracowników jest nowych (pracują od 2 miesięcy). Ze względu na kłopoty w firmie wystąpiła potrzeba zredukowania liczby osób zatrudnionych o połowe.
Pytanie badawcze: Zastosowanie której ze struktur danych przeniesie firmie mniejsze straty pod względem kompetencji pracowników 
W kolejce bądź stosie pracownika reprezentuje jego doświadczenie w miesiącach([36, 36, 36, 36, 36, 36, 36, 36, 18, 18, 18, 18, 2, 2, 2, 2, 2, 2, 2, 2]) 
Jako pierwszą zastosujmy kolejkę:
Ukladamy odpowednio pracowników'''
empl = QueueBaB()
for i in range(8):
    empl.enqueue(36)
for i in range(4):
    empl.enqueue(18)
for i in range(8):
    empl.enqueue(2)
#pracownicy:
print(empl.list_of_items)
#przeprowadzamy radukcję
lost_exp = 0
for i in range(10):
    lost_exp += empl.dequeue()
#teraz doświadczenie pracowniku prezentuje się następująco:
print(empl.list_of_items)
#Mozna zatem powiedzieć ze straciliśmy łącznie 27 lat doświadczenia pracowników.
print(lost_exp)
#Teraz zastosujmy stos
empl2 = Stack()
for i in range(8):
    empl2.add(36)
for i in range(4):
    empl2.add(18)
for i in range(8):
    empl2.add(2)
lost_exp2 = 0
for i in range(10):
    lost_exp2 += empl2.remove()
#Po redukcji doświadczenie pracowniku prezentuje się następująco:
print(empl2.stack)
#Przy zastosowaniu stosu straciliśmy łącznie 4 lata i 4 miesiące doświadczenia
print(lost_exp2)
'''Przyjmując zatem uproszczenie, ze jedynym kryterium przy podejmowaniu decyzji o zwolnienie pracownika jest jego doświadczenie, 
zastosowanie stosu zawsze będzie korzystniejsze dla pracodawcy, poniewaz straci tych mniej doświadczonych pracowników
i mniej czasu zajmie mu odrobienie strat (nadrobienie doświadczenia)'''
#W przypadku naszego ekseprymentu, po zastosowaniu kolejki potrzeba 1.5 roku aby znowu mieć w firmie pracownika z trzyletnim doświadczeniem.
#Przyjmijmy,ze teraz zatrudniamy 4 nowych pracowników
for i in range(4):
    empl.enqueue(0)
for i in range(0, len(empl.list_of_items)):
    empl.list_of_items[i] += 18
#Po 1.5 roku doświadcznie pracowników prezentuje się następująco
print(empl.list_of_items)

for i in range(4):
    empl2.add(0)
for i in range(0, len(empl2.stack)):
    empl2.stack[i] += 18
#W przypadku ze stosem po 1.5 roku mamy bardziej doświadcoznych pracowników
print(empl2.stack)
