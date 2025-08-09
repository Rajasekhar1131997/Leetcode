# Leetcode Problem 557: Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        #Split the given string into separate words using split function with delimiter (" "-space)
        s = s.split(" ")
        # initialize an empty list to store the reversed word
        result = []
        # loop until it reverses each word in string
        for string in s:
            # converting each word into list, since we can't perform two pointers directly on string
            string = list(string)
            # initializing our pointers left and right
            left, right = 0, len(string) - 1
            # logic to reverse the word
            while left < right:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
            # using join convert the reversed list back to string
            new_string = ''.join(string)
            # append that word to our reversed list
            result.append(new_string)
        # finally, return the overall string separated by space using join and map functions.
        return " ".join(map(str, result))
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")

# We can also solve this problem using slicing each word
class Solution:
    def reverseWords(self, s: str) -> str:
        # initialize an empty result list
        result = []
        # using split function, separate each word
        s = s.split(" ")
        # for each word, using slicing reverse the word and append it to result
        for word in s:
            result.append(word[::-1])
        # return the sentence by joining each word using join function
        return " ".join(result)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")