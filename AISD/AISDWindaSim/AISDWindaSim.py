import random
from typing import Callable
from texttable import Texttable

### Symulation Inner Workings
class Elevator:
    def __init__(self, move: int = 0, current_level: int = 0, move_history: list = [0]):
        self.lifetime_move: int = move
        self.current_level: int = current_level
        self.move_history: list = move_history

    def move_to_level(self, move_to_level):
        self.lifetime_move += abs(self.current_level - move_to_level)
        self.current_level = move_to_level
        self.move_history.append(move_to_level)

    def __float__(self):
        return float(self.lifetime_move * 2.8)
    
    def __str__(self) -> str:
        return f'{round(float(self)/1000, 2)} km'
    
def iterate_move_epochs(func: Callable, epochs: int = 1000,
    elevator: Elevator = Elevator(), action: Callable = None):

    for i in range(epochs):
        func(elevator)
        if action != None:
            action()

    return elevator

# Scenario 1
def move_rand(elevator: Elevator):
    new_level = elevator.current_level
    while (new_level == elevator.current_level):
        new_level = random.randint(0, 10)

    elevator.move_to_level(new_level)

# Scenario 2
def to_work(elevator: Elevator):
    if random.random() < 0.7:
        elevator.move_to_level(random.randint(4,10))
        elevator.move_to_level(0)
    else:
        move_rand(elevator)
# Scenario 3
        
def from_work(elevator: Elevator):
    if random.random() < 0.7:
        elevator.move_to_level(0)
        elevator.move_to_level(random.randint(1,10))
    else:
        move_rand(elevator)

# Algorithm I
def stay_at_level(epochs: int, scenario: Callable):
    return iterate_move_epochs(scenario, epochs)

# Algorithm II
def return_to_bottom(epochs: int, scenario: Callable):
    elev = Elevator()
    return iterate_move_epochs(scenario, epochs,
        elevator=elev, action=elev.move_to_level(0))

# Algorithm III
def return_to_top(epochs: int, scenario: Callable):
    elev = Elevator()
    return iterate_move_epochs(scenario, epochs,
        elevator=elev, action=elev.move_to_level(10))

### Gathering Data
epochs = 1000
A1S1 = stay_at_level(epochs, move_rand)
A1S2 = stay_at_level(epochs, to_work)
A1S3 = stay_at_level(epochs, from_work)

A2S1 = return_to_bottom(epochs, move_rand)
A2S2 = return_to_bottom(epochs, to_work)
A2S3 = return_to_bottom(epochs, from_work)

A3S1 = return_to_top(epochs, move_rand)
A3S2 = return_to_top(epochs, to_work)
A3S3 = return_to_top(epochs, from_work)

### Output Data
def print_data():
    table = Texttable()
    headers = ['Scenariusz','Algorytm I' , 'Algorytm II', 'Algorytm III']
    table.header(headers)
    table.set_cols_align(['c', 'c', 'c', 'c'])

    table.add_row(['Scenariusz 1', str(A1S1), str(A2S1), str(A3S1)])
    table.add_row(['Scenariusz 2', str(A1S2), str(A2S2), str(A3S2)])
    table.add_row(['Scenariusz 3', str(A1S3), str(A2S3), str(A3S3)])
    SrdA1 = Elevator()
    SrdA2 = Elevator()
    SrdA3 = Elevator()
    SrdA1.lifetime_move = (A1S1.lifetime_move + A1S2.lifetime_move + A1S3.lifetime_move)/3
    SrdA2.lifetime_move = (A2S1.lifetime_move + A2S2.lifetime_move + A2S3.lifetime_move)/3
    SrdA3.lifetime_move = (A3S1.lifetime_move + A3S2.lifetime_move + A3S3.lifetime_move)/3
    table.add_row(['Wartość średnia', str(SrdA1), str(SrdA2), str(SrdA3)])

    print(table.draw())
print(f'+---------+ Wyniki Symulacji +---------+')
print_data()

### Algorythm Tests
# Algorithm I
A1_test = Elevator()
A1_test.move_to_level(7)
A1_test.move_to_level(2)
A1_test.move_to_level(5)
A1_test.move_to_level(6)
A1_test.move_to_level(1)

# Algorithm II
"""
Winda po przejeździe zawsze wraca na parter (piętro 0), a dopiero potem jedzie na kolejne piętro.
Rozpatrzymy ten sam przykład co dla poprzedniego algorytmu:
Przy takim losowaniu w tym algorytmie winda będzie zatrzymywać się na następujących piętrach:
0 → 7 → 0 → 2 → 5 → 0 → 6 → 1 → 0

Nie do końca rozumiem dlaczego winda jedzie tutaj 2 -> 5
jeśli "Winda po przejeździe zawsze wraca na parter (piętro 0)"
zakładam że jest jakieś przeoczenie w danych, ale na wszelki wypadek tutaj w testach wpisałem te
(zakładane) niepoprawne dane, aby matematyka się zgadała z tym co jest w dokumęcie z zadaniem.
"""
A2_test = Elevator()
A2_test.move_to_level(7)
A2_test.move_to_level(0)
A2_test.move_to_level(2)
A2_test.move_to_level(5)
A2_test.move_to_level(0)
A2_test.move_to_level(6)
A2_test.move_to_level(1)
A2_test.move_to_level(0)

# Algorithm III
"""
Opis działania autorskiego Algorytmu III

Winda zaczyna na piętrze 0, ale po przejeździe zawsze wraca na najwyższe piętro (piętro 10),
a dopiero potem jedzie na kolejne piętro.
Rozpatrzam ten sam przykład co w Algorytmie I:
Przy takim losowaniu w tym algorytmie winda będzie zatrzymywać się na następujących piętrach:
0 → 7 → 10 → 2 → 10 → 5 → 10 → 6 → 10 → 1 → 10
Czyli pokonana odległość będzie wynosić:
(7 + 3 + 8 + 8 + 5 + 5 + 4 + 4 + 9 + 9) × 2.8 = 173.6
Czyli korzystając z tego algorytmu winda pokona odległość 173.6m."""
A3_test = Elevator() # Elevator begins at level 0
A3_test.move_to_level(7)
A3_test.move_to_level(10)
A3_test.move_to_level(2)
A3_test.move_to_level(10)
A3_test.move_to_level(5)
A3_test.move_to_level(10)
A3_test.move_to_level(6)
A3_test.move_to_level(10)
A3_test.move_to_level(1)
A3_test.move_to_level(10)


def print_alg_tests():
    table = Texttable()
    headers = ['Algorytm I' , 'Algorytm II', 'Algorytm III']
    table.header(headers)
    table.set_cols_align(['c', 'c', 'c'])

    table.add_row([float(A1_test), float(A2_test), float(A3_test)])
    
    print(table.draw())
print(f'\n+---------+ Testy Algorytmów +---------+')
print_alg_tests()

input("\nPress Enter to exit.")