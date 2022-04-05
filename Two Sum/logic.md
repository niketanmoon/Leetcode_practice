- `nums` - Its a list of numbers 
- `target` - Its the number we have to find index for 
# Logic
- First define a hash_map = {}
- Now loop through the list nums. We used `enumerate` to get index and number
- The problem is to find the index of two numbers that adds to the target
- first number = number inside nums
- second number  = target - first number
- Now check if second number is in hash map if it is then return idx of the first number and hash_map[second_number]
- else store the index of the first number as key and value pair 
- `Example`
`
nums = [2, 7, 11, 15]  target = 9
`

- We store `hashmap = {
	2: 0,
	7: 1
}`