- Apply binary search
- Make a helper function and pass left and right pointer nums and target
- Now while left <= right
- get the middle number and check if the middle number is the target then return middle index
- Now go first to left sorted array by checking if left number <= middleNumber
- Once you are in the left sorted array - define condition to go to right
- target > middle or target < left number - in both cases we go to right
- else we go to  left
- Similarly when we are in right portion of array
- define condition to go to left - target < middle number or target > rightmost
- else we go to right