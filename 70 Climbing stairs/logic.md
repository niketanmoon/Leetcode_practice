- In a list say n = 100
- Now if we start from last 100 step, the way to reach is always 1 step
- And for 99th step the way to reach is also 1
- This is true for every case
- Now iterate from 0 to n-2
- lets say n=5
- list = [0,0,0,1, 1]
- Now for third step = fourth step + 5th step
- list = [0, 0, 2, 1, 1]
- Observe that last and second last step = 1
- Now when we found out ways for 3rd step, this becomes second last step  and 4th step becomes last_step
- Now once all the ways are calculated, Return the sum, which is on the second Last step