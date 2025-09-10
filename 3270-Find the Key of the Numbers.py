# Leetcode Problem 3270: Find the Key of the Numbers
# https://leetcode.com/problems/find-the-key-of-the-numbers/description/
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # using zfill, we make the given number into 4 digit number
        n1 = str(num1).zfill(4)
        n2 = str(num2).zfill(4)
        n3 = str(num3).zfill(4)
        # initialize an empty result list to hold the min/smallest digit
        key_digits = []
        # loop through each three numbers
        for i in range(4):
            # get the smallest number for each digit
            smallest = min(int(n1[i]), int(n2[i]), int(n3[i]))
            # append that smallest digit to key digits list
            key_digits.append(str(smallest))
        # find the key
        key = int("".join(key_digits))
        # return the key
        return key

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")