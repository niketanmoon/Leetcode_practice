**nlogn** method
- loop through the numbers 
- For each number while n: do % to check number of 1 and then do n // 2 
**dynamic programming solution O(n)**
- except first index which is 0 every other index is 1 + dp[i - offset]
- offset is a multiple of double the number
- offset = 1
- later if offset * 2 = index then offset = i
