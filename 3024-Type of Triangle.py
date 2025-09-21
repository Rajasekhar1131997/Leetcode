# Leetcode Problem 3024: Type of Triangle
# https://leetcode.com/problems/type-of-triangle/description/
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # sort the numbers
        a, b, c = sorted(nums)

        # checking the triangle inequality, if it's not possible, we return none
        if a + b <= c:
            return "none"
        
        # if all the sides are equal length, it's equilateral
        if a == b == c:
            return "equilateral"
        # if any of the two sides are equal, it's isosceles
        elif a == b or b == c or c == a:
            return "isosceles"
        # else, we return it as scalene
        else:
            return "scalene"

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")