- IMplement a sliding window technique 
- left is 0 and total = 0 also result to max value
- now we go through the loop
- and each time we add to the total
- if anytime total >= target we just take the minimum of l - r + 1 and result 
- also increment left but before than decrement total
- Once this is all done we just return result if it is not float inf else 0