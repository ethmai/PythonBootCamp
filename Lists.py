#Working with Lists
my_list = [1,2,3]
my_list = ['a string',23,100,232,'0']
print my_list
print len(my_list)

#Indexing and Slicing
print my_list[0] 	#print item at index 0
print my_list[1:]	#print items from index 1 onwards 
print my_list[:3]	#print items from 0 to 3
my_list = my_list + ['infinity'] # adding more items into the list, re-assigning the list make the addition permanent
print my_list

#Make the list double
print my_list*2 # doubling is not permanent unless you re-assign the list

#Append method
l = [1,2,3]
l.append('append me!')
print l
#Pop method
l.pop(0)
print l
popped_item = l.pop() #if not assigned, default value is -1
print popped_item
print l

#Reverse
new_list = ['a','x','z','d','s','f',1,100,25]
new_list.reverse()
print new_list

#sort: Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort() 
print new_list

""" 
Nesting Lists
A great feature of of Python data structures is that they support nesting. This means we can data structures within data structures. For example: A list inside a list.
Let's see how this works!
"""
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]
print matrix
print matrix[0]
print matrix[0][0]

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]
print first_col