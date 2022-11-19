'''
Computers represent characters with numbers. There exist different mappings between characters and numbers, with the most famous one being https://en.wikipedia.org/wiki/ASCII.

All the Latin letters are given consecutive numbers, for example, 'A' has number 65, 'B' has number 66, 'C' has number 67, etc.

Using list comprehension, produce a list of characters ['A', 'B', ..., 'Z']. Convert this list into a string; you should get 'ABCDE...'.

Use function chr to convert a number into the ASCII character.
'''

letters = [chr(n) for n in range(65,91)]
print(f"letters:{letters}")

s = "".join(letters)

print(s)