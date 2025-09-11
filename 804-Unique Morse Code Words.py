# Leetcode Problem 804: Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/description/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # initialize the 26 alphabet letters
        letters = "abcdefghijklmnopqrstuvwxyz"
        # given morse codes for 26 alphabets
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # initialize an empty hash map
        morse_map = {}
        i = 0
        # map each alphabet to morse code
        for code in morse_codes:
            morse_map[letters[i]] = code
            i += 1
        # initialize an empty result set to store unique values
        result = set()
        # for each word in words list
        for word in words:
            # find the morse code
            string = ""
            for char in word:
                string += morse_map[char]
            # add that morse code to result set
            result.add(string)
        # return the length of the result set at the end
        return len(result)

print("Time Complexity: O(N.M)")
print("Space Complexity: O(N)")