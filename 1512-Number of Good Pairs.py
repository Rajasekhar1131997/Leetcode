# Leetcode Problem 1512: Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/description/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # initialize the count to 0
        count = 0
        # loop through each number in the list
        for i in range(len(nums)):
            # inner loop through each number and make sure j is greater than i
            for j in range(i+1, len(nums)):
                # i<j condition will be satisfied and we need to check if nums[i] == nums[j]
                if nums[i] == nums[j]:
                    # increment the count
                    count += 1
        # we have the return the count of good pairs encountered
        return count

print("Time Complexity: O(N^2)")
print("Space Complexity: O(1)")