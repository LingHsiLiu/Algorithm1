# 104. Merge K Sorted Lists
# Merge k sorted linked lists and return it as one sorted list.

# Analyze and describe its complexity.

# Example
# Given lists:

# [
#   2->4->null,
#   null,
#   -1->null
# ],
# return -1->2->4->null.


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        
        trav = dummy = ListNode(-1)
        heap = []
        for ll in lists:
            print(ll)
            if ll:
                self.heappushNode(heap, ll)
        
        while heap:
            node = heappop(heap)[1]
            trav.next = node
            trav = trav.next
            if trav.next:
                self.heappushNode(heap, trav.next)
        return dummy.next
    
    def heappushNode(self, heap, node):
        heappush(heap, (node.val, node))

        

