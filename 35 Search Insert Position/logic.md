- First key is that the array is sorted
- We will make use of binary search to do the searching of a target
- l = left end r = right end
- while l <= r:
	middle = l + (r-l) // 2
- This way you find the middle index of the array and see if the target is greater, smaller or equal to  the middle element
- Now if the target value is greater, that means target is in the right side so move l = middle + 1 and continue
- else move right to left side i.e. r = middle - 1
- if the target is found then return the middle index