# Recursion Interview Questions
# Recursively reverse a string
def recursiveReverseString(string):
    stringArray = list(string)
    size = len(string)
    
    # Base case - return the string if the size in <= 1
    if size <= 1:
        return string
    
    # Remove the last char and append it to the front
    return string[size-1] + recursiveReverseString(string[:size-1])

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

# Heap's algorithm
def permutateString(string):
    
    # Take care of string to array conversion and iteration
    size = len(string)
    stringArray = list(string)
    final = []

    # Inner function to do the work
    def _permutate(k, stringArray):
        # Base case where k = 1
        if k == 1:
            print(''.join(stringArray))
            final.append(''.join(stringArray))
        else:
            # Main loop to decrease and conquer
            for i in range(k):
                # Decrease k by 1 first
                _permutate(k-1, stringArray)

                # If k is even swap first element and k-1 element
                # else swap ith element with k-1 element
                if k%2 == 0:
                    stringArray[0], stringArray[k-1] = stringArray[k-1], stringArray[0]
                else:
                    stringArray[i], stringArray[k-1] = stringArray[k-1], stringArray[i]
    # Do the actual work here
    _permutate(size, stringArray)
    return final, len(final)

# Recurse and swap last 2 elements
def permutateString2(string):
    final = set()
    stringArray = list(string)
    def _permutate(s1, s2):
        size = len(s2)
        if len(s2) == 1:
            print(''.join(s1[:len(s1)-1] + s2 + [s1[-1]]))
            final.add(''.join(s1[:len(s1)-1] + s2 + [s1[-1]]))
        else:
            for i in range(size):
                # Pull out the ith element from s2
                element = s2[i]
                # Recreate a new array with that element
                newArray = s2[:i] + s2[i+1:]
                # Append the element to s1 and also pass in the new array
                _permutate(s1 + [element], newArray)
    
    # The trick is you have start with empty array and move elements to it one by one
    # and finally swapping the last 2
    # _permutate is called at every ith index to cover all possible combinations
    _permutate([], stringArray)
    return final, len(final)

def bfs():
    pass
    