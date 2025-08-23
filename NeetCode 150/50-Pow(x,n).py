# Leetcode Problem 50: Pow(x, n)
# https://leetcode.com/problems/powx-n/description/
# This is one way of solving this problem
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if x value is 0, we return 0
        if x == 0: return 0
        # if n value is 0, any value to the power 0 always return 1
        if n == 0: return 1
        # return the result
        return x**n

print("Time Complexity: O(log |n|)")
print("Space Complexity: O(1)")

# Solving this problem using recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # if x value is 0, we return 0
            if x == 0: return 0
            # if n value is 0, any value to the power 0 always return 1
            if n == 0: return 1
            # recursive function until we process the n the value
            res = helper(x*x, n//2)
            # if the n value is odd, we return x * res else we return res
            return x * res if n %2 else res
        # passing values to the helper recursive function
        res = helper(x, abs(n))
        # return res if n >=0 else we need to return 1/res
        return res if n >=0 else 1/res

print("Time Complexity: O(log |n|)")
print("Space Complexity: O(log |n|)")