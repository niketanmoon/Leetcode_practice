- We create a dummy node
- Let leftPrev point to dummy and current points to head
- Now iterate the current and left previous till left and left-1
- range(left-1)
- Now Reverse the list such that first save the current.next 
- Now point current.next to previous which is Null then move the previous to current and current to current.next in this case temp
- Once reverse is done we point the leftPrevious.next.next = current and leftPrevious.next = current.next
- return dummy.next