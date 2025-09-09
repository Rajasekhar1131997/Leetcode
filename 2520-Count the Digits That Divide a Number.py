# Leetcode Problem 2520: Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
class Solution:
    def countDigits(self, num: int) -> int:
        # initialize the count to 0
        count = 0
        # make a copy of given num to temp
        temp = num
        # check if each digit is divisible by given number or not, if yes, we count it
        while num != 0:
            remainder = num % 10
            if temp % remainder == 0:
                count += 1
            num = num // 10
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")