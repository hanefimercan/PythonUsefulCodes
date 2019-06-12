from cPickle import dumps
from sys import getsizeof


def getSizeOfObject(obj):
    # size of an object in bytes
    objectAsString = dumps(obj)
    return getsizeof(objectAsString) 
    
    
# Test
a = {'Mercan': [1,2,3,4,5], 1024: None, 'test': {'test2': None}}
print(str(getSizeOfObject(a)) + " bytes")
