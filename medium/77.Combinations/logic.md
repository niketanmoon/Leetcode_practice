- first create a result list
- Create a helper function
- Whenever size of comb list is equal to k then append comb list to result and return
- Go through start till n+1 and first add i to the comb list and then make a decision tree for it till size 2
- Once this is done that means we have added that comb to result now pop the comb list 
- call the backtrack function(1, []) and return result