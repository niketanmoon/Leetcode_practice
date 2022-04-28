class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # check if the new interval is to the left
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #check if new interval is to the right and not overlapping
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # otherwise they are overlapping
                newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res