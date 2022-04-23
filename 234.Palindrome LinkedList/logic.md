**Naive Solution**
- Iterate through the linked and append it to an array
- Now check palindrome for array

**O(1) Space Complexity**
- First take slow and fast pointer
- Now iterate through the linked list till fast and fast.next is not null
- Now slow is at middle now reverse the linkedlist from right half
- Once the linkedlist from right half is reversed we will check beginning and end node and see if they matches or not
