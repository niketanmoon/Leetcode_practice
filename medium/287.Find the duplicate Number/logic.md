- it is similar to a linkedlist cycle
- Now we have to apply floyds tortoise and hare algorithm
- where slow increments by one step but fast increments by 2 step 
- once fast == slow we break 
- now we initialize fast to 0 to  point at beginning 
- now we increment both by 1 and once they are equal we break
- At end return slow