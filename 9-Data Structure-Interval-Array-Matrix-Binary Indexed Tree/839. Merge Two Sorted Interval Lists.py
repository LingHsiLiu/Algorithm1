# 839. Merge Two Sorted Interval Lists
# Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

# Example
# Given list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)], return [(1,4),(5,6)].

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        i, j = 0, 0 
        results = []
        while (i < len(list1) and j < len(list2)):
            if list1[i].start < list2[j].start:
                self.push_back(results, list1[i])
                i += 1
            else:
                self.push_back(results, list2[j])
                j += 1
        while i < len(list1):
            self.push_back(results, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(results, list2[j])
            j += 1
        
        return results
        
    def push_back(self, results, interval):
        if not results:
            results.append(interval)
            return 
        
        last_interval = results[-1]
        if last_interval.end < interval.start:
            results.append(interval)
            return 
        
        results[-1].end = max(results[-1].end, interval.end)

