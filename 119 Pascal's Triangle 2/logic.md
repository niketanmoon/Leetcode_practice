- We know that the base case is always res = [[1]]
- Now we loop from range 0 to rowIndex as the first row is already initialized
- then we will add 0 at the beginning and at the end of the element
- temp = [0, 1, 0]
- Now we will loop through len(last element in result) + 1, this is because the next row always contain an extra element from previous row
- and create a row with adding current and next element of temp
- Now since the row is created we can append it to the res
- return the last element in res