// 585. Maximum Number in Mountain Sequence
// Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

// Example
// Given nums = [1, 2, 4, 8, 6, 3] return 8
// Given nums = [10, 9, 8, 7], return 10

public class Solution {
    /**
     * @param nums: a mountain sequence which increase firstly and then decrease
     * @return: then mountain top
     */
    public int mountainSequence(int[] nums) {
        // write your code here
        int left = 0 ; 
        int right = nums.length - 1;
        while (left + 1 < right){
            int m1 = left + (right-left)/2;
            int m2 = right - (right - m1)/2;
            if (nums[m1] < nums[m2]){
                left = m1 + 1;
            }else if (nums[m1] > nums[m2]){
                right = m2 - 1; 
            }else{
                left = m1;
                right = m2;
            }
        }
        return nums[left] > nums[right] ? nums[left] : nums[right];
    }
}
