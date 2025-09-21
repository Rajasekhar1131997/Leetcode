# Leetcode Problem 2455: Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        # initialize the count and total to 0
        count = 0
        total = 0
        # loop through each num in nums list
        for num in nums:
            # check if the number is even and also divisible by 3 or not. if yes, we count and add it to sum
            if num % 3 == 0 and num % 2 == 0:
                count += 1
                total += num
        # we return the average if the count > 0, otherwise 0
        return total//count if count > 0 else 0

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")