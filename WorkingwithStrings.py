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

print s.count()
print s.count('o')
print s.find('o')

# Formatting

	
