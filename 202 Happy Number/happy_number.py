class Solution:
	def isHappy(self, n: int) -> boolean:
		visit = set()
		while n not in visit:
			visit.add(n)
			n = self.sumOfSquares(n)
			if n == 1:
				return True
		return False


	def sumOfSquares(self, n:int) -> int:
		current_sum = 0
		while n:
			digit = n % 10
			digit = digit ** 2
			current_sum += digit
			n = n // 10
		return current_sum