// 463. Sort Integers
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
        for (int i = 0; i < A.length; i++) {
            int newVal = A[i];
            // System.out.println(newVal);
            int j = i - 1;
            // System.out.println(j);
            while (j >= 0 && A[j] > newVal) {
                A[j + 1] = A[j];
                j--;
                // System.out.println(j + 1);
            }
            A[j + 1] = newVal;

        }
    }
}
