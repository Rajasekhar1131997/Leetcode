# Leetcode Problem 7: Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        # these are the boundaries of signed 32-bit integer range.
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        # if the given number is less than 0
        if x < 0:
            # we convert the number into string and slicing it in reverse order exlcuding the - symbol and multiplying with -1
            x = int(str(x)[:0:-1]) * -1
        # else, we normally convert the number into string and use slicing to reverse the number
        else:
            x = int(str(x)[::-1])
        # we also make sure to check the boundaries of the given number, if it isn't we return 0
        if x < MIN_INT or x > MAX_INT:
            return 0
        # otherwise, we simply return x
        return x

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# This is another approach to solve the problem
class Solution:
    def reverse(self, x: int) -> int:
        # these are the boundaries of signed 32-bit integer range.
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        # initiliazing the variable sign to hold positive or negative sign
        sign = -1 if x < 0 else 1
        # no matter waht the sign is we change the x to positive and reverse the number
        x = abs(x)
        # the variable reversed_x will hold the reversed value
        reversed_x = 0
        # loop until all the numbers in x are processed
        while x:
            # this will get the last digit from number x
            digit = x % 10
            # for every digit, reversed_x will add that digit to it and increase
            reversed_x = reversed_x * 10 + digit
            # we also decrease the value of x by dividing with 10 to remove processed digit
            x = x // 10
        # we also make sure to multiply it with sign variable
        reversed_x *= sign
        # logic to check out our boundaries
        if reversed_x < MIN_INT or reversed_x > MAX_INT:
            return 0
        # return the reversed_x value
        return reversed_x
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")