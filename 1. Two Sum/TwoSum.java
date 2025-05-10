// LeetCode 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Below Approach is using Brute Force
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i=0;i<nums.length;i++){
            for (int j=i+1;j<nums.length;j++){
                if (nums[i] + nums[j] == target){
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}

// Approach 2: Using HashMap
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            mp.put(nums[i], i);
        }
        for (int i=0;i<nums.length;i++){
            int complement = target - nums[i];
            if (mp.containsKey(complement) && mp.get(complement) != i){
                return new int[]{i, mp.get(complement)};
            }
        }
        return new int[]{};
    }
}