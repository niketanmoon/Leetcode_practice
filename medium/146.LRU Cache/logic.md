- First create a Node class with key and val and also prev and next to be None
- Now in initialization of lru class, define self.capacity as capacity and self.cache as empty hashmap
- Also we need to keep track of LRU and most recent
- self.left = least recent Node(0,0) and self.right = Node(0, 0) most recent
- Also it should be a doubly linked list therefore left.next = right and right.prev = left
- **get function**
- If the key is in the cache we will first remove and insert it in the most recent place
- return self.cache[key].val
- if nothing is found then return -1
- **put function**
- if key is in cache then we remove it from the list
- now it is not in the cache so we insert it into the cache and do insert
- if len(cache) > capacity then we will remove the lru which is self.left.next and then delete it from the cache
**remove function**
- For removing prev node is node.prev and next node is node.next
- Now we will link previous.next = node.next and next.previous = node.previous
**insert function**
- previous node is right.prev and next node is right
- Now for inserting we will add next node.prev = node and previous.next = node
- Now we will connect new nodes next and prev link
- node.prev = prev and node.next = next