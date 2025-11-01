# Leetcode Problem 2574: Left and Right Sum Differences
# https://leetcode.com/problems/left-and-right-sum-differences/description/
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # initialize an empty list to store the result
        answer = []
        # initialize two variables left sum and right sum
        leftsum = rightsum = 0
        # loop through each value in nums list
        for i in range(len(nums)):
            # compute the left sum
            leftsum = sum(nums[:i])
            # compute the right sum
            rightsum = sum(nums[i+1:])
            # compute the absolute difference
            abs_diff = abs(leftsum - rightsum)
            # append that value to answer result
            answer.append(abs_diff)
        # finally, return the answer result
        return answer

print("Time Complexity: O(N^2)")
print("Space Complexity: O(N)")