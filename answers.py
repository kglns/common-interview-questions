def recursiveReverseStr(string):
    stringArray = list(string)
    size = len(string)
    if size <= 1:
        return string
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
    