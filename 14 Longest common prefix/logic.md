- Finding the longest common prefix among the array of strings and if there is no common prefix then return empty string
- First tackle the empty string scenario. If the array is empty return empty string
- If the array is not empty, then the longest prefix length can only be equal to minimum length of string in an array
- Initialize common prefix = ""
- Now loop while i < minLength:
- if the character of the first string is equal to the character of the rest of the strings in an array then increase the longest common prefix
- If it is not equal then return the longest string