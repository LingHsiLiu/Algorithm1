// 463. Sort Integers (合併排序)
// Given an integer array, sort it in ascending order. Use selection sort, bubble sort, insertion sort or any O(n2) algorithm.

// Example
// Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].

public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return;
        }
        int[] temp = new int[A.length];
        mergeSort(A, 0, A.length - 1, temp);
    }
    
    private void mergeSort(int[] A, int start, int end, int[] temp){
        if (start >= end){
            return;
        }
        mergeSort(A, start, (start + end) / 2, temp);
        mergeSort(A, (start + end) / 2 + 1, end, temp);
        merge(A, start, end, temp);
    }
    
    private void merge(int[] A, int start, int end, int[] temp){
        int middle = (start + end) / 2;
        int leftIndex = start;
        int rightIndex = middle + 1;
        int index = leftIndex;
        
        while (leftIndex <= middle && rightIndex <= end){
            if(A[leftIndex] < A[rightIndex]){
                temp[index++] = A[leftIndex++];
            }else{
                temp[index++] = A[rightIndex++];
            }
        }
        
        while (leftIndex <= middle){
            temp[index++] = A[leftIndex++];
        }
        while(rightIndex <= end){
            temp[index++] = A[rightIndex++];
        }
        
        for (int i = start; i <= end; i++){
            A[i] = temp[i];
        }
    }
}
