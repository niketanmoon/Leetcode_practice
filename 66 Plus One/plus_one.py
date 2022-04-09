class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_list = list()
        # concatenate all the numbers in digit in form of string
        string_digit = "".join(map(str, digits))
        final_number = int(string_digit) + 1
        for i in str(final_number):
            my_list.append(i)
        return my_list
            
        