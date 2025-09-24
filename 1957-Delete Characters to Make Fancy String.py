# Leetcode Problem 1957: Delete Characters to Make Fancy String
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
class Solution:
    def makeFancyString(self, s: str) -> str:
        # initialize an empty result list to store each character
        result = []
        # loop through each character in given string
        for char in s:
            # add that character to result list
            result.append(char)
            # we need to check the length of the result list and also we need to check if the previously added 3 characters are same or not
            if len(result)>=3 and result[-1] == result[-2] == result[-3]:
                # if yes, we pop the last appended character from the list
                result.pop()
        # return the concatenated result list
        return "".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")