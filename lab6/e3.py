'''
Using list comprehension, create a list A of 10 random integers in the interval  [0,100] .
With the use of list compresention, convert A into a string s, where the numbers are separated by '-', e.g., "56-20-78-..."
With the use of list comprehension, calculate the number c of elements in A that are greater than 50.
Test your solutions.
'''
import random

a = [random.randint(0,100) for _ in range(10)]
print(f"a={a}")



c = [n for n in a if n>50]
print(f"c={c}")