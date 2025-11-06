# Leetcode Problem 2729: Check if The Number is Fascinating
# https://leetcode.com/problems/check-if-the-number-is-fascinating/description/
class Solution:
    def isFascinating(self, n: int) -> bool:
        # compute 2 * n and convert it into string
        two_n = str(n * 2)
        # compute 3 * n and convert it into string
        three_n = str(n * 3)
        # convert the n into string
        n = str(n)
        # now concatenate all the three strings into one
        concat = n + two_n + three_n
        # return true if the length of that concatenated string is 9 and contain only 1 to 9 digits
        return len(concat) == 9 and set(concat) == set("123456789")

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")