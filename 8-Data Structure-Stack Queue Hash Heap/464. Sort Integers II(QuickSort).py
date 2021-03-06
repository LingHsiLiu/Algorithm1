// 464. Sort Integers II // 快速排序
// Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

// Example
// Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].


public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers2(int[] A) {
        // write your code here
        quickSort(A, 0, A.length - 1);
    }
    // 快速排序
    private void quickSort(int[] A, int start, int end){
        if (start >= end){
            return;
        }
        
        int left = start, right = end;
        // key point 1: pivot is the value, not the index
        int pivot = A[(start + end) / 2];

        // key point 2: every time you compare left & right, it should be 
        // left <= right not left < right
        while (left <= right) {
        
        int left = start, right = end;
        int pivot = A[(end + start)/2];
        
        while (left < right){
            while (left <= right && A[left] < pivot){
                left++;
            }
            while (left <= right && A[right] > pivot){
                right++;
            }
            if (left <= right){
                int temp = A[left];
                A[left] = A[right];
                A[right] = temp;
            
                left++;
                right--;
            }
        }
        quickSort(A, start, right);
        quickSort(A, left, end);
    }
}
