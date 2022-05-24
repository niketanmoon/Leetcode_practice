- The idea is to store every word in a Trie data structure
- Make a new class Trie with children as hashmap and endWord as False
- Now in the class wordDictionary in the contructor just initialize self.root = TrieNode
**addWord**
- first go through each character in word if it is not in the children then add that character as a Trienode into hashmap
- if it is present then go to character's children 
- at end of the word mark endWord as True
**search**
- its a recursive call to dfs(idx=0, self.root)
- First go through each character from idx to len(word)
- if the c is "." then we will call dfs on all the children values
- if dfs returns True then return True else after the whole children values are done return False
- else if c is not "." simply check if it is in root.children hashmap 
- if it is not then return False as the word does not exist 
- else current = current.children[c] moving curent to its children
- At dfs end return current.endWord