# Leetcode Problem 2129: Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/description/
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # split the string into words using split command
        words = title.split()
        # initialize an empty result list to store words after performing operations
        result = []
        # loop through each word in words list
        for word in words:
            # if the length of word is <=2, we convert the word to lowercase and add it to result
            if len(word) <= 2:
                result.append(word.lower())
            # otherwise, we need to change the first letter of word to uppercase and rest to lowercase and add it to result list
            else:
                result.append(word.capitalize())
        # return the string after appending
        return " ".join(result)

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")