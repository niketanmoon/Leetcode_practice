- First take a stack where you will store the parentheses
- loop through the string and whenever you find the open bracket, append it on the stack
- If you dont find the open bracket and find close bracket 
a. Then first check if your stack is empty
- if the stack is empty that means the string is not valid
- else we pop the first element of the stack and see if it matches with the close bracket then continue else return not valid
- Once all the string is looped through we will see if the stack is empty if the stack is empty then that means all the brackets matched and if its still not empty then that means string was not valid
- This can be done using return not stack