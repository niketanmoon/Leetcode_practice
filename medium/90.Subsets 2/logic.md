- Take a list
- First sort the nums list so that it is easy to remove duplicates
- call the backtrack
- if i == len(nums) then append the subset to the result with a copy and return
**Including nums[i]**
- Now add the nums[i] to the subset
- then call the backtrack on the next index 
- then pop it from the subset so that the subset is reset
**Not including nums[i]**
- While doing this it is necessary to move the index so that it does not include the duplicate
- then call the backtrack again on next index
- Make a initial call with index 0 and empty list
- return res