- Create a hashmap
- Iterate through the array and check if num is in hashmap
- If it is not then store num as key and idx as value
- Now if it is in Hashmap then check if abs(idx - idx of the num in hashmap) <= k
- If it is then return True else return False