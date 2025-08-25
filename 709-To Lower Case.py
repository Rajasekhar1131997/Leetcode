# Leetcode Problem 709: To Lower Case
# https://leetcode.com/problems/to-lower-case/description/
class Solution:
    def toLowerCase(self, s: str) -> str:
        # initialize an empty list to store each character
        result = []
        # loop through each character in string s
        for char in s:
            # if the current character is in ASCII range of 65 and 90 i.e (Capital letters)
            if 65 <= ord(char) <= 90:
                # convert that character to lower case by adding 32 and add that new character to result
                result.append(chr(ord(char) + 32))
            # if the character is not a capital simply add that character to result
            else:
                result.append(char)
        # convert that list to string using join and return the output
        return "".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")