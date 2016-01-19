# methods
l = [1, 2, 3, 3, 4, 5, 6]
print l

print l.count(3)

help(l.count)

"""functions
def sample_function(arg1, arg2):
    pass


sample_function(1, 2)
"""


def addition(arg1, arg2):
    """
    Usage: perform a addition for 2 integer
    :rtype: object
    :param arg1: number 1
    :param arg2: number 2
    :return: number + number 2
    """
    print arg1 + arg2


help(addition)
addition(100, 101)


def greeting(name):
    print 'Hello ' + name


greeting(James)
