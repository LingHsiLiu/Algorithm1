# 5. Kth Largest Element
# Find K-th largest element in an array.

# Example
# In array [9,3,2,4,8], the 3rd largest element is 4.

# In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return None
        return self.partition(nums, 0, len(nums) - 1, len(nums) - n)
    
    def partition(self, nums, start, end, n):
        if start == end:
            return nums[n]
            
        left, right = start, end
        pivot = nums[(start + end)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # left is not bigger than right
        if n <= right:
            return self.partition(nums, start, right, n)
        if left <= n:
            return self.partition(nums, left, end, n)
            
        return nums[n]


