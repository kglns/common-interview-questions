from recursion import recursiveReverseString, mergeSort, permutateString2

def testRecursiveReverseString():
    assert(recursiveReverseString('') == '')
    assert(recursiveReverseString('a') == 'a')
    assert(recursiveReverseString('abcd') == 'dcba')

def testMergeSort():
    assert(mergeSort([2]) == [2])
    assert(mergeSort([2, 1]) == [1, 2])
    assert(mergeSort([9,8,7,6,5]) == [5,6,7,8,9])

if __name__ == '__main__':
    print('----- Running Tests -----')
    testRecursiveReverseString()
    testMergeSort()
    # permutateString('abcd')
    # permutateString2('abc')
    