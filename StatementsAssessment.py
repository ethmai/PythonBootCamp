# Use for, split(), and if to create a Statement that will print out letters that start with 's':
st = 'Print only the words that start with s in this sentence'
l = st.split()
print l
for word in l:
    if word[0] == 's':
        print word

#Use range() to print all the even numbers from 0 to 10.
x = 0
for x in range(10):
    if x % 2 == 0:
        print x,
print''

#better solution:
print range(0,11,2)

#Use List comprehension to create a list of all numbers between 1 and 50 that are divisble by 3.
x = 0
for x in range(1,50):
    if x % 3 == 0:
        print x,
print''

#Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
l = st.split()
for word in l:
    if len(word) % 2 == 0:
        print word + "'s length is event"

"""
Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

for x in range(1,101):
    if x % 3 == 0:
        if x % 5 == 0:
            print x,
            print "= FizzBuzz"

        else:
            print x,
            print  '= Fizz'
    elif x % 5 == 0:
        print x,
        print '= Buzz'
    else:
        print x

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
l = st.split()
l1 =[]
for i in l:
    l1.append(i[0])
print l1

