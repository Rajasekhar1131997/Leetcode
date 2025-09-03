# Leetcode Problem 1544: Make the String Great
# https://leetcode.com/problems/make-the-string-great/description/
class Solution:
    def makeGood(self, s: str) -> str:
        # initialize an empty stack to help process the characters
        stack = []

        # loop through each character in the string s
        for ch in s:
            # check if the stack is not empty, and:
            #   - the top of the stack is not equal to the current character (ensures opposite case)
            #   - the lowercase version of the top of the stack equals the lowercase of the current character
            #     (ensures same letter regardless of case)
            # if both conditions hold, then stack[-1] and ch form a "bad" pair like "aA" or "Bb"
            if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
                # remove the top element since the pair cancels out
                stack.pop()
            else:
                # otherwise, push the current character onto the stack
                stack.append(ch)

        # after processing all characters, join the stack into a final string and return it
        return "".join(stack)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")