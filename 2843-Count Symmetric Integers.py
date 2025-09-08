# Leetcode Problem 2843: Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/description/
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # intialize count to 0 to keep track of number of symmetric integers
        count = 0
        # loop through the given range low to high
        for i in range(low, high+1):
            # convert each number into string
            string = str(i)
            # find the length of each string
            n = len(string)
            # if the string is of odd length, we ignore that string/value and continue
            if n % 2 == 1:
                continue
            # divide the string into half
            half = n // 2
            # get the first half of string
            first_half = string[:half]
            # get the second half of string
            second_half = string[half:]
            # get the sum of first half
            sum1 = sum(int(ch) for ch in first_half)
            # get the sum of second half
            sum2 = sum(int(ch) for ch in second_half)
            # if the first half and second half sum are equal, we count it
            if sum1 == sum2:
                count += 1
        # return the count
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")