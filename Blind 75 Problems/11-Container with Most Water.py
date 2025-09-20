# Leetcode Problem 11: Container with Most Water
# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # intialize the left and right pointers
        left = 0
        right = len(height) - 1
        # let the max_area be 0
        max_area = 0
        # loop through the entire list
        while left<right:
            # find the max area, the max area can be find by using the below
            max_area = max(min(height[left], height[right]) * (right-left), max_area)
            # we check if the left vertical line is smaller than or equal to right vertical line, we move forward, otherwise, we move the right pointer to left
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        # finally, return the maximum area
        return max_area

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")