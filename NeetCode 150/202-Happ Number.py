# Leetcode Problem 202: Happy Number
# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        # Initialize an empty set to check the given number is ending in a loop
        visit = set()
        # while the given number is not in set
        while n not in visit:
            # add that number to the set first
            visit.add(n)
            # Now, find the squares of the given number with helper function
            n = self.sumOfSquares(n)
            # If that number equals 1, return True and conclude as Happy Number
            if n == 1:
                return True
        # If that numbers ends in loop, we return False and conclude as not Happy Number
        return False
    
    # Helper function to find the squares of the given number
    def sumOfSquares(self, n: int) -> int:
        # Initialize the result to 0
        result = 0
        # Loop until the given number is greater than 0
        while n > 0:
            # get each number using % 10 gives the single number
            digit = n % 10
            # Squaring that number
            digit = digit ** 2
            # adding that number to the result
            result += digit
            # we reduce the number by diving with 10
            n = n // 10
        # return the result
        return result
    
print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")