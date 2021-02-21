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

# Common sorting algo which employs divide and conquer
# Time complexity - O(nlog(n))
# Space complexity - O(n)
def mergeSort(unsortedArray):
    
    # Helper inner function for combining base cases
    def _combine(first, second):
        final = []
        sizeFirst, sizeSecond = len(first), len(second)

        # Iterate the smaller array
        # Compare, and append the smaller element to final until the array is exhausted
        if sizeFirst > sizeSecond:
            while first:
                if first[0] < second[0]:
                    final.append(first[0])
                    first = first[1:]
                else:
                    final.append(second[0])
                    second = second[1:]
        else:
            while second:
                if first[0] < second[0]:
                    final.append(first[0])
                    first = first[1:]
                else:
                    final.append(second[0])
                    second = second[1:]
        
        # Append the residual elements if exists. 
        if first:
            final = final + first
        if second:
            final = final + second
        return final
            
    # Base case        
    size = len(unsortedArray)
    if size <= 1:
        return unsortedArray
    
    # Otherwise divide and conquer
    first = mergeSort(unsortedArray[:int(size/2)])
    second = mergeSort(unsortedArray[int(size/2):size])
    
    # Sort and combine elements from base cases
    resultantArray = _combine(first, second)
    return resultantArray

def testMergeSort():
    assert(mergeSort([2]) == [2])
    assert(mergeSort([2, 1]) == [1, 2])
    assert(mergeSort([9,8,7,6,5]) == [5,6,7,8,9])

def bfs():
    pass

if __name__ == '__main__':
    print('----- Running Tests -----')
    testRecursiveReverseString()
    testMergeSort()
    