- Apply binary search 
- while left < right
- check if the middle element is less than the next element that means peak is on right side
- so left = middle + 1
- else peak can be the middle element or the left side so right = middle
- return left at the end to get the index