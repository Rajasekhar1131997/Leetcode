// 136. Single Number
// https://leetcode.com/problems/single-number/description/
class Solution {
    public int singleNumber(int[] nums) {
        int result = 0; // Initialize result to 0
        for (int num : nums){ // Loop through each number in the array
            result ^= num; // Use XOR operation to find the single number
        }
        return result; // Return the result
    }
}