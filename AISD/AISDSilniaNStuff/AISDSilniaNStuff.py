### Zadanie 3.1
def factorial(n: int):
    return 1 if n == 0 else n * factorial(n-1)

print('+-----+ Silnia +-----+')
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

### Zadanie 3.2
def collatz(n: int):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    else:
        return [n] + collatz(3 * n + 1)
    
print('+-----+ Sekwęcja Collatza +-----+')
print(collatz(1))
print(collatz(2))
print(collatz(3))
print(collatz(4))
print(collatz(5))

### Zadanie 3.3
def biggest_common_denominator(a: int, b: int):
    return a if b == 0 else biggest_common_denominator(b, a % b)

print('+-----+ Największy Wspólny Dzielnik +-----+')
print(biggest_common_denominator(10,4))
print(biggest_common_denominator(20,6))
print(biggest_common_denominator(28,8))
print(biggest_common_denominator(30,20))
print(biggest_common_denominator(35,14))

### Zadanie 3.4
def quicksort(array: list):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2] 
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

print('+-----+ Algorytm Quicksort +-----+')
print(quicksort(collatz(1)))
print(quicksort(collatz(2)))
print(quicksort(collatz(3)))
print(quicksort(collatz(4)))
print(quicksort(collatz(5)))

input("\nPress Enter to exit.")