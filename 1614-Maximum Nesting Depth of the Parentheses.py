# Leetcode Problem 1614: Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/
class Solution:
    def maxDepth(self, s: str) -> int:
        # initialize depth variable
        depth = 0
        # initialize max_depth variable to 0
        max_depth = 0
        # loop through each character in string s
        for ch in s:
            # if the character is '(', we increase the depth by 1
            if ch == '(':
                depth += 1
                # we find the max_depth
                max_depth = max(max_depth, depth)
            # if the character is ')', we decrease the depth by 1
            elif ch == ')':
                depth -= 1
        # return the max_depth at the end
        return max_depth
    
print("Time Complexity: O(N)")
print("Space Complexity: O(1)")