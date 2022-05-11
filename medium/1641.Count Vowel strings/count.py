class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        result = 0
        for i in range(2, n+1):
            j = 3
            while j >= 0:
                dp[j] = dp[j] + dp[j+1]
                j -= 1
        for el in dp:
            result += el
        return result
                