- Check if "0" in any string then return "0"
- Reverse both the numbers
- While adding the multiplied number always add it to the i1 + i2 index of num1 and num2
- create an array of 0 for len(num1) + len(num2)
- Directly add to the index (i1 + i2) num1[i1] * num2[i2] 
- Now the array may contain 8*2 = 16 which is a two digit number
- Then take the carry and store it in next index i1+i2+1 = res[i1+i2] // 10
- We just want to store the last digit in array so take the mod of result at i1 + i2
- When everything is done reverse the number
- It may contain leading zeros so eliminate it and convert the number in arrays to string and return join of it