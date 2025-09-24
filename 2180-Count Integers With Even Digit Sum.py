# Leetcode Problem 2180: Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
class Solution:
    def countEven(self, num: int) -> int:
        # helper function to get the digit sum
        def digitsum(num):
            # if the given number is 0, we return 0
            if num == 0:
                return 0
            # else, we find the total of the given number
            total = 0
            while num != 0:
                remainder = num % 10
                total += remainder
                num //= 10
            return total
        # initialize the count to 0
        count = 0
        # loop through the range starting from 1 to num
        for i in range(1, num+1):
            # if the given number is even, we count it
            if digitsum(i) % 2 == 0:
                count += 1
        # return the count finally
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")