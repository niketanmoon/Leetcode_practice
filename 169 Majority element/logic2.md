- Implement it using Boyer Moore algorithm
- This will search it in O(1) space complexity
- Let result be first element of the array
- Now go through the array and see if the number == result - if it is then increase the count
- If it is not equal then first check if count > 0 if it is then decrement the count else update the result if the count is zero and also increase the count