// 539. Move Zeroes
// Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Example
// Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
public class Solution {
    /**
     * @param nums: an integer array
     * @return: nothing
     */
    public void moveZeroes(int[] nums) {
        // write your code here
        int right = 0, left = 0;
        while (right < nums.length){
            
            if (nums[right] != 0){
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left ++;
            }
            right ++;
        }        
    }
}
