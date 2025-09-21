# Leetcode Problem 3300: Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/
class Solution:
    def minElement(self, nums: List[int]) -> int:
        # helper function to calculate digit sum
        def calsum(num):
            # initialize the digit sum to 0
            num_sum = 0
            # loop until the num is greater than 0
            while num>0:
                remainder = num % 10
                num_sum += remainder
                num = num // 10
            # return the digit sum
            return num_sum
        # loop through each element in nums
        for i in range(len(nums)):
            # replace each number with their sum of digits
            nums[i] = calsum(nums[i])
        # return the minimum value from nums list
        return min(nums)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")