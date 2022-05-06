class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # go through each row and find the minimum and add it 
        dp = [0] * (len(triangle)+1)
        for row in triangle[::-1]:
            for idx, num in enumerate(row):
                # I have to check num + dp[idx] or num+dp[idx+1]
                dp[idx] = num + min(dp[idx], dp[idx+1])
        return dp[0]