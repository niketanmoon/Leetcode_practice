- There is a sorted array in non decreasing order
- First initialize a index to 1 : this is because we want to change the number at this index
- loop through array from index 1
- Now compare if the current and previous element is same or not
- if its not same then replace the target_index with the current index number
- `nums[target_index] = nums[i]`
- and then increment the target index to 2
