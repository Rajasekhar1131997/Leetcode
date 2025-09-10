# Leetcode Problem 2325: Decode the Message
# https://leetcode.com/problems/decode-the-message/description/
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # initialize the 26 alphabets to letters
        letters = "abcdefghijklmnopqrstuvwxyz"
        # initialize i to 0
        i = 0
        # initialize an empty hash map
        hash_map = {}
        # remove all the spaces from the given key
        key = key.replace(" ", "")
        # assign each key value to each letter
        for char in key:
            if char not in hash_map:
                hash_map[char] = letters[i]
                i += 1
        # initialize an empty list to store decoded message
        decoded_msg = []
        # for every char in message
        for char in message:
            # if it's a space, we append that to list
            if char == " ":
                decoded_msg.append(" ")
            # else, we append the key message to list
            else:
                decoded_msg.append(hash_map[char])
        # join the message and return it
        return "".join(decoded_msg)
    
print("Time Complexity: O(N)")
print("Space Complexity: O(N)")