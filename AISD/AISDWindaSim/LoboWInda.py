import random
from typing import Callable
from collections import deque

level=0
level_space=2.8
level_max=10 # including 0 and 10
level_min=0

length_counter=0.0


def script1():
    start = random.randint(0, 10)
    finish = random.randint(0, 10)

    # Zapewniamy że start i finish są różne
    while start == finish:
        finish = random.randint(0, 10)

    return start, finish


def script2():
    if random.random() < 0.7:
        start = random.randint(4, 10)
        finish = 0

        return start, finish
    return script1()


def script3():
    if random.random() < 0.7:
        start = 0
        finish = random.randint(1, 10)

        return start, finish
    return script1()


# elevator
def move_elevator(destination):
    if destination > level_max or destination < level_min:
        return
    global length_counter
    global level
    length_counter= abs(level-destination) * level_space + length_counter
    level = destination


def print_and_reset_counter():
    global length_counter
    print(str(round(length_counter, 1)) + "m")
    length_counter = 0.0


def moveI(start, finish):
    move_elevator(start)
    move_elevator(finish)
    print_and_reset_counter()
      

def moveII(start, finish):
    move_elevator(start)
    move_elevator(finish)
    move_elevator(0)
    print_and_reset_counter()
    
    
avg = deque()
def moveIII(start, finish):
    global avg
    # moving elevator from start to finish
    move_elevator(start)
    move_elevator(finish)
    
    # adding requested start position to queue and removing any position beyond 10 most recent
    avg.append(start)
    while len(avg)>=10:
        avg.popleft()
    
    # calculating optimal position
    optimalpos = 0
    for x in avg:
        optimalpos+=x
    optimalpos = optimalpos//len(avg)
    
    # moving to optimal position
    move_elevator(optimalpos)
    print_and_reset_counter()
    
    
# testing the elevator
from itertools import product
for test, move in product([script1, script2, script3],[moveI, moveII, moveIII]):
        # message
        print("Testing " + test.__name__ + " for " + move.__name__)
        print()
        
        #test
        for x in range(0, 10):
            start, finish = test()
            move(start, finish)
        print_and_reset_counter()