- First check if no grid then return 0
- Create a set visited and also initialize rows and cols and also count of islands
- Now iterate throught the grid and if we found "1" and r, c is not in visit we call bfs on it and increment the count of island 
**bfs**
- initialize a q and add (r, c) in q. Also add it to visited
- Now while q pop the row and col and go to all the four directions and check if "1" is found and r, c is not visited we just add it to q and visited
- Bfs done. Now at the end of the program return count of islands