"""# function to calculate volume of a sphere
def vol(rad):
    import math
    return float(4 / 3) * math.pi * rad ** 3


radius = int(raw_input('Enter the radius of your sphere: '))
print vol(radius)


# function to check whether a number is in a given range (inclusive)

def random_check(num, low, high):
    if num in range(low - 1, high + 1):
        return True
    else:
        return False


num = int(raw_input('Enter your number: '))
low = int(raw_input('Enter your lower limit: '))
high = int(raw_input('Enter your upper limit: '))
if random_check(num, low, high) is True:
    print('Your number is within the range')
else:
    print("Your number is out of range")


# Python function that accepts a string and calculate the number of upper case letters and lower case letters


def up_low(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print "Original String : ", s
    print "No. of Upper case characters : ", d["upper"]
    print "No. of Lower case Characters : ", d["lower"]


s = raw_input('Please enter a string with upper and lower case characters: ')
up_low(s)


# Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x


# Python function to multiply all the numbers in a list.

def multiply(numbers):
    prod = 1
    for i in numbers:
        prod *= i
    return prod


print multiply([1, 2, 4, 5, 7, -8])

"""
# Python function to check if a word/phrase is palindrome or not
def palindrome(s):
    s = s.replace(' ', '')  # to remove white space from the string
    return bool(s[::-1] == s)


print palindrome('nurses run')
print palindrome('hotel')

# Python function to check whether a string is pangram or not.
# set() is an unordered collection with no duplicate elements

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())