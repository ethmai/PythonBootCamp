square = lambda num: num ** 2
print square(9)

even = lambda x: x % 2 == 0
print even(9)
print even(4)

# grab first character of a string
first = lambda s: s[0]
print first('San Francisco')

# reverse a string
reverse = lambda s: s[::-1]
print reverse('San Francisco')

# Lambda can accept more than 1 function into a lambda expression
adder = lambda x, y: x * y
print adder(7, 6)

# Lambda can be very useful when used with map(), filter(), and reduce()
