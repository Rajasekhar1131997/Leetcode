# Leetcode Problem 258: Add Digits
# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num: int) -> int:
        #base case, if the given number is less than 10, we simply return the given number
        if num < 10:
            return num
        # if the given number is > 9, we need to process until it has only one digit
        total = 0
        # while given number is not equal to 0, we process the number everytime
        while num != 0:
            remainder = num % 10
            total += remainder
            num //= 10
        # calling the recurisve function with the new total value
        return self.addDigits(total)

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")



# we can solve this problem using digital root problem
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")