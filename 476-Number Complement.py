# Leetcode Problem 476: Number Complement
# https://leetcode.com/problems/number-complement/description/
class Solution:
    def findComplement(self, num: int) -> int:
        # converting the given decimal number into binary number
        binary_num = format(num, "b")
        # converting the binary number into binary string
        binary_string = str(binary_num)
        # finding the complement string
        complement_string = "".join("1" if ch == "0" else "0" for ch in binary_string)
        # converting the complement string into decimal number
        complement_num = int(complement_string, 2)
        # return the complement number
        return complement_num

print("Time Complexity: O(N)")
print("Space Complexity: O(N)")