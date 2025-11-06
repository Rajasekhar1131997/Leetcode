# Leetcode Problem 3210: Find the Encrypted String
# https://leetcode.com/problems/find-the-encrypted-string/description/
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # initialize an empty string
        new_string = ""
        # find the length of given string
        n = len(s)
        # loop through each character in given string
        for i in range(n):
            # now append each character to new string as per the given algorithm
            new_string += s[(i+k)%n]
        # finally, return the new string
        return new_string

print("Time Complexity: O(N^2) -> if considering the worst case, because everytime we are reallocating the new string")
print("Space Complexity: O(N)")

# we can also solve this problem in O(N) by making use of list
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        result = [s[(i+k)%n] for i in range(n)]
        return ''.join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")