# Leetcode Problem 3688: Bitwise OR of Even Numbers in an Array
# https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/description/
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # initialize the result to 0, it will hold the final result after computing
        result = 0
        # loop through each num in nums
        for num in nums:
            # check if that num is even or odd
            if num % 2 == 0:
                # if even, we bitwise OR the even numbers
                result |= num
        # finally, return the result
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")