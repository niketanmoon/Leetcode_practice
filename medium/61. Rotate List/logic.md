- First check the base case that is if not head then return head
- Then find the length of the linked list and shift the pointer to last node
- Now k = k % length this is because if k = 6 and length = 5 then we want to do 1 rotation
- But what if now k = 0 then return head
- Now start rotating algo
- Go till the pivot and then put the current.next in temp
- Now point the current.next to Null and tail.next to head
- Then just return temp