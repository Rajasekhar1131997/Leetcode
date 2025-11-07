# Leetcode Problem 2544: Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/description/
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # convert the given number n into list
        n = [digit for digit in str(n)]
        # initialize a variable flag with 1 and summ to 0
        flag = 1
        summ = 0
        # loop through each number in n list
        for num in n:
            # if the flag is 1, we add it and make the flag to 0
            if flag == 1:
                summ += int(num)
                flag = 0
            # if the flag is 0, we subtract it and make the flag to 1
            else:
                summ -= int(num)
                flag = 1
        # finally, return the summ
        return summ

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")