- check if t is empty or not if empty return empty
- Make two hashmaps for count t and window
- Now update countT hashmap
- Approach with sliding window
- loop through the string and put character in window
- Now also check if that character is in countT or not
- if it is and values for window and count T match then we increment the have
- check while have == need
- update the result and result length 
- decrement the character count from window
- check if that character is again in countT and the count in window < count t
- if it is that means decrement have
- increment left by 1
- At the end we will left, right from res
- return s[left, right+1] if res length is not infinity