# Leetcode Problem 15: 3Sum
# https://leetcode.com/problems/3sum/description/
# Solving this problem using Two Pointers Approach
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initializing empty list to store lists
        result = []
        # sorting the list
        nums.sort()
        # Using two pointer approach to solve this problem
        # Loop until we complete all the values from the list
        for i in range(len(nums)):
            # check if the previous element is same as the current one, if yes, we continue
            if i!=0 and nums[i] == nums[i-1]:
                continue
            # initializing our left and right pointers
            left = i+1
            right = len(nums) - 1
            # TWo pointers logic
            while left < right:
                # calculating the total
                total = nums[i] + nums[left] + nums[right]
                # checking if our total value is greater than 0
                if total > 0:
                    # we move our right pointer to left
                    right -= 1
                # checking if our total value is less than 0
                elif total < 0:
                    # we move our left pointer to the right
                    left += 1
                # if our total is 0, we add that list to our result list
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # move forward to continue with our list
                    left += 1
                    # Two pointer and also check if our current value is same as previous one, so we can skip it
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        # return the result list
        return result

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1) for auxillary and O(N^2) in worst case")