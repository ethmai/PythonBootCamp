#Working with Strings

#This is a one line comment!
s='Hello World!'
print s
print s*2
n=len(s)
print s[::-1]
print s[::-1]*2
i=0
while i<n+1:
	print s[i-1]
	i-=1
	if i<=-n:
		break

""" This is a block comment
num=1
while num < 11:
	print num**2
	num +=1
"""

#Continue with string
s='Hello World concatenate me!'

#Capitalize 1st world in the string
print s.capitalize()

#upper casing
print s.upper()

#split a string in to a list - by default using space
print s.split()
print s.split('W')

#lower casing
sl='HELLO WORLD!'
print sl.lower()

#Count string

print s.count('o')
print s.find('o')

# Formatting
s='STRING'
print 'Place another stirng with a mod and s: %s' %(s)

#Floating point numbers
print 'Floating point numbers: %1.2f' %(13.144)	

print 'Floating point numbers: %1.0f' %(13.144)

print 'Floating point numbers: %1.5f' %(13.144)

print 'Floating point numbers: %25.2f' %(13.144)

'''Conversion Format methods.
It should be noted that two methods %s and %r actually convert any python object to a string using two seperate methods: str() and repr(). We will learn more about these functions later on in the course, but you should note you can actually pass almost any Python object with these two methods and it will work:
'''
print 'Here is a number: %s. Here is a string: %s' %(123.1,'hi')

print 'Here is a number: %r. Here is a string: %r' %(123.1,'hi')

# Pass a tuple to the modulo symbol to place multiple formats in your print statements:

print 'First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22)
# Multiple times:
print 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')
# Several Objects:
print 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3)