class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        left, right = 0, len(s) - 1
        charArray = list()
        for c in s:
            charArray.append(c)
            
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            charArray[left], charArray[right] = charArray[right], charArray[left]
            left += 1
            right -= 1
        return "".join(charArray)