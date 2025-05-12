// 88. Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p = m+n-1; // length of both arrays
        int p1 = m-1; // last index of nums1
        int p2 = n-1; // last index of nums2
        while (p1 >= 0 && p2 >=0){ // while both arrays have elements
            if (nums1[p1] > nums2[p2]){ // if the last element of nums1 is greater than the last element of nums2
                nums1[p] = nums1[p1]; // we will set it to the last index of nums1
                p--; // decrement the pointer by 1
                p1--; // decrement the pointer by 1
            } else{
                nums1[p] = nums2[p2]; // if the last element of nums2 is greater than the last element of nums1
                p--; // we will set it to the last index of nums1
                p2--; // decrement the pointer by 1
            }
        }
        while (p2 >= 0){ // if nums1 is empty and nums2 still has elements
            nums1[p] = nums2[p2]; // we will set it to the last index of nums1
            p2--; 
            p--;
        }
    }
}