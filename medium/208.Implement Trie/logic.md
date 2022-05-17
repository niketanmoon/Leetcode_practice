- First implement a class TrieNode that takes children as a hashmap and endOfWord as False 
**init**
- initialize the root node to TrieNode
**insert**
- first set current to root
- Now go through each character in word
- if character not in children hashmap then add it to current.children[c] = TrieNode
- if it is in hashmap then we have to change the current to that children node
- at the end update endofword to True
**search**
- current to root
- now go through each character and if character not in hashmap then return False as we didnt find the word
- else increment current to its children
- return if current.endOfWord is true or not
**startsWith**
- same as search except at the end we dont have to look at end and we can just return True