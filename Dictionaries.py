# Working with Dictionaries
my_dict = {'key1':'val1','key2':'val2','key3':'val3'}
print my_dict
print my_dict['key3']
my_dict = {'k1':213,'k2':3.4,'k3':'string'}
print my_dict['k2']
print my_dict['k3'][::-1]
my_dict['k1'] = my_dict['k1']-120
print my_dict
my_dict['k1'] +=100
print my_dict['k1']

""" Assigning keys and values to an empty dictionary"""
d = {}
d['animal'] = 'dog'
d['answer'] = 42
d['owner'] = 'Mr. Bean'
print d

"""Nested Dictionaries"""
d={'k1':{'Nestkey':{'subnetkey':'value'}}}
print d['k1']['Nestkey']['subnetkey'].upper()


d = {'k1':213,'k2':3.4,'k3':'string'}
print d.keys()
print d.values()
print d.items()