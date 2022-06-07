class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # tree has 2 * n elements
        self.tree = [0] * self.n + nums
        self.build()

    def build(self):
        for index in range(self.n - 1, 0, -1):
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query(self, left, right):
        left, right = left + self.n, right + self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result, left = result + self.tree[left], left + 1
            if right % 2 == 0:
                result, right = result + self.tree[right], right - 1
            left, right = left // 2, right // 2
        return result

    def update(self, index, val):
        index += self.n
        delta = val - self.tree[index]
        while index > 0:
            self.tree[index] += delta
            index //= 2


class NumArray:
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)