- Take two pointers prev and current
- Initialize previous to one node before head
- currentNode = head
- Now iterate through the list and see if the current value matches the val or not
- if it matches then remove that link by prev.next = current.next
- if it does not match then just do prev = current and update current to next node