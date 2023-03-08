##solution
- since the question has space constraints we can't another data structure to solve it
- instead we will use the array itself to register the frequency of each element
- another thing to notice is the elements of the array are always less than the length
- so we can use each element to point at specific index and get it's frequency
- when we traverse we make each element negative
- if we get an element that is negative it means it has been modified before which means that indeces value has been incountered and is being encountered again which means it's a duplicate we will add it to the solution.