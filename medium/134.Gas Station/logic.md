- First check if the sum gas is less than sum of cost if it is then return -1
- Now total = 0 and startIdx = 0
- Now go through the list and add gas[i] - cost[i] to  the total
- Now check if anytime total is negative we reset it to 0 and move to the next index and we know that it should not start from that index
- So startIdx = i+1
- return startIdx