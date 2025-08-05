# Leetcode Problem 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solving this problem using Sliding Window Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # If the string is empty, we return 0
        if len(s) == 0:
            return 0
        # Initialize an empty set
        characters = set()
        # Initialize the left pointer
        left = 0
        # Initialize the result
        result = 0
        # Initializing the right pointer and looping through each character in string
        for right in range(len(s)):
            # Checking if the current pointer is already present in the set
            while s[right] in characters:
                # Remove the left most character or duplicate from the set
                characters.remove(s[left])
                # Increment the left point by 1 to move forward
                left += 1
            # We keep adding the next value into the set
            characters.add(s[right])
            # Finding the maximum value
            result = max(result, right-left+1)
        return result

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")