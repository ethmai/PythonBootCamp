"""working with files"""

f = open('test.txt')
f.read()
print f.read()
f.seek(0)
print f.readlines()

"""%%writefile new.txt
First line
Second line"""

#For loop to print all lines in a new line
for line in open('test.txt'):
	print line

