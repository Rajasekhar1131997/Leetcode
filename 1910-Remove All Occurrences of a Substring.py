# Leetcode Problem 1910: Remove All Occurrences of a Substring
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # initialize an empty stack
        stack = []
        # let n be the length of substring
        n = len(part)
        # loop through each character in string s
        for char in s:
            # append each character into stack
            stack.append(char)
            # check if the length of stack is >= n and the concatenation of last three characters is equal to the substring need to be removed
            if len(stack) >= n and ''.join(stack[-n:]) == part:
                # we need to remove the characters from stack until the length of substring
                for i in range(n):
                    stack.pop()
        # finally, return the concatenated string formed using stack list
        return ''.join(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")