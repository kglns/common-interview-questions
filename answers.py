# Recursion Interview Questions
# Recursively reverse a string
def recursiveReverseString(string):
    stringArray = list(string)
    size = len(string)
    # Base case - return the string if the size in <= 1
    if size <= 1:
        return string
    # Remove the last char and append it to the front
    return string[size-1] + recursiveReverseStr(string[:size-1])

def testRecursiveReverseString():
    assert(recursiveReverseStr('') == '')
    assert(recursiveReverseStr('a') == 'a')
    assert(recursiveReverseStr('abcd') == 'dcba')

def mergeSort():
    pass

def bfs():
    pass

if __name__ == '__main__':
    print('----- Running Tests -----')
    testRecursiveReverseString()
    