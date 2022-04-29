**bucket sort**
- Since there are three colors we can make a hashmap with the count and then go through 0 to 2 and if hashmap exist then update the nums with that key

**Quick Sort**
- left, right and a current pointer 
- while current pointer <= right 
- Whenever we encounter a 0 swap left and current pointer and increment left and current pointer
- Whenever we encounter a 1, increment current pointer
- whenever we encounter a 2, swap current and right and decrement right and **dont increment current pointer**
