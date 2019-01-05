# 577. Merge K Sorted Interval Lists
# Merge K sorted interval lists into one sorted interval list. You need to merge overlapping intervals too.

# Example
# Given

# [
#   [(1,3),(4,7),(6,8)],
#   [(1,2),(9,10)]
# ]
# Return

# [(1,3),(4,8),(9,10)]

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        data = []
        for i in intervals:
            data += i
        data.sort(key = lambda t:t.start)
        res = [data[0]]
        for d in data:
            if res[-1].end < d.start:
                res += [d]
            else:
                res[-1].end = max(res[-1].end, d.end)
        return res
