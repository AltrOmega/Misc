from collections import deque

### Zadanie 3.1
def isvalid(s: str):
    stack = deque()
    for char in s:
        if char in ['(','[']:
            stack.append(char)
            continue
        
        if char in [')',']']:
            char_ = stack.pop()
            char = '(' if char == ')' else '['
            if char != char_:
                return False

    if len(stack) == 0:
        return True
    return False

print("+-----+ Zadanie 3.1 +-----+")
print(isvalid('(())'))
print(isvalid('([])'))
print(isvalid('((2 + 5) * (2 + 3)) / 2'))
print(isvalid('a = [(3, 5), (2, 5), (2, 9)]'))
print(isvalid('(]()[]'))
print(isvalid('[[((]]))'))

### Zadanie 3.2
def pocztapolska(list_):
    queue = deque(list_)
    out = deque()
    while queue:
        name, condition = queue.popleft()

        if condition == True:
            queue.append((name, False))
        else:
            out.append(name)

    return out

line = [
    ('Grażyna', True),
    ('Laura', False),
    ('Bartek', False),
    ('Andrzej', True),
    ('Wiesiek', False)
]
print("\n+-----+ Zadanie 3.2 +-----+")
print(pocztapolska(line))

### Zadanie 3.3
def helpStackSort(list_: list):
    s_ = deque(list_)
    p_ = deque()

    while s_:
        t = s_.pop()
        while p_ and p_[-1] > t:
            s_.append(p_.pop())
        p_.append(t)
    while p_:
        s_.append(p_.pop())
    return s_

print("\n+-----+ Zadanie 3.3 +-----+")
data = [3, 6, 7, 2, 9, 1, 7, 10, 0]
print(data)
print(helpStackSort(data))

input("\nPress Enter to exit.")