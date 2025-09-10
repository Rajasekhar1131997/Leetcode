# Leetcode Problem 1704: Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # initialize a dictionary of vowels
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # initialize the counts to 0
        a_count = b_count = 0
        # split the given string into two halfs a and b
        a = s[:len(s)//2]
        b = s[(len(s)//2):]
        # get the count of vowels in a string
        for char in a:
            if char in vowels:
                a_count += 1
        # get the count of vowels in b string
        for char in b:
            if char in vowels:
                b_count += 1
        # if their count is equal, then the string halves are alike
        return a_count == b_count

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")