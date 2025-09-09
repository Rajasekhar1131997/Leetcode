# Leetcode Problem 3498: Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/description/
class Solution:
    def reverseDegree(self, s: str) -> int:
        # initialize sum to 0
        sum = 0
        # for each char, find the reverse index using ord('z') - ord(character) + 1
        for index,char in enumerate(s):
            reverse_index_char = ord('z') - ord(char) + 1
            # multiply that reversed index character with index (since it's 1-indexed, we add 1)
            product = reverse_index_char * (index+1)
            # add that product to sum
            sum += product
        # return the sum
        return sum

print("Time Complexity: O(N)")
print("Space Complexity: O(1)")