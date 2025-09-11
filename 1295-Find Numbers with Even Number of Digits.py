# Leetcode Problem 1295: Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # initialize the count to 0
        count = 0
        # loop through each number in nums list
        for num in nums:
            # convert the number to string and check it's of even or odd length
            string = str(num)
            if len(string) % 2 == 0:
                # if even, we count it
                count += 1
        # return the count of even number of digits
        return count

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")