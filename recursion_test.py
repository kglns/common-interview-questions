from recursion import recursiveReverseString, mergeSort, permutateString, permutateString2

def testRecursiveReverseString():
    assert(recursiveReverseString('') == '')
    assert(recursiveReverseString('a') == 'a')
    assert(recursiveReverseString('abcd') == 'dcba')

def testMergeSort():
    assert(mergeSort([2]) == [2])
    assert(mergeSort([2, 1]) == [1, 2])
    assert(mergeSort([9,8,7,6,5]) == [5,6,7,8,9])

def testPermutateString():
    assert(permutateString('abc')[1] == 6)
    assert(permutateString2('abc')[1] == 6)

if __name__ == '__main__':
    print('----- Running Tests -----')
    testRecursiveReverseString()
    testMergeSort()
    testPermutateString()
    