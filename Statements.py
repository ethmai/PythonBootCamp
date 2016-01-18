# If, Elif, Else

loc = 'Apple Store'
if loc == 'Auto shop':
    print 'Welcome to the Auto Shop'
elif loc == 'bank':
    print 'Welcome to the Bank'
else:
    print 'Where are you?'

"""
Name = raw_input("What is your name: ")
if Name == 'Sam':
    print "Hello Sam!"
elif Name == 'Jay':
    print 'Welcome Jay!'
elif Name == 'John':
    print 'Hi John!'
else:
    print "I wasn't expecting you but you are welcome to join us"
"""
# For loop

# One parameter
for i in range(5):
    print(i),
print''
# Two parameters
for i in range(3, 6):
    print(i),
print''
# Three parameters
for i in range(4, 10, 2):
    print(i),
print''
# Going backwards
for i in range(0, -10, -2):
    print(i),
print''

a = 'This is a string'
for i in a:
    print i

# loop with a tuple
tup = (1, 2, 3, 4, 5)
for i in tup:
    print(i),
print''

l = [(2, 4), (6, 8), (10, 12)]
for tup in l:
    print tup,
print''

# unpacking
for (t1, t2) in l:
    print t1,
print''

"""
For loop with Dictionaries
(Only keys are printed, Python 3 can do better)
"""
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print item,
print''

# python 2.x

for k, v in d.iteritems():
    print k, v

# python 3.x
for k, v in d.items():
    print k, v

# Modulo
print(10 % 3)

# While Loop