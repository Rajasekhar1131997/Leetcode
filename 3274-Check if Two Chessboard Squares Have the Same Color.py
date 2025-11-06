# Leetcode Problem 3274: Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # initialize a hash map to store series of alphabets from a to h
        alpha_map = {}
        i = 1
        cols = "abcdefgh"
        # logic to add the series to the alphabets using hashmap
        for letter in cols:
            alpha_map[letter] = i
            i += 1
        # we need to perform this operation, only if the provided string is off same length
        if len(coordinate1) == len(coordinate2):
            # find the characters and digits from the given strings
            char1 = coordinate1[0]
            digit1 = coordinate1[1]
            char2 = coordinate2[0]
            digit2 = coordinate2[1]
            # compute the digit sum
            digit_sum = int(digit1) + int(digit2)
            # compute the character sum
            char_sum = alpha_map[char1] + alpha_map[char2]
            # if their sum is even, that means they have the same color, and we return True, otherwise false
            if (digit_sum + char_sum) % 2 == 0:
                return True
            else:
                return False

print("Time Complexity: O(1)")
print("Space Complexity: O(1)")