# Leetcode Problem 3701: Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/description/
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # initialize the even and odd sum to 0
        even_sum = odd_sum = 0
        # loop through each index
        for i in range(len(nums)):
            # if the index is even, we add that number to even sum
            if i % 2 == 0:
                even_sum += nums[i]
            # if the index is odd, we add that number to odd sum
            else:
                odd_sum += nums[i]
        # return the difference
        return even_sum - odd_sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")