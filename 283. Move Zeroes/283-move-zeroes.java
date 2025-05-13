// 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/description/
// Approach: Two Pointers
class Solution {
    public void moveZeroes(int[] nums) { 
        int n = nums.length; // Get the length of the array
        if (n<2) return; // If the array has less than 2 elements, return
        int insert = 0; // Pointer to keep track of the position to insert non-zero elements
        for (int i=0;i<n;i++){ // Iterate through the array
            if(nums[i] !=0){ // If the current element is non-zero
                nums[insert] = nums[i]; // Move it to the insert position
                insert++; // Increment the insert position
            }
        }
        while(insert<n){ // Fill the remaining positions with zeroes
            nums[insert] = 0; // Set the current position to zero
            insert++; // Increment the insert position
        }
    }
}