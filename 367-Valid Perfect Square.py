# Leetcode Problem 367: Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/description/
# Using Binary Search to solve this problem
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if the given number is less than 2, we return True
        if num < 2:
            return True
        # initialize left to 2 and right value to num // 2
        left, right = 2, num // 2
        # loop until we reach the right value
        while left <= right:
            # find the mid value
            mid = (left + right) // 2
            # find the square of the mid value
            square = mid * mid
            # if the square is equal to the give number, we return True
            if square == num:
                return True
            # if the squared number is less than given number, we increment the left value by adding 1 to the mid
            elif square < num:
                left = mid + 1
            # else, we decrease the mid value by 1 to the right pointer
            else:
                right = mid - 1
        # return False
        return False

print("Time Complexity: O(log N)")
print("Space Complexity: O(1)")