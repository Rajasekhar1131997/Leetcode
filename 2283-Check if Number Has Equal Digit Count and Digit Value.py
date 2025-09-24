# Leetcode Problem 2283: Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
class Solution:
    def digitCount(self, num: str) -> bool:
        # initialize an empty hashmap
        hash_map = {}
        # get the frequency of each character from given string
        for char in num:
            hash_map[char] = hash_map.get(char, 0) + 1
        # loop through the given num string with index and character
        for i, n in enumerate(num):
            # get the expected integer
            expected = int(n)
            # find the actual count of the index from hashmap
            actual = hash_map.get(str(i), 0)
            # if the actual is not equal to expected, we return False, otherwise return True
            if expected != actual:
                return False
        return True

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")