class Solution:
    def climbStairs(self, n: int) -> int:
        last = second_last = 1
        for i in range(n-1):
            second_last, last = last + second_last, second_last
        return second_last