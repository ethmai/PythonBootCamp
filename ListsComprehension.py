l = []
for letter in 'word':
    l.append(letter)
print l

# Can be done in List Comprehension:
lst = [letter for letter in 'word']
print lst

lst = [x ** 2 for x in xrange(0, 11)]
print lst

lst = [num for num in range(11) if num % 2 == 0]
print lst

# Convert C to F
celsius = [0, 10, 20.1, 98.7]
fahrenheit = [temp * (9 / 5.0) + 32 for temp in celsius]
print fahrenheit

"""
Nested List Comprehension
Final result is x to the power of 6
"""
lst = [x**3 for x in [x**3 for x in range(11)]]
print lst