# Leetcode Problem 66: Plus One
# https://leetcode.com/problems/plus-one/
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if no digits list is given, return 0
        if not digits:
            return 0
        # reversing the list
        digits = digits[::-1]
        # Initalizing carry to 1
        carry = 1
        # Initializing i to keep track of each value
        i = 0
        # Loop until the carry value is 1
        while carry:
            # check if the i value is less than length of digits
            if i < len(digits):
                # if the value is 9, we set the value to 0
                if digits[i] == 9:
                    digits[i] = 0
                # if the value is not 9, we just increment the value and set the carry to 0
                else:
                    digits[i] += 1
                    carry = 0
            # If the above fails, we simply append the one to our digits list and set carry to 0
            else:
                digits.append(1)
                carry = 0
            # We keep increment the i value to move to the next digit
            i += 1
        # we return the reverse digits as result
        return digits[::-1]

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")