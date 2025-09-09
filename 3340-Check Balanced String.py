# Leetcode Problem 3340: Check Balanced String
# https://leetcode.com/problems/check-balanced-string/description/
class Solution:
    def isBalanced(self, num: str) -> bool:
        # initialize odd_sum and even_sum to 0
        odd_sum = even_sum = 0
        # loop through each character in num string
        for index, char in enumerate(num):
            # if the index is odd
            if index % 2 == 1:
                # convert the char to int and add it to odd_sum
                number = int(char)
                odd_sum += number
            # if the index is even, we convert the char to int and add it to even_sum
            else:
                number = int(char)
                even_sum += number
        # return true if the string is balanced, otherwise false
        return odd_sum == even_sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")