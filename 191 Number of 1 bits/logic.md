- while n > 0
- take the last digit and mod it by 2 if its 1 then add it to the count
- Now remove the last digit by shifting to the right by 1 or taking quotient division and update the number

**Logic 2**
- Each time update n with n & (n-1) and increase the counter
- And with n - 1 will remove only the 1 bit from the number