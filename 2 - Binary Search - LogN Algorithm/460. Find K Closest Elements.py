# Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

# Example
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        res = []
        start, end, length = 0, len(A) - 1, len(A)
    
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        toRight = min(length, k + end)
        toLeft = max(0, start - k)
        rangeToSearch = A[toLeft:toRight]
        diff = [(abs(e - target), e) for e in rangeToSearch]
        diff = sorted(diff)
        diff = diff[:k] ## 前k個tuple

        for _, x in diff:
            res.append(x)
        return res
