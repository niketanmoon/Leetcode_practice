- First take a list that contains n+1 1s
- [1, 1, 1, 1]
- Now range from 2 to n + 1 and then we have to count the total tree for each number
- So now loop from 1 to number of nodes we selected
- Now **total = number[left] * number[right]**
- Now go through this for every number of nodes given and add it to the total
- Now once we calculated the number of nodes we did with some number of nodes we update the list
- Lets say we were able to make total of 5 trees with 3 nodes
- [1, 1, 2, 5]
- and then return list[n] the last value calculated 