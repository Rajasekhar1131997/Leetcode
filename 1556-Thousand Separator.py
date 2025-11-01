# Leetcode Problem 1556: Thousand Separator
# https://leetcode.com/problems/thousand-separator/description/
class Solution:
    def thousandSeparator(self, n: int) -> str:
        # convert the given number into string and reverse it
        s = str(n)[::-1]
        # divide the given string into parts with 3 characters each starting from index 0
        split_parts = [s[i:i+3] for i in range(0, len(s), 3)]
        # join the each part with '.' and return the reverse characters
        return '.'.join(split_parts)[::-1]
    
print("Time Complexity: O(log N)")
print("Space Complexity: O(log N)")