class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        output = []
        bucket = [[] for _ in range(len(nums)+1)]
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        for key, val in hashMap.items():
            bucket[val].append(key)
        
        for list1 in bucket[::-1]:
            if list1:
                for c in list1:
                    output.append(c)
                    k -= 1
                    if not k:
                        return output
        return output