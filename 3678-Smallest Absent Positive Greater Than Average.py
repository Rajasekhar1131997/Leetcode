# Leetcode Problem 3678: Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/description/
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        # find the average of the nums array
        avg = sum(nums) / len(nums)
        # convert the average to the nearest possible positive integer
        x = floor(avg) + 1
        # base case, if the x value is less than or equal to 0, we modify the x to be 1
        if x <= 0:
            x = 1
        # convert the nums list to set
        nums_set = set(nums)
        # loop though each value ranging from x to 100 as given in constraints
        for i in range(x, 101):
            # if the that value is not present in nums, we return that value, otherwise increment it
            if i not in nums_set:
                return i
        # base case, the above loop checks until only 100, it will not check for 101
        return 101

print("Time Complexity: O(N), it will be O(1) if n<=100")
print("Space Complexity: O(N), it will be O(1) if n <= 100")